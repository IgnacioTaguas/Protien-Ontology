import rdflib
g = rdflib.Graph()
g.parse("MCBPO.owl")

#############################################
#METRICS
#############################################

#Number of protein classes
#7 (Literal - Integer)
query1 = g.query("""
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        SELECT (COUNT (DISTINCT ?protein_class) AS ?num_protein_class)
        WHERE
        {?protein_class rdfs:subClassOf <http://purl.obolibrary.org/obo/NCIT_C17021> .
        }""")
for result in query1: print(result)

#Number of proteins
#1198 (Literal - Integer)
query2 = g.query("""
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        SELECT (COUNT (DISTINCT ?protein) AS ?num_proteins)
        WHERE
        {?protein rdf:type ?protein_class .
         ?protein_class rdfs:subClassOf <http://purl.obolibrary.org/obo/NCIT_C17021> .
        }""")
for result in query2: print(result)   

#Number of genes
#1169 (Literal - Integer)
query3 = g.query("""
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        SELECT (COUNT (DISTINCT ?gene) AS ?num_genes)
        WHERE
        {?gene rdf:type <http://purl.obolibrary.org/obo/NCIT_C16612> .
        }""")
for result in query3: print(result) 

#Number of species
#384 (Literal - Integer)
query4 = g.query("""
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        SELECT (COUNT (DISTINCT ?species) AS ?num_species)
        WHERE
        {?species rdf:type <http://purl.obolibrary.org/obo/NCIT_C45293> .
        }""")
for result in query4: print(result)

#Number of locations
#103 (Literal - Integer)
query5 = g.query("""
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        SELECT (COUNT (DISTINCT ?location) AS ?num_locations)
        WHERE
        {?location rdf:type <http://purl.obolibrary.org/obo/NCIT_C13282> .
        }""")
for result in query5: print(result)

#Number of functions
#236 (Literal - Integer)
query6 = g.query("""
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        SELECT (COUNT (DISTINCT ?function) AS ?num_functions)
        WHERE
        {?function rdf:type <http://purl.obolibrary.org/obo/NCIT_C18967> .
        }""")
for result in query6: print(result)

#Number of processes
#335 (Literal - Integer)
query7 = g.query("""
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        SELECT (COUNT (DISTINCT ?process) AS ?num_processes)
        WHERE
        {?process rdf:type <http://purl.obolibrary.org/obo/NCIT_C17828> .
        }""")
for result in query7: print(result)

#############################################
#LICENSE
#############################################

#License
#http://creativecommons.org/licenses/by/4.0/ (Literal)
query8 = g.query("""
        PREFIX dc:<http://purl.org/dc/elements/1.1/> 
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO>
        SELECT ?license
        WHERE
        {base: dc:rights ?license .
        }""")
for result in query8: print(result)

#############################################
#URIS AND NAMES
#############################################

#URIs and names for the protein classes
#http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#Structural (URI)
query9 = g.query("""
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        SELECT DISTINCT ?protein_class ?protein_class_name
        WHERE
        {?protein_class rdfs:subClassOf <http://purl.obolibrary.org/obo/NCIT_C17021> .
         ?protein_class rdfs:label 'Structural'
        }""")
for result in query9: print(result)

#URI, ID, name for a protein
#http://purl.uniprot.org/uniprot/A0A344 (URI)
#ACCD_COFAR (Literal)
#Acetyl-coenzyme A carboxylase carboxyl transferase subunit beta, chloroplastic (Literal)
query10 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT ?protein ?protein_id ?protein_name
        WHERE
        {?protein base:hasAccessionNumber 'A0A344' .
         ?protein base:hasProtID ?protein_id .
         ?protein base:hasProtName ?protein_name .
        }""")
for result in query10: print(result)

#URI and name for a gene
#http://www.semanticweb.org/a/ontologies/2020/0/MCBPO/4421772 (URI)
#accD (Literal)
query11 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT ?gene ?gene_name
        WHERE
        {?gene base:hasGeneID '4421772' .
         ?gene base:hasGeneName ?gene_name .
        }""")
for result in query11: print(result)

