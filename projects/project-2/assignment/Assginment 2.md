<header>
  <h1>Project 2: The SPARQL Library of Common Core Ontologies</h1>
</header>

1. Detecting Cycles in the Hierarchy: This query can help identify problematic cyclic subclass relationships in an ontology, which often signal modeling errors or unintended structures. 
(level 6 - 3 pts)

<pre>
  <code>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?classA ?classB
WHERE {
  ?classA rdfs:subClassOf+ ?classB .
  ?classB rdfs:subClassOf+ ?classA .
  FILTER(?classA != ?classB)  # Exclude trivial cycles where classA and classB are the same
}
</code>
</pre>


2. Detecting missing labels: This version splits the `rdfs:label` and `rdfs:comment` checks into two separate sections, each with its own `FILTER` and `BIND` statements,
 making it clear whether a term is missing a label or a comment. (level 4 - 10 pts)

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?term ?missingAnnotation
WHERE {
    {
        # Find all terms missing rdfs:label
        {
            ?term a rdfs:Class .
        }
        UNION
        {
            ?term a rdf:Property .
        }
        UNION
        {
            ?term a owl:NamedIndividual .
        }
        
        FILTER NOT EXISTS { ?term rdfs:label ?label . }
        BIND("Missing rdfs:label" AS ?missingAnnotation)
    }
    UNION
    {
        # Find all terms missing rdfs:comment
        {
            ?term a rdfs:Class .
        }
        UNION
        {
            ?term a rdf:Property .
        }
        UNION
        {
            ?term a owl:NamedIndividual .
        }

        FILTER NOT EXISTS { ?term rdfs:comment ?comment . }
        BIND("Missing rdfs:comment" AS ?missingAnnotation)
    }
}
</code>
</pre>


3. Check the misuse of the universal restriction (“allValuesFrom”) when it is used as the default qualifier instead of the existential restriction (“someValuesFrom”).
It identifies instances where `owl:allValuesFrom` is potentially misapplied as a default qualifier instead of using `owl:someValuesFrom` (Level 5 - 5 pts)

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

SELECT ?property ?class ?restriction
WHERE {
    # Find properties with universal restrictions
    ?property a owl:ObjectProperty .
    ?restriction a owl:Restriction ;
                 owl:onProperty ?property ;
                 owl:allValuesFrom ?class .
    
    # Check for absence of existential restrictions on the same property
    FILTER NOT EXISTS {
        ?property a owl:ObjectProperty .
        ?existentialRestriction a owl:Restriction ;
                                owl:onProperty ?property ;
                                owl:someValuesFrom ?class .
    }
}
    
  </code>
</pre>


4. Misusing primitive and defined classes: detecting the failure to make the definition ‘complete’ rather than ‘partial.’ In other words,
   finding definitions that are ‘necessary and sufficient’ rather than just ‘necessary'. (Level 3 - 20 pts)

<pre>
  <code>
    PREFIX : <http://example.org/ontology/>

SELECT ?definition ?necessaryCondition
WHERE {
    ?definition a :Definition ;
                :necessaryCondition ?necessaryCondition .
    
    FILTER NOT EXISTS {
        ?definition :sufficientCondition ?sufficientCondition .
    }
}

  </code>
</pre>


5. detects definitions of relationships that are defined as inverse of another relationship when the two relationships are `owl:SymmetricProperty`.
   For example, detecting the creation of the symmetric relationship “farFrom” an inverse relationship, e.g. itself, “farFrom”. (Level 5 - 5 pts)

<pre>
  <code>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?property ?inverseProperty
WHERE {
    # Find properties that are declared symmetric
    ?property a owl:SymmetricProperty .
    
    # Check if the property is defined as the inverse of itself or another property
    ?property owl:inverseOf ?inverseProperty .
    
    # Check if the inverse property is the same as the symmetric property itself or also symmetric
    FILTER (?property = ?inverseProperty || EXISTS { ?inverseProperty a owl:SymmetricProperty })
}
    
  </code>
</pre>

6. Detect Classes Without a Subclass (Leaf Classes). This query detects classes that do not have any subclasses.
   These "leaf" classes might be indicators of incomplete modeling if too many are present. (level 3 - 20 pts)

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?class
WHERE {
    ?class a rdfs:Class .
    
    # Find classes that do not have any subclasses
    FILTER NOT EXISTS {
        ?subClass rdfs:subClassOf ?class .
    }
} 
  </code>
</pre>



7. Detect Properties with Conflicting Domain and Range: This query checks for properties that are used with instances whose types conflict with the
   property's declared domain and range, which could result in incorrect or inconsistent usage of the properties. (level 3 20 pts)

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?property ?subject ?object
WHERE {
    ?property a rdf:Property ;
              rdfs:domain ?domain ;
              rdfs:range ?range .
    
    ?subject rdf:type ?subjectClass .
    ?subject ?property ?object .
    ?object rdf:type ?objectClass .

    # Check if the subject and object are not conforming to the domain and range
    FILTER(?subjectClass != ?domain || ?objectClass != ?range)
}

  </code>
</pre>

8. Detect Classes without Subclasses or Instances: This query identifies classes that neither have subclasses nor instances,
   which might indicate unused or improperly modeled classes. (level 2 - 25 pts)

<pre>
  <code>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?class
WHERE {
    ?class a rdfs:Class .
    
    # Check for missing subclasses
    FILTER NOT EXISTS {
        ?subclass rdfs:subClassOf ?class .
    }
    
    # Check for missing instances
    FILTER NOT EXISTS {
        ?instance rdf:type ?class .
    }
}
  </code>
</pre>
    


9. Detect Classes Without `owl:disjointWith` Declarations: This query checks for classes that do not have an `owl:disjointWith` declaration,
    which helps ensure logical separation between classes. (level 8)

<pre>
  <code>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?classA
WHERE {
    ?classA a rdfs:Class .
    
    # Check if the class lacks an owl:disjointWith declaration
    FILTER NOT EXISTS {
        ?classA owl:disjointWith ?classB .
    }
}

  </code>
</pre>
