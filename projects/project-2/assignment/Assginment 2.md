<header>
  <h1>Project 2: The SPARQL Library of Common Core Ontologies</h1>
</header>

1. Detecting Cycles in the Hierarchy: This query can help identify problematic cyclic subclass relationships in an ontology, which often signal modeling errors or unintended structures. 
(level 6 - 3 pts)

Severity level: Error

The potential consequences of the issues the query identifies: A cyclic subclass relationship means that `?classA` is a subclass of `?classB` and vice versa. This relationship implies that the two classes are mutually dependent and essentially indistinguishable in terms of their scope, which creates ambiguity.


<pre>
  <code>
PREFIX rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt;

SELECT ?classA ?classB (IF(BOUND(?classA), "Cyclic subclass relationship detected", "No cycles detected") AS ?message)
WHERE {
  ?classA rdfs:subClassOf+ ?classB .
  ?classB rdfs:subClassOf+ ?classA .
  FILTER(?classA != ?classB)  # Exclude trivial cycles where classA and classB are the same
}
</code>
</pre>


2. Detecting missing labels: This version splits the `rdfs:label` and `rdfs:comment` checks into two separate sections, each with its own `FILTER` and `BIND` statements,
 making it clear whether a term is missing a label or a comment. (level 4 - 10 pts)

Severity warning: Warning

The potential consequences of the issues the query identifies: The absence of `rdfs:label` and `rdfs:comment` makes the ontology less user-friendly, reduces its potential for reuse, integration, and automated processing, and increases the likelihood of misinterpretation.


<pre>
  <code>
PREFIX rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;
PREFIX rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt;
PREFIX owl: &lt;http://www.w3.org/2002/07/owl#&gt;

SELECT ?term ?missingLabel ?missingComment
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
        FILTER isIRI(?term)  # Exclude blank nodes
        BIND("Missing label" AS ?missingLabel)
        BIND("" AS ?missingComment)  # Ensure this field is empty when no comment issue is present
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
        FILTER isIRI(?term)  # Exclude blank nodes
        BIND("Missing comment" AS ?missingComment)
        BIND("" AS ?missingLabel)  # Ensure this field is empty when no label issue is present
    }
}
</code>
</pre>


3. Check the misuse of the universal restriction (“allValuesFrom”) when it is used as the default qualifier instead of the existential restriction (“someValuesFrom”).
It identifies instances where `owl:allValuesFrom` is potentially misapplied as a default qualifier instead of using `owl:someValuesFrom` (Level 5 - 5 pts)

Severity warning: Error

The potential consequences of the issues the query identifies: A reasoner will not infer that there must be instances of the property, leading to incomplete or incorrect inferences.


<pre>
  <code>
PREFIX rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;
PREFIX rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt;
PREFIX owl: &lt;http://www.w3.org/2002/07/owl#&gt;

SELECT ?property ?class ?restriction
WHERE {
    # Find object properties with universal restrictions
    ?property a owl:ObjectProperty .
    
    # Find restrictions with allValuesFrom on the property and a class
    ?restriction a owl:Restriction ;
                 owl:onProperty ?property ;
                 owl:allValuesFrom ?class .
    
    # Ensure there is no corresponding someValuesFrom restriction on the same property and class
    FILTER NOT EXISTS {
        ?existentialRestriction a owl:Restriction ;
                                owl:onProperty ?property ;
                                owl:someValuesFrom ?class .  # Same class is important
    }

    # Exclude blank nodes for restrictions if necessary
    FILTER isIRI(?restriction)
}
  </code>
</pre>


4. Misusing primitive and defined classes: detecting the failure to make the definition ‘complete’ rather than ‘partial.’ In other words,
   finding definitions that are ‘necessary and sufficient’ rather than just ‘necessary'. (Level 3 - 20 pts)

   Severity warning: Error

The potential consequences of the issues the query identifies: Definitions in an ontology typically require both necessary and sufficient conditions to fully describe the scope and boundaries of a concept. A missing sufficient condition means that the definition is incomplete, leaving ambiguity in how the concept should be interpreted or applied.
This could lead to misinterpretations of the concept, as users might not understand under what circumstances an entity fully belongs to the class or concept being defined.