#URI and name for a species
#http://www.uniprot.org/taxonomy/13443 (URI)
#Coffea arabica (Literal)
query12 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT ?species ?species_name
        WHERE
        {?species base:hasSpeciesID '13443' .
         ?species base:hasSpeciesName ?species_name .
        }""")
for result in query12: print(result)

#URI and name for a locations
#https://www.ebi.ac.uk/QuickGO/term/GO:0009317 (URI)
#acetyl-CoA carboxylase complex (Literal)
query13 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT ?location ?location_name
        WHERE
        {?location base:hasLocationID 'GO:0009317' .
         ?location base:hasLocationName ?location_name .
        }""")
for result in query13: print(result)

#URI and name for a function
#https://www.ebi.ac.uk/QuickGO/term/GO:0003989 (URI)
#acetyl-CoA carboxylase activity (Literal)
query14 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT ?function ?function_name
        WHERE
        {?function base:hasFunctionID 'GO:0003989' .
         ?function base:hasFunctionName ?function_name .
        }""")
for result in query14: print(result)

#URI and name for a process
#https://www.ebi.ac.uk/QuickGO/term/GO:0006633 (URI)
#fatty acid biosynthetic process (Literal)
query15 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT ?process ?process_name
        WHERE
        {?process base:hasProcessID 'GO:0006633' .
         ?process base:hasProcessName ?process_name .
        }""")
for result in query15: print(result)

#############################################
#TAXONOMY
#############################################

#Type of protein for a given protein
#Transport (Literal)
query16 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#> 
        SELECT ?protein_class_name
        WHERE
        {?protein base:hasAccessionNumber 'P63115' .
        ?protein rdf:type ?protein_class .
        ?protein_class rdfs:subClassOf <http://purl.obolibrary.org/obo/NCIT_C17021> .
        ?protein_class rdfs:label ?protein_class_name .
        }""")
for result in query16: print(result)

#############################################
#PROPERTIES
#############################################

#Gene that codes a given protein
#Slc7a10 (Literal)
query17 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT ?gene_name
        WHERE
        {?protein base:hasAccessionNumber 'P63115' .
         ?protein base:isCodedByGene ?gene .
         ?gene base:hasGeneName ?gene_name .
        }""")
for result in query17: print(result)

#Locations for a given protein
#apical dendrite (Literal)
#neuronal cell body (Literal)
#integral component of plasma membrane (Literal)
query18 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT ?location_name
        WHERE
        {?protein base:hasAccessionNumber 'P63115' .
         ?protein base:isInLocation ?location .
         ?location base:hasLocationName ?location_name .
        }""")
for result in query18: print(result)

#Functions for a given protein
#L-amino acid transmembrane transporter activity (Literal)
query19 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT ?function_name
        WHERE
        {?protein base:hasAccessionNumber 'P63115' .
         ?protein base:hasFunction ?function .
         ?function base:hasFunctionName ?function_name .
        }""")
for result in query19: print(result)

#Process for a given protein
#D-alanine transport (Literal)
#D-serine transport (Literal)
#neutral amino acid transport (Literal)
query20 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT ?process_name
        WHERE
        {?protein base:hasAccessionNumber 'P63115' .
         ?protein base:isInvolvedIn ?process .
         ?process base:hasProcessName ?process_name .
        }""")
for result in query20: print(result)

#Length for a given protein
#530 (Literal - Integer)
#amino acids (Literal)
query21 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT ?length_value ?length_unit
        WHERE
        {?protein base:hasAccessionNumber 'P63115' .
         ?protein base:hasLength ?length .
         ?length base:hasLengthValue ?length_value .
         ?length base:hasLengthUnit ?length_unit .
        }""")
for result in query21: print(result)

#Proteins coded by a given gene
#Acyl-CoA-binding domain-containing protein 4 (Literal)
query22 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT ?protein_name
        WHERE
        {?gene base:hasGeneID '79777' .
         ?protein base:isCodedByGene ?gene .
         ?protein base:hasProtName ?protein_name .
        }""")
for result in query22: print(result)

#Proteins in a given location
#Aspartate aminotransferase, cytoplasmic isozyme 1 (Literal)
#Probable cell wall protein ARB_06477 (Literal)
#Diacylglycerol acyltransferase/mycolyltransferase Ag85A (Literal)
#34 kDa antigenic protein homolog (Literal)
#35 kDa protein (Literal)
query23 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT DISTINCT ?protein_name
        WHERE
        {?location base:hasLocationID 'GO:0005618' .
         ?protein base:isInLocation ?location .
         ?protein base:hasProtName ?protein_name .
        }""")
