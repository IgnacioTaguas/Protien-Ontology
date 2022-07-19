# MCBPO
Development of the OWL ontology MCBPO, implemented on Protégé, whose purpose is to provide a consensual knowledge model of proteins.

Other ontologies and resources in the field of proteins already exist, and many of them classificate proteins according to their function; such is tha case of Protein Ontology (PRO). Nevertheless, the classifications used tend to be quite complex, given the complexity of protein functions; this makes them almost inaccessible for people not working on topics specifically related to proteins. The goal of this project is to develop an ontology with a more comprehensive classification, which can be used both by experts on the topic and users that lack deep knowledge on it. To do this, proteins are classified in seven categories according to their function; nonetheless, the ontology contains in-depth knowledge for each protein stored (each protein instance has very specific data regarding its sequence, the gene that encodes it, its fucntion and cellular location at the most detailed level...), in order to make the ontology useful to experts as well.

MCBPO is inteded as a connection between already existing ontologies and databases of the same domain. For this reason, the data was taken from UniProt and GO, as well as PRO, Gene Ontology and NCI Thesaurus. A thorough search of the terms  present in other protein ontologies was carried out, and those already existing were reused in our ontology to avoid knowledge duplicity problems. 

The UniProt and GO databases were parsed using Python, which was also used to classify the proteins. OpenRefine, the most widely used software to import data into the ontology, was not used, as it does not allow to generate URIs from other ontologies, and therefore would not allow the creation of MCBPO as a connection between existing ontologies. For this reason, the ontology was created using Protégé and OBO Edit (tools for ontology visualization), and the instances were introduced with Bash scripts developed by ourselves.

For the ontology validation three tools were used: OOPS! and HermiT, which are ontologies' reasoners, and RDFlib, which is a Python package working with RDF with a SPARQL implementation. In this way, several SPARQL queries were resolved.

This repository has the following files and directories:
  - 
