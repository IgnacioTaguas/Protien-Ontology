from re import search,sub
from Bio import SeqIO

#We create a dictionary

records_dict = {}

#We save the information that can be retrieved from the parser in the dictionary

record_num = 0

for record in SeqIO.parse("uniprot_test.dat", "swiss"):
    record_num += 1
    records_dict[str(record_num)] = {}
    #Protein accesion
    try:
        prot_accession = record.id
        records_dict[str(record_num)]["prot_accession"] = prot_accession
    except:
        records_dict[str(record_num)]["prot_accession"] = "NULL"
    #Protein identifier
    try:
        prot_identifier = record.name
        records_dict[str(record_num)]["prot_identifier"] = prot_identifier
    except:
        records_dict[str(record_num)]["prot_identifier"] = "NULL"
    #Protein name
    try:
        temp = record.description
        temp = sub(" {.+?}","",temp)
        match = search("=(.+?);",temp)
        prot_name = match.group(1)
        records_dict[str(record_num)]["prot_name"] = prot_name
    except:
        records_dict[str(record_num)]["prot_name"] = "NULL"
    #Protein sequence
    try:
        prot_sequence = str(record.seq)
        records_dict[str(record_num)]["prot_sequence"] = prot_sequence
    except:
        records_dict[str(record_num)]["prot_sequence"] = "NULL"
    #Protein length
    try:
        prot_length = len(prot_sequence)
        records_dict[str(record_num)]["prot_length"] = prot_length
    except:
        records_dict[str(record_num)]["prot_length"] = "NULL"
    #Protein keywords
    try:
        prot_keywords = record.annotations["keywords"]
        records_dict[str(record_num)]["prot_keywords"] = prot_keywords
    except:
        records_dict[str(record_num)]["prot_keywords"] = []
    #Gene identifier
    try:
        temp = str(record.dbxrefs)
        match = search("GeneID:(.+?)\'",temp)
        gene_identifier = match.group(1)
        records_dict[str(record_num)]["gene_identifier"] = gene_identifier
    except:
        records_dict[str(record_num)]["gene_identifier"] = "NULL"        
    #Gene name
    try:       
        temp = record.annotations["gene_name"]
        temp = sub(" {.+?}","",temp)
        match = search("=(.+?);",temp)
        gene_name = match.group(1).split(",")[0]
        records_dict[str(record_num)]["gene_name"] = gene_name
    except:
        records_dict[str(record_num)]["gene_name"] = "NULL"
    #Organism identifier
    try:
        org_identifier = record.annotations["ncbi_taxid"][0]
        records_dict[str(record_num)]["org_identifier"] = org_identifier
    except:
        records_dict[str(record_num)]["org_identifier"] = "NULL"
    #Organism name
    try:
        temp = record.annotations["organism"]
        org_name = sub(" \(.+\)","",temp)
        records_dict[str(record_num)]["org_name"] = org_name
    except:
        records_dict[str(record_num)]["org_name"] = "NULL"

print("Done")

#We save the information that cannot be retrieved from the parser in the dictionary
        
record_num = 0

with open("uniprot_test.dat","r") as uniprot_file:
    for line in uniprot_file:
        
        if search("^ID",line):
            record_num +=1
            records_dict[str(record_num)]["prot_location_identifier"] = []
            records_dict[str(record_num)]["prot_location"] = []
            records_dict[str(record_num)]["prot_function_identifier"] = []
            records_dict[str(record_num)]["prot_function"] = []
            records_dict[str(record_num)]["prot_process_identifier"] = []
            records_dict[str(record_num)]["prot_process"] = []

        #Protein location
        if search("DR   GO; GO:.+?; C:.+?;",line):
            match = search("DR   GO; (GO:.+?); C:(.+?);",line)
            prot_location_identifier = match.group(1)
            prot_location = match.group(2)
            records_dict[str(record_num)]["prot_location_identifier"].append(prot_location_identifier)
            records_dict[str(record_num)]["prot_location"].append(prot_location)
            
        #Protein function
        if search("DR   GO; GO:.+?; F:.+?;",line):
            match = search("DR   GO; (GO:.+?); F:(.+?);",line)
            prot_function_identifier = match.group(1)
            prot_function = match.group(2)
            records_dict[str(record_num)]["prot_function_identifier"].append(prot_function_identifier)
            records_dict[str(record_num)]["prot_function"].append(prot_function)

        #Protein process
        if search("DR   GO; GO:.+?; P:.+?;",line):
            match = search("DR   GO; (GO:.+?); P:(.+?);",line)
            prot_process_identifier = match.group(1)
            prot_process = match.group(2)
            records_dict[str(record_num)]["prot_process_identifier"].append(prot_process_identifier)
            records_dict[str(record_num)]["prot_process"].append(prot_process)