for result in query23: print(result)

#Proteins with a given function
#Acyl-CoA-binding domain-containing protein 6 (Literal)
#Acyl-CoA-binding protein homolog 3 (Literal)
#Putative acyl-CoA-binding protein (Literal)
#Acyl-CoA-binding domain-containing protein 5 (Literal)
#Acyl-CoA-binding domain-containing protein 4 (Literal)
#Acyl-CoA-binding domain-containing protein 2 (Literal)
#Virion membrane protein A16 homolog (Literal)
#Acyl-CoA-binding protein homolog 1 (Literal)
#Acyl-CoA-binding protein (Literal)
query24 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT DISTINCT ?protein_name
        WHERE
        {?function base:hasFunctionID 'GO:0008289' .
         ?protein base:hasFunction ?function .
         ?protein base:hasProtName ?protein_name .
        }""")
for result in query24: print(result)

#Proteins involved in a given process
#Ataxin-7-like protein 3B (Literal)
#Putative regulator AbrB (Literal)
query25 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT DISTINCT ?protein_name
        WHERE
        {?process base:hasProcessID 'GO:0010468' .
         ?protein base:isInvolvedIn ?process .
         ?protein base:hasProtName ?protein_name .
        }""")
for result in query25: print(result)

#############################################
#INTERCONNECTIVITY
#############################################

#Proteins that have the same name as a given protein
#Q9NS82 (Literal)
query26 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT DISTINCT ?similar_protein_accesion
        WHERE
        {?protein base:hasAccessionNumber 'P63115' .
         ?protein base:isSameProteinAs ?similar_protein .
         ?similar_protein base:hasAccessionNumber ?similar_protein_accesion
        }""")
for result in query26: print(result)

#Genes that have the same name as a given gene
#24153212 (Literal)
#34178287 (Literal)
#998201 (Literal)
query27 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT DISTINCT ?similar_gene_id
        WHERE
        {?gene base:hasGeneID '5382663' .
         ?gene base:isSameGeneAs ?similar_gene .
         ?similar_gene base:hasGeneID ?similar_gene_id
        }""")
for result in query27: print(result)

#Locations that are shared by two given proteins
#chromatin (Literal)
#nucleus (Literal)
query28 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT DISTINCT ?location_name
        WHERE
        {?protein base:hasAccessionNumber 'P16909' .
         ?protein base:isInLocation ?location .
         ?other_protein base:hasAccessionNumber 'P14196' .
         ?other_protein base:isInLocation ?other_location .
         FILTER (?location = ?other_location) .
         ?location base:hasLocationName ?location_name .
        }""")
for result in query28: print(result)

#Functions that are shared by two given proteins
#monooxygenase activity (Literal)
#FAD binding (Literal)
query29 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT DISTINCT ?function_name
        WHERE
        {?protein base:hasAccessionNumber 'Q88FY2' .
         ?protein base:hasFunction ?function .
         ?other_protein base:hasAccessionNumber 'D4B1Y1' .
         ?other_protein base:hasFunction ?other_function .
         FILTER (?function = ?other_function) .
         ?function base:hasFunctionName ?function_name .
        }""")
for result in query29: print(result)

#Processes that are shared by two given proteins
#hemicellulose catabolic process (Literal)
#arabinan catabolic process (Literal)
query30 = g.query("""
        PREFIX base:<http://www.semanticweb.org/a/ontologies/2020/0/MCBPO#>
        SELECT DISTINCT ?process_name
        WHERE
        {?protein base:hasAccessionNumber 'A2QT85' .
         ?protein base:isInvolvedIn ?process .
         ?other_protein base:hasAccessionNumber 'A2Q7E0' .
         ?other_protein base:isInvolvedIn ?other_process .
         FILTER (?process = ?other_process) .
         ?process base:hasProcessName ?process_name .
        }""")
for result in query30: print(result)
