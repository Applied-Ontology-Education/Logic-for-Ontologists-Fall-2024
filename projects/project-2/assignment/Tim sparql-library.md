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