<pre>
  <code>
  PREFIX : &lt;http://example.org/ontology/&gt;

SELECT ?definition ?necessaryCondition
WHERE {
    ?definition a :Definition ;
                :necessaryCondition ?necessaryCondition .
    
    FILTER NOT EXISTS {
        ?definition :sufficientCondition ?sufficientCondition .
    }

    # Filter definitions with a specific pattern in their URI (e.g., definitions for specific domain terms)
    FILTER REGEX(STR(?definition), "^http://example.org/ontology/domainA", "i")
}
  </code>
</pre>


5. detects definitions of relationships that are defined as inverse of another relationship when the two relationships are `owl:SymmetricProperty`.
   For example, detecting the creation of the symmetric relationship “farFrom” an inverse relationship, e.g. itself, “farFrom”. (Level 5 - 5 pts)

   Severity warning: Warning

The potential consequences of the issues the query identifies: Symmetric properties, by definition, do not need to be explicitly declared as their own inverse because the symmetry already implies that P(x, y) is equivalent to P(y, x). Declaring the property as its own inverse adds unnecessary complexity and clutter to the ontology.
This can make the ontology more difficult to read, understand, and maintain, especially for human users who might be confused by seemingly redundant statements.



<pre>
  <code>
PREFIX owl: &lt;http://www.w3.org/2002/07/owl#&gt;
PREFIX rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;
PREFIX rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt;

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

   Severity warning: Warning

The potential consequences of the issues the query identifies: The query identifies classes that do not have any subclasses. While this is not necessarily an error, it can indicate potential issues in the ontology’s design and completeness. 

Improved: adding additional logic to filter for classes that not only lack subclasses but also:
Do not have instances.
Do not have labels or comments, which can indicate documentation gaps.
Check if the class is disjoint with any other classes.
Check if the class is involved in any property restrictions (e.g., owl:allValuesFrom or owl:someValuesFrom).
Include optional matching on specific patterns in class URIs using REGEX for further complexity.


<pre>
  <code>
PREFIX rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;
PREFIX rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt;
PREFIX owl: &lt;http://www.w3.org/2002/07/owl#&gt;

SELECT ?class (COUNT(DISTINCT ?subClass) AS ?subClassCount) (COUNT(DISTINCT ?instance) AS ?instanceCount)
       (SAMPLE(?label) AS ?label) (SAMPLE(?comment) AS ?comment) (SAMPLE(?restriction) AS ?restriction)
WHERE {
    # Find all classes
    ?class a rdfs:Class .
    
    # Find classes that do not have any subclasses
    FILTER NOT EXISTS {
        ?subClass rdfs:subClassOf ?class .
    }

    # Count instances of the class (if any)
    OPTIONAL {
        ?instance a ?class .
    }

    # Find classes that are missing labels
    OPTIONAL {
        ?class rdfs:label ?label .
    }
    FILTER (!BOUND(?label))  # Only select classes without labels
    
    # Find classes that are missing comments
    OPTIONAL {
        ?class rdfs:comment ?comment .
    }
    FILTER (!BOUND(?comment))  # Only select classes without comments

    # Check if the class is involved in any property restrictions (e.g., owl:allValuesFrom or owl:someValuesFrom)
    OPTIONAL {
        ?restriction a owl:Restriction ;
                     owl:onProperty ?property ;
                     (owl:allValuesFrom | owl:someValuesFrom) ?class .
    }

    # Check if the class is disjoint with any other class
    OPTIONAL {
        ?class owl:disjointWith ?disjointClass .
    }

    # Filter to match specific patterns in class URIs (e.g., classes with 'ontology' in the URI)
    FILTER REGEX(STR(?class), "ontology", "i")
}
GROUP BY ?class
HAVING (?subClassCount = 0 && ?instanceCount = 0)

  </code>
</pre>



7. Detect Properties with Conflicting Domain and Range: This query checks for properties that are used with instances whose types conflict with the
   property's declared domain and range, which could result in incorrect or inconsistent usage of the properties. (level 3 20 pts)

   Severity warning: Warning

