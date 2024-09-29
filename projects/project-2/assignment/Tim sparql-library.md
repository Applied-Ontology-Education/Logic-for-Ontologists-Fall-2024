**The SPARQL Library of Common Core Ontologies**

The goal of this project is to develop a suite of SPARQL queries that will serve as quality control (QC) checks against the [Common Core Ontologies](https://github.com/CommonCoreOntology/CommonCoreOntologies) suite. These queries will be designed to identify and flag potential issues, ensuring the ontology's integrity, consistency, and adherence to predefined standards.

**Assignment Details**

Your task is to construct SPARQL queries to be included in the [CCO QC workflow](https://github.com/CommonCoreOntology/CommonCoreOntologies/actions). Ideally, your queries will be added to the CCO repository [here](https://github.com/CommonCoreOntology/CommonCoreOntologies/tree/develop/.github/deployment/sparql). 

Your queries will be ranked in terms of difficulty. The lowest - 8 - indicates a rather easy query, while the highest - 1 - will indicate a very sophisticated query. 

For our purposes, the more sophisticated queries will be worth more points than less sophisticated, and you are required to submit enough queries to acquire 100 points according to the following point system: 


  | **Query Sophistication** | **Points** |
  | ------------------------ | ---------- |
  |       1                  |      35    |
  |       2                  |      25    |
  |       3                  |      20    |
  |       4                  |      10    |
  |       5                  |       5    |
  |       6                  |       3    |
  |       7                  |       2    |
  |       8                  |       0    |

You're probably thinking, "why would I submit a level 8 if they're not worth any points?" Great question. Because everyone has to submit at least one level 8. Otherwise, you're permitted to submit in any distribution you choose. For example, you might submit 2 queries for level one (70 points), one for level 3 (20 points), one for 4 (10 points), and one for kata 8 (0 points but required). 

It is your responsibility and the responsibility of your peers reviewing your submission in PR to determine whether your submission is ranked appropriately. In the event that consensus is reached that your query is ranked inappropriately, you must work with your peers to revise the submission so that it is either more or less challenging, accordingly. You are not permitted to submit new queries with different strengths after PRs are open, but must instead revise your PRs. So, think hard about how challenging your submission is. 

**Template**

The SPARQL queries should have the template: 
Title
    (descriptive title of the query)
Constraint Description: 
    (description of the query functionality)
Severity:
    (select "Warning" or "Error")

Your query should end with a BIND clause and an associated ?error in the SELECT. For example: 

  - BIND (concat("WARNING: The following ontology elements have the same rdfs:label ", str(?element), " and ", str(?element2)) AS ?error)

**Guidance**

A few tips for developing effective SPARQL queries for the Common Core Ontologies (CCO):
  - Review the [existing SPARQL queries](https://github.com/CommonCoreOntology/CommonCoreOntologies/tree/develop/.github/deployment/sparql) so as not to duplicate work
  - Review [documentation and design patterns](https://github.com/CommonCoreOntology/CommonCoreOntologies/tree/develop/documentation) to understand stucture of CCO
  - Understand common issues in ontologies; [explore the OOPS!](https://oa.upm.es/35873/1/INVE_MEM_2014_192872.pdf) list here for inspiration
  - Observe annotation conventions, e.g. use of labels, comments, etc. must be present and accurate

When creating queries, start with simple quality control checks and build complexity through practice. Feel free to leverage generative AI for this project. Also, feel free to collaborate with peers. 

Be sure to test your queries. You may do this in Protege or in the [SPARQL playground](https://atomgraph.github.io/SPARQL-Playground/). 

**Title: SPARQL Query to Identify Acronyms**

Constraint Description: This SPARQL query is designed to identify terms in an ontology (either classes or properties) that have labels resembling acronyms.

Severity: Warning

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?term ?label ?warning
WHERE {
  # Extract all terms (classes and properties) with labels
  {
    ?term a owl:Class .
  }
  UNION
  {
    ?term a owl:ObjectProperty .
  }
  UNION
  {
    ?term a owl:DatatypeProperty .
  }

  # Get the label of the term
  ?term rdfs:label ?label .

  # Check for labels that look like acronyms (upper case and short)
  FILTER(
    REGEX(?label, "^[A-Z0-9-\\.]{2,6}$", "i")
  )

  # Bind a warning message if the label matches the regex
  BIND (concat("WARNING: The term ", str(?term), " has a label that looks like an acronym: ", ?label) AS ?warning)
}
```
**Title: Axiom Type and Anonymous Class**

Constraint Description: (Principle of Single Inheritance) SPARQL query to check an ontology for the use of subclass or equivalent class axioms whereby a class is defined to be a subclass or equivalent class of an anonymous class

Severity: Warning

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?class ?axiomType ?anonymousClass ?warning
WHERE {
  {
    # Subclass axiom where the superclass is anonymous (blank node)
    ?class rdfs:subClassOf ?anonymousClass .
    FILTER(isBlank(?anonymousClass))  # Check if the superclass is anonymous
    BIND("subClassOf" AS ?axiomType)
  }
  UNION
  {
    # Equivalent class axiom where the equivalent class is anonymous (blank node)
    ?class owl:equivalentClass ?anonymousClass .
    FILTER(isBlank(?anonymousClass))  # Check if the equivalent class is anonymous
    BIND("equivalentClass" AS ?axiomType)
  }

  # Bind a warning message when an anonymous class is found
  BIND(concat("WARNING: The class ", str(?class), " has an anonymous ", ?axiomType, " axiom.") AS ?warning)
}
```

**Title: Reused Term, Axiom type and Axiom Detail**

Constraint Description: (Preservation of Meaning of Higher-Level Ontology Terms) SPARQL query that checks whether an ontology reuses a term from a higher-level ontology and adds new content to it through the addition of an axiom.

Severity: Error.

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT DISTINCT ?reusedTerm ?axiomType ?axiomDetail ?error
WHERE {
  # 1. Identify terms that are reused from another ontology (by detecting external namespaces)
  ?reusedTerm a owl:Class .
  FILTER(STRSTARTS(STR(?reusedTerm), "http://higher-level-ontology-namespace.org/")) # Replace with actual namespace

  # 2. Check if the reused term is extended in the current ontology with a subclass axiom
  {
    ?reusedTerm rdfs:subClassOf ?axiomDetail .
    BIND("subClassOf" AS ?axiomType)
  }
  UNION
  # 3. Check if the reused term is extended with an equivalent class axiom
  {
    ?reusedTerm owl:equivalentClass ?axiomDetail .
    BIND("equivalentClass" AS ?axiomType)
  }
  UNION
  # 4. Check if additional restrictions are added to the reused term
  {
    ?reusedTerm rdfs:subClassOf [ owl:onProperty ?property ; owl:someValuesFrom ?axiomDetail ] .
    BIND(CONCAT("Restriction on property: ", STR(?property)) AS ?axiomType)
  }
  
  # BIND an error message for reused terms
  BIND(CONCAT("ERROR: The reused term ", STR(?reusedTerm), " is extended with a ", ?axiomType, " axiom.") AS ?error)
}
```
**Title: Checking for Plurals**

Constraint Description: All terms in your ontology should be nouns and noun-phrases that are singular in number. This query allows a user to identify ontology terms that potentially have plural labels, which might not follow ontology design conventions.

Severity: Warning.

```sparql

PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?term ?label ?warning
WHERE {
  # Extract all classes and properties
  {
    ?term a owl:Class .
  }
  UNION
  {
    ?term a owl:ObjectProperty .
  }
  UNION
  {
    ?term a owl:DatatypeProperty .
  }
  
  # Get the label of the term
  ?term rdfs:label ?label .

  # Filter for terms that have labels potentially indicating plurals
  FILTER(
    REGEX(?label, "(s|es|ies)$", "i")
  )

  # Bind a warning message for terms with plural-like labels
  BIND(CONCAT("WARNING: The term '", ?label, "' appears to be plural.") AS ?warning)
}
```
**Title: Query to Detect Negative Terms**

Constraint Description: This query will return all terms in the ontology that have labels containing one of the negative terms listed. This can help identify terms that may introduce negation or exclusion concepts, which might require further review depending on the ontology's modeling approach. This query helps you identify negative terms in your ontology and, at the same time, generates warnings if there are ontology elements that have identical labels.

Severity: Warning.

```sparql

PPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?element ?element2 ?label1 ?label2 ?error
WHERE {
  {
    # Extract all classes with labels
    ?element a owl:Class .
  }
  UNION
  {
    # Extract all object properties with labels
    ?element a owl:ObjectProperty .
  }
  UNION
  {
    # Extract all datatype properties with labels
    ?element a owl:DatatypeProperty .
  }

  # Get the label of the first element
  ?element rdfs:label ?label1 .

  # Detect negative terms in the first element's label
  FILTER(REGEX(?label1, "(?i)\\b(not|non|no|without|absent|null|empty|void|false)\\b"))

  # Find other elements with the same label
  {
    ?element2 a owl:Class .
  }
  UNION
  {
    ?element2 a owl:ObjectProperty .
  }
  UNION
  {
    ?element2 a owl:DatatypeProperty .
  }

  # Get the label of the second element
  ?element2 rdfs:label ?label2 .

  # Check for duplicate labels
  FILTER(?label1 = ?label2)

  # Avoid self-matching (make sure we don't compare the same element)
  FILTER(?element != ?element2)

  # Bind an error message for duplicate negative terms
  BIND(CONCAT("ERROR: The terms ", STR(?element), " and ", STR(?element2), " have the same label: '", ?label1, "'") AS ?error)
}

```
**Title: Detect Ellipses**

Constraint Description: This query will return a list of terms (both classes and properties) whose labels contain ellipses. You can use this to identify and review any such labels that may be incorrectly or ambiguously defined in the ontology.

Severity: Warning

```sparql

PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?term ?label ?warning
WHERE {
  {
    # Extract all classes with labels
    ?term a <http://www.w3.org/2002/07/owl#Class> .
  }
  UNION
  {
    # Extract all object properties with labels
    ?term a <http://www.w3.org/2002/07/owl#ObjectProperty> .
  }
  UNION
  {
    # Extract all datatype properties with labels
    ?term a <http://www.w3.org/2002/07/owl#DatatypeProperty> .
  }

  # Get the label of the term
  ?term rdfs:label ?label .

  # Filter for labels that contain ellipses (three dots)
  FILTER(CONTAINS(?label, "..."))

  # Bind a warning message for terms with ellipses in the label
  BIND(CONCAT("WARNING: The label '", ?label, "' contains ellipses.") AS ?warning)
}

```

**Title: IRI Subject Validation and Annotation Check**

Constraint Description: This SPARQL query checks if a specific IRI is the subject of any triple in an RDF dataset or ontology. It also checks how a specific IRI is used and whether it has appropriate annotations, the query ensures that the data is well-structured, properly annotated, and used according to the design principles of the ontology

Severity: Error. 

```sparql

PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?predicate ?object ?annotationProperty ?annotationValue ?error
WHERE {
  # Check if the IRI is the subject of a triple
  <http://example.org/yourIRI> ?predicate ?object .

  # Check for annotations on the IRI
  OPTIONAL {
    <http://example.org/yourIRI> ?annotationProperty ?annotationValue .
    FILTER(?annotationProperty IN (rdfs:label, rdfs:comment, owl:versionInfo))
  }
  
  # Bind an error message
  BIND(CONCAT("ERROR: The IRI <http://example.org/yourIRI> is the subject of a triple with predicate '", STR(?predicate), "' and object '", STR(?object), "'.") AS ?error)
}
```