print("Done")

#We create a file with all the terms that will be useful for our prediction

#prediction_array = []
#for key in records_dict.keys():
#    
#        record = records_dict[key]
#        locations = record["prot_location"]
#        functions = record["prot_function"]
#        processes = record["prot_process"]
#        keywords = record["prot_keywords"]
#        elements = locations + functions + processes + keywords
#        
#        if elements != []:
#            for element in elements:
#                if element not in prediction_array:
#                    prediction_array.append(element)
#
#prediction_file = open("prediction.txt","w")
#for element in prediction_array:
#    prediction_line = str(str(element)+"\n")
#    prediction_file.write(prediction_line)
#prediction_file.close()
#
#print("Done")

#We predict the functional group where each protein can be placed
#This is a lexical prediction based on the terms that appear in each protein definition

structural = ["structural","extracellular","wall","cytoskeleton","microtubule","myosin","actin","cadherin","adhesion","junction","organisation","remodelling"]
storage = ["storage","vacuole","seed","egg","milk","aminoacids","metal","zinc","magnesium","manganese","starvation"]
transport = ["transport","transmembrane","channel","carrier","import","export","migration"]
catalytic = ["catalytic","enzyme","activator","inhibitor","oxidoreductase","transferase","isomerase","lyase","hydrolase","ligase","helicase","kinase","dehydrogenase","oxidase","protease","endonuclease","nuclease","phosphatase","ATPase","GTPase","peroxidase","peptidase","monooxygenase","deaminase","isomerase","FAD","NAD"]
regulatory = ["regulation","inducer","repressor","positive","negative","replication","transcription","splicing","termination","DNA","RNA","nucleus","nucleolus","chromosome","chromatin"]
signaling_receptor = ["signaling","secreted","secretory","signal transduction","chemotaxis","hormone","cytokin","steroid","glycoprotein","receptor","perception","detection"]
immunological_infectious = ["inmunological","immunity","innate","adaptive","defense","inflamatory","antimicrobial","Ig","T", "B","infectious","infection","pathogenesis","virulence","host","toxin","viral","virion","allergen"]

for key in records_dict.keys():

        prediction = []
        record = records_dict[key]
        locations = record["prot_location"]
        functions = record["prot_function"]
        processes = record["prot_process"]
        keywords = record["prot_keywords"]
        elements = locations + functions + processes + keywords
        elements = sub("['\[\],]","",str(elements)).split(" ")
        
        if bool(set(elements)&set(structural)): prediction.append("Structural")
        if bool(set(elements)&set(storage)): prediction.append("Storage")
        if bool(set(elements)&set(transport)): prediction.append("Transport")
        if bool(set(elements)&set(catalytic)): prediction.append("Catalytic")
        if bool(set(elements)&set(regulatory)): prediction.append("Regulatory")
        if bool(set(elements)&set(signaling_receptor)): prediction.append("Signaling or Receptor")
        if bool(set(elements)&set(immunological_infectious)): prediction.append("Immunological or Infectious")
        records_dict[key]["prot_classification"] = prediction

print("Done")            

#We create a tabular file with the protein information
#We only include the records that have a gene identifier and with only one functional prediction

csv_file = open("uniprot.csv","w")
csv_file.close()