The potential consequences of the issues the query identifies: The query identifies domain and range mismatches between properties and the actual types of the subject and object, and checks for subproperty relationships, subclass hierarchies, and property restrictions. 

Improved: Subproperty handling adds complexity by considering property hierarchies.
Class hierarchy checks allow for more flexible reasoning about domain and range.
Property restrictions introduce deeper reasoning into the validation of subject and object types.
Inverse properties provide additional semantic richness for more complex relationship patterns.
REGEX filtering narrows the scope of properties based on URI patterns, adding specificity to the query.


<pre>
  <code>
PREFIX rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;
PREFIX rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt;
PREFIX owl: &lt;http://www.w3.org/2002/07/owl#&gt;

SELECT ?property ?subject ?object ?domain ?range ?subjectClass ?objectClass ?subProperty
WHERE {
    # Find properties with declared domain and range
    ?property a rdf:Property ;
              rdfs:domain ?domain ;
              rdfs:range ?range .
    
    # Optional: find subproperties
    OPTIONAL {
        ?subProperty rdfs:subPropertyOf ?property .
    }

    # Match instances with the property
    ?subject rdf:type ?subjectClass .
    ?subject ?property ?object .
    ?object rdf:type ?objectClass .
    
    # Check for mismatches between subject/object classes and the domain/range
    FILTER (?subjectClass != ?domain || ?objectClass != ?range)
    
    # Check if subject belongs to a subclass of the domain
    OPTIONAL {
        ?subjectClass rdfs:subClassOf ?domain .
    }
    
    # Check if object belongs to a subclass of the range
    OPTIONAL {
        ?objectClass rdfs:subClassOf ?range .
    }
    
    # Check for property restrictions involving owl:allValuesFrom or owl:someValuesFrom
    OPTIONAL {
        ?restriction a owl:Restriction ;
                     owl:onProperty ?property ;
                     (owl:allValuesFrom | owl:someValuesFrom) ?restrictionClass .
    }

    # Additional filter to identify specific properties based on their URI patterns
    FILTER REGEX(STR(?property), "http://example.org/properties/", "i")
    
    # Optional check for inverse properties (inverse relationships)
    OPTIONAL {
        ?property owl:inverseOf ?inverseProperty .
        ?object ?inverseProperty ?subject .
    }
}
GROUP BY ?property ?subject ?object ?domain ?range ?subjectClass ?objectClass ?subProperty

  </code>
</pre>

8.  identifies datatype properties that do not have any rdfs:range defined, and also checks if they are used in any triples. (Level 2 - 25 pts)

Severity warning: Warning

The potential consequences of the issues the query identifies: The query identifies datatype properties that do not have an rdfs:range defined and are not used in any triples. The issues found in this query can lead to several potential consequences, mostly related to incomplete modeling, ambiguous data, and underutilization of properties. 



<pre>
  <code>
PREFIX rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;
PREFIX rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt;
PREFIX owl: &lt;http://www.w3.org/2002/07/owl#&gt;

SELECT ?property
WHERE {
    ?property a owl:DatatypeProperty .
    
    # Check if the property has no range
    FILTER NOT EXISTS {
        ?property rdfs:range ?range .
    }
    
    # Check if the property is used in any triples
    FILTER NOT EXISTS {
        ?subject ?property ?literal .
    }
}

  </code>
</pre>
    


9. Detect Classes Without `owl:disjointWith` Declarations: This query checks for classes that do not have an `owl:disjointWith` declaration,
    which helps ensure logical separation between classes. (level 8)

   Severity warning: Warning

The potential consequences of the issues the query identifies: The query identifies classes that lack owl:disjointWith declarations, which means the ontology does not explicitly declare that these classes are mutually exclusive. While this does not immediately break the ontology, it can lead to several potential consequences that may affect the clarity, reasoning, and data integrity of the ontology. 


<pre>
  <code>
PREFIX owl: &lt;http://www.w3.org/2002/07/owl#&gt;
PREFIX rdfs: &lt;http://www.w3.org/2000/01/rdf-schema#&gt;

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