csv_file = open("uniprot.csv","a")
header= "prot_accession;prot_identifier;prot_name;\
prot_location_indetifier_1;prot_location_1;\
prot_location_indetifier_2;prot_location_2;\
prot_location_indetifier_3;prot_location_3;\
prot_function_indetifier_1;prot_function_1;\
prot_function_indetifier_2;prot_function_2;\
prot_function_indetifier_3;prot_function_3;\
prot_process_indetifier_1;prot_process_1;\
prot_process_indetifier_2;prot_process_2;\
prot_process_indetifier_3;prot_process_3;\
prot_classification;prot_length;prot_sequence;\
gene_identifier; gene_name;org_identifier;org_name\n"        
csv_file.write(header)

for key in records_dict.keys():
    
    if records_dict[key]["gene_identifier"]!="NULL" and len(records_dict[key]["prot_classification"])==1:
        
        record = records_dict[key]
        prot_accession = str(record["prot_accession"])
        prot_identifer = str(record["prot_identifier"])
        prot_name = str(record["prot_name"])
        
        try: prot_location_identifier_1 = str(record["prot_location_identifier"][0])
        except: prot_location_identifier_1 = ""
        try: prot_location_identifier_2 = str(record["prot_location_identifier"][1])
        except: prot_location_identifier_2 = ""
        try: prot_location_identifier_3 = str(record["prot_location_identifier"][2])
        except: prot_location_identifier_3 = ""
        try: prot_location_1 = str(record["prot_location"][0])
        except: prot_location_1 = ""
        try: prot_location_2 = str(record["prot_location"][1])
        except: prot_location_2 = ""
        try: prot_location_3 = str(record["prot_location"][2])
        except: prot_location_3 = ""
            
        try: prot_function_identifier_1 = str(record["prot_function_identifier"][0])
        except: prot_function_identifier_1 = ""
        try: prot_function_identifier_2 = str(record["prot_function_identifier"][1])
        except: prot_function_identifier_2 = ""
        try: prot_function_identifier_3 = str(record["prot_function_identifier"][2])
        except: prot_function_identifier_3 = ""
        try: prot_function_1 = str(record["prot_function"][0])
        except: prot_function_1 = ""
        try: prot_function_2 = str(record["prot_function"][1])
        except: prot_function_2 = ""
        try: prot_function_3 = str(record["prot_function"][2])
        except: prot_function_3 = "" 
        
        try: prot_process_identifier_1 = str(record["prot_process_identifier"][0])
        except: prot_process_identifier_1 = ""
        try: prot_process_identifier_2 = str(record["prot_process_identifier"][1])
        except: prot_process_identifier_2 = ""
        try: prot_process_identifier_3 = str(record["prot_process_identifier"][2])
        except: prot_process_identifier_3 = ""
        try: prot_process_1 = str(record["prot_process"][0])
        except: prot_process_1 = ""
        try: prot_process_2 = str(record["prot_process"][1])
        except: prot_process_2 = ""
        try: prot_process_3 = str(record["prot_process"][2])
        except: prot_process_3 = ""         
    
        prot_classification = str(record["prot_classification"][0])
        prot_length = str(record["prot_length"])
        prot_sequence = str(record["prot_sequence"])
        gene_identifier = str(record["gene_identifier"])
        gene_name = str(record["gene_name"])
        org_identifier = str(record["org_identifier"])
        org_name = str(record["org_name"])

        line = str(prot_accession+";"+prot_identifer+";"+prot_name+";"+\
                   prot_location_identifier_1+";"+prot_location_1+";"+\
                   prot_location_identifier_2+";"+prot_location_2+";"+\
                   prot_location_identifier_3+";"+prot_location_3+";"+\
                   prot_function_identifier_1+";"+prot_function_1+";"+\
                   prot_function_identifier_2+";"+prot_function_2+";"+\
                   prot_function_identifier_3+";"+prot_function_3+";"+\
                   prot_process_identifier_1+";"+prot_process_1+";"+\
                   prot_process_identifier_2+";"+prot_process_2+";"+\
                   prot_process_identifier_3+";"+prot_process_3+";"+\
                   prot_classification+";"+prot_length+";"+prot_sequence+";"+\
                   gene_identifier+";"+gene_name+";"+org_identifier+";"+org_name+"\n")
                          
        csv_file.write(line) 
               
csv_file.close()

print("Done")
