### NOTES FOR ASSIGNMENT

PLEASE NOTE: this is a complilation of 42 problems/pitfalls identified by a preexisting software (OOPS) whose tools are behind a paywall. The paper attached, includes diagrams displaying the code patterns used to identify some of these pitfalls. PLEASE confirm that pitfall solution explored has not been defined by another tool/reasoner listed in the paper (e.g. XD-Tools, Moki, Onto-check, reasoner and/or specific test cases - TABLE III)

OOPS () for sale
https://www.igi-global.com/article/oops-ontology-pitfall-scanner/116450


https://oa.upm.es/35873/1/INVE_MEM_2014_192872.pdf (site for all pitfalls defined by OOPS)

P1, P9, P14, P15, P15, P16, P17, P18, P23 have not been addressed by the OOPS tool.


::: mermaid        
classDiagram
    Pitfalls -- Critical 
    Pitfalls -- Important 
    Pitfalls -- Minor
    Pitfalls: identified by OOPS

    class Critical{
      P01. Creating Polysemous Elements
      P03. Creating the Relationship “is” Instead of Using “rdfs:subClassOf”, “rdf:type” or “owl:sameAs”
      P05. Defining Wrong Inverse Relationships
      P06. Including Cycles in the Hierarchy
      P14. Misusing “owl:allValuesFrom”
      P15. Misusing “not some” and “some not”
      P16. Misusing Primitive and Defined Classes
      P19. Swapping Intersection and Union
      P27. Defining Wrong Equivalent Relationships
      P28. Defining Wrong Symmetric Relationships
      P29. Defining Wrong Transitive Relationships
      P31. Defining Wrong Equivalent Classes
      P37. Ontology Not Available
      P39. Ambiguous Namespace
      P40. Namespace Hijacking
    }
    class Important{
      P10. Missing Disjointness
      P11. Missing Domain or Range in Properties
      P12. Missing Equivalent Properties
      P17. Specializing a Hierarchy Exceedingly
      P18. Specifying the Domain or the Range Exceedingly
      P23. Using Incorrectly Ontology Elements
      P24. Using Recursive Definition
      P25. Defining a Relationship Inverse to Itself
      P26. Defining Inverse Relationships for a Symmetric One
      P30. Missing Equivalent Classes
      P34. Untyped Class
      P35. Untyped Property
      P38. No OWLOntology Declaration
    }
    class Minor{
      P02. Creating Synonyms as Classes
      P04. Creating Unconnected Ontology Elements
      P07. Merging Different Concepts in the Same Class
      P08. Missing Annotations
      P09. Missing Basic Information
      P13. Missing Inverse Relationships
      P20. Misusing Ontology Annotations
      P21. Using a Miscellaneous Class
      P22. Using Different Naming Criteria in the Ontology
      P32. Several Classes with the Same Label
      P33. Creating a Property Chain with Just One Property
      P36. URI Contains File Extension
    }
:::



P01. Creating Polysemous Elements: An ontology element whose name has different meanings is included in the ontology to represent more than one conceptual idea. For example, the class “Theatre” is used  to represent both the artistic discipline and the place in which a play is performed.

- P02. Creating Synonyms as Classes: Several classes whose identifiers are synonyms are created and defined as equivalent. For example, the classes “Waterfall” and “Cascade” are defined as equivalents. This pitfall is related to the guidelines presented in Noy, and McGuinness (2001), which explain that synonyms for the same concept do not represent different classes.

- P03. Creating the Relationship “is” Instead of Using “rdfs:subClassOf”, “rdf:type” or “owl:sameAs”: The “is” relationship is created in the ontology instead of using OWL primitives for representing the subclass relationship (“subclassOf”), the membership to a class (“instanceOf”), or the equality between instances (“sameAs”). An example of this pitfall is to define the class “Actor” in the  following way ‘Actor ≡ Person ⨅ ∃inter- prets.Actuation ⨅ ∃is.Man’. This pitfall is related to the guidelines for understanding the “is-a” relation provided in Noy, and McGuinness (2001).

- P04. Creating Unconnected Ontology Elements: Ontology elements (classes, relationships or attributes) are created with no relation to the rest of the ontology. An  example of this type of pitfall is to create  the relationship “memberOfTeam” and to miss the class representing teams; thus, the relationship created is isolated in the ontology.

- P05. Defining Wrong Inverse Relationships: Two relationships are defined as inverse relations when they are not necessarily inverse. An example of this type of pitfall is to define “isSoldIn” and “isBoughtIn” as inverse relationships.

- P06. Including Cycles in the Hierarchy (Gómez-Pérez, 2004; Noy, & McGuin- ness, 2001): A cycle between two classes in the hierarchy is included in the ontology even though the ontology is not intended to have such classes as equivalent. That is, some class A has a subclass B, and at the same time B is a superclass of A. An example of this type of pitfall is represented by the class “Professor” as subclass of “Person”, and the class “Person” as subclass of “Professor”.

- P07. Merging Different Concepts in the Same Class: A class whose identifier refers to two or more different concepts is cre- ated. An example of this type of pitfall is the creation of the class “StyleAndPeriod”.

- P08. Missing Annotations: Ontology terms lack annotations properties such as rdfs:label or rdfs:comment. An example of this type of pitfall is to create a class and to fail to provide human readable annotations attached to such a class.

- P09. Missing Basic Information: Some of the information needed is not included in the ontology. This pitfall may be related to the requirements in the ontology requirements specification document (ORSD) not covered by the ontology, or to knowledge that can be added to the ontology to make it more complete. An example of this type of pitfall is to create the relationship “startsIn” in order to represent that the routes have a starting point in a particular location and to miss the relationship “endsIn” in order to represent that a route has an end point.

- P10. Missing Disjointness (Gómez- Pérez, 2004; Noy, & McGuinness, 2001; Rector et al., 2004): The ontology lacks disjoint axioms between classes or between properties that should be defined as disjoint. For example, we can create the classes “Odd” and “Even” (or the classes “Prime” and “Composite”) without being disjoint; such representation is incomplete with regard to the definition of these types of numbers.

- P11. Missing Domain or Range in Properties: Relationships and/or attributes without domain or range (or none of them) are included in the ontology. An example of this type of pitfall is to create the relationship “hasWritten”, with no domain nor range specification, in an ontology about art in which the relationship domain should be “Writer” and the relationship range should be “LiteraryWork”. This pitfall is related to the common error that appears when defining the ranges and domains described in Rector et al. (2004).

- P12. Missing Equivalent Properties: When an ontology is imported into another, classes duplicated in both ontologies are normally defined as equivalent classes. However, the ontology developer misses the definition of equivalent properties in the cases of duplicated relationships and attri- butes. An example of this type of pitfalls is to fail to define the relations “hasMember” and “has-Member” as equivalent.

- P13. Missing Inverse Relationships: This pitfall appears when any relationship (ex- cept for the symmetric ones) does not have an inverse relationship defined within the ontology. For example, the case in which the ontology developer omits the inverse definition between the relations “hasLanguageCode” and “isCodeOf”.

- P14. Misusing “owl:allValuesFrom” (Rector et al., 2004): This pitfall can appear in two different ways. Firstly, when the universal restriction (“allValuesFrom”) is used as the default qualifier instead of the existential restriction (“someValuesFrom”). Secondly, when “allValuesFrom” is included to close off the possibility of further additions for a given property. An example of this type of pitfall is to define the class “Book” in the following way ‘Book ≡ ∃producedBy.Writer ⨅ ∀uses.Paper’ thus closing the possibility of adding “Ink” as an element used in the writing.

- P15. Misusing “not some” and “some not” (Rector et al., 2004): The pitfall here is to confuse the representation of “some not” with “not some”. An example of this type of pitfall is to define a vegetarian pizza as any pizza which has both some topping which is not meat and some topping which is not fish. This example is explained in more detail in Rector et al. (2004).

- P16. Misusing Primitive and Defined Classes (Rector et al., 2004): This pitfall implies failing to make the definition ‘complete’ rather than ‘partial’ (or ‘necessary and sufficient’ rather than just ‘necessary). It is critical to understand that, in general, nothing will be inferred to be subsumed under a primitive class by the classifier (Rector et al., 2004). This pitfall implies that the developer does not understand the open world assumption. An example of this pitfall is to create the primitive class ‘CheesyPizza ⊏ Pizza ⨅ ∃hasTopping. Cheese’ instead of creating it as a defined class in the following way: ‘CheesyPizza ≡ Pizza ⨅ ∃hasTopping.Cheese’. This example is explained in more detail in Rector et al. (2004).

- P17. Specializing a Hierarchy Exceedingly: The hierarchy in the ontology is specialized in such a way that the final leaves cannot have instances since they are actually instances and should have been created as such instead of as classes. Authors in Noy, and McGuinness (2001) provide guidelines for distinguishing between a class and an instance when modeling hierarchies. An example of this type of pitfall is to create the classes “Madrid”, “Barcelona” and “Sevilla”, among others, as subclasses of “Place”.

- P18. Specifying the Domain or the Range Exceedingly (Noy, & McGuinness, 2001; Rector et al., 2004): This pitfall means failing to find a domain or a range general enough. An example of this type of pitfall is to restrict the domain of the relationship “isOfficialLanguage” to the class “City”, instead of allowing the class “Country” or a more general concept such as “GeopoliticalObject” to have an official language.

- P19. Swapping Intersection and Union: The ranges and/or domains of the properties (relationships and attributes) are defined by intersecting several classes in cases in which the ranges and/or domains should be the union of those classes. This pitfall is related both to the common error that appears when defining ranges and domains described in Rector et al. (2004) and to the guidelines for defining these elements provided in Noy, and McGuinness (2001). An example of this type of pitfall is to create the relationship “takesPlaceIn” with one range declaration for the class “City” and other range declaration for the class “Nation”, as this implementation represents the intersection of both ranges instead of the union.

- P20. Misusing Ontology Annotations: The contents of some annotation properties are swapped or misused. An example of this type of pitfall is to include in the rdfs:label annotation of the class “Crossroads” the following sentence ’the place of intersection of two or more roads’; and to include in the rdfs:comment annotation the word ‘Crossroads’.

- P21. Using a Miscellaneous Class: This means creating in a hierarchy a class containing the instances that do not belong to the sibling classes instead of classifying such instances as instances of the class in the upper level of the hierarchy. An example of this type of pitfall is to create the class “HydrographicalResource”, and the subclasses “Stream” and “Waterfall”, among others, and also the subclass “OtherRiverElement”.

- P22. Using Different Naming Criteria in the Ontology: Ontology elements are not named following the same convention within the whole ontology. Some notions about naming conventions are provided in Noy, and McGuinness (2001). For example, this pitfall appears when a class identifier starts with upper case, e.g. “Ingredient”, whereas its subclass identifiers start with lower case, e.g. “flour” and “milk”.

- P23. Using Incorrectly Ontology Elements: An ontology element (class, relationship or attribute) is used to model a part of the ontology that should be modeled with a different element. A particular case of this pitfall regarding the misuse of classes and property values is addressed in Noy, and McGuinness (2001). An example of this type of pitfall is to create the relationship “isEcological” between an instance of “Car” and the instances “Yes” or “No”, instead of creating an attribute “isEcological” whose range is Boolean.

- P24. Using Recursive Definition: An ontology element is used in its own definition. An example of this type of pitfall is to create the relationship “hasFork” and to establish as its range the following: The set of restaurants that have at least one value for the relationship “hasFork”.

- P25. Defining a Relationship Inverse to Itself: A relationship is defined as inverse of itself. In this case, this property could have been defined as “owl:SymmetricProperty” instead. An example of this type of pitfall is to create the relationship “hasBorderWith” and to state that “hasBorderWith” is its inverse relationship.

- P26. Defining Inverse Relationships for a Symmetric One: A relationship is defined as “owl:SymmetricProperty”, and such a relationship is defined as inverse of another relationship. For example, to create for the symmetric relationship “farFrom” an inverse relationship, e.g. itself, “farFrom”.

- P27. Defining Wrong Equivalent Relationships: Two relationships are defined as equivalent relations when they are not necessarily equivalent. An example of this type of pitfalls is to mix up common relationships that could hold between several types of entities, as “hasPart” defined in one ontology between human body parts and the relation “hasPart” defined in another ontology between research plans and research projects.

- P28. Defining Wrong Symmetric Relationships: A relationship is defined as symmetric when the relationship is not necessarily symmetric. This situation can appear because the domain and range are too specific; for example, if we define the symmetric relationship “hasSpouse” between the concepts “Man” and “Woman” instead of using the concept “Person” both as domain and range of such a relationship.

- P29. Defining Wrong Transitive Relationships: A relationship is defined as transitive when the relationship is not necessarily transitive. An example of this type of pitfall is to create the relationship “participatesIn”, whose domain is the union of the concepts “Team” and “Individual” and whose range is the concept “Event”, and defining the relationship as transitive.

- P30. Missing Equivalent Classes: When an ontology is imported into another, classes with the same conceptual meaning that are duplicated in both ontologies should be defined as equivalent classes in order to benefit the interoperability between both ontologies. However, the ontology developer may miss the definition of equivalent classes in the cases of duplicated concepts. An example of this pitfall is to fail to define the classes ‘Trainer’ (class in an imported ontology) and ‘Coach’ (class in the ontology about sports being developed) as equivalent classes.

- P31. Defining Wrong Equivalent Classes: Two classes are defined as equivalent when they are not necessarily equivalent. For example, defining “Car” as equivalent to “Vehicle”.

- P32. Several Classes with the Same Label: Two or more classes have the same content in the rdfs:label annotation. For example, to link the label “Theatre” both with the building and the literary discipline, adding no more labels to them.

- P33. Creating a Property Chain with Just One Property: There is a property chain that includes only one property in the antecedent part. For example, to create the following property chain: isInChargeOf -> supervises.

- P34. Untyped Class (Hogan et al., 2010): A resource is used as a class without having been declared as a Class. An example of this type of pitfall is to create individu- als of the class “Person” and to omit that “Person” is a class.

- P35. Untyped Property (Hogan et al., 2010): A resource is used as a property with- out having been declared as a rdf:Property or as some subclass of it. An example of this type of pitfall is to link individual by the relation “hasPart” and to omit that “hasPart” is an object property.

- P36. URI Contains File Extension (Archer, Goedertier, & Loutas, 2012): This involves including file extensions as “.owl”, “.rdf”, “.ttl”, “.n3” and “.rdfxml” in an ontology URI. An example of this pitfall is to define an ontology uri as “http://www. biopax.org/release/biopax-level3.owl” containing the extension “.owl” related to the technology used.

- P37. Ontology Not Available: This involves omitting to provide online description or documentation of the ontology when looking up its URI. An example of this pitfall could be the following case: “Ontology Security (ontosec)” (URI: http://www.semanticweb.org/ontologies/2008/11/OntologySecurity.owl) which is not available online as RDF nor as HTML (at the moment of carrying out this work).

- P38. No OWLOntology Declaration: This means failing to declare the owl:Ontology tag where the ontology metadata should be provided. An example of this pitfall could be found at the “Creative Commons Rights Expression Language (cc)” ontology (URI: http://creativecommons.org/ ns) that does not have any owl:Ontology declaration in its RDF file even though it has other OWL elements used as, for example, owl:equivalentProperty (at the moment of carrying out this work).

- P39. Ambiguous Namespace: This means failing to define both the ontology URI and the xml:base namespace. An example of this pitfall could be found at “Basic Access Control ontology (acl)” (URI: http://www.w3.org/ns/auth/acl) that has no owl:Ontology tag nor xml:base definition.

- P40. Namespace Hijacking (Heath, & Bizer, 2011): This means reusing or referring to terms from other namespaces not actually defined in such namespace. This pitfall is related to the Linked Data publishing guidelines provided in Heath, and Bizer (2011): “Only define new terms in a namespace that you control.” An example of this pitfall is to use “http://www.w3.org/2000/01/rdf-schema#Property” that is not defined in the rdf namespace (http://www.w3.org/2000/01/rdf-schema#) instead of using “http://www.w3.org/1999/02/22-rdf-syntax-ns#Property”, that is actually defined in the rdfs namespace (http://www.w3.org/1999/02/22-rdf-syntax-ns#).


# Process workflow for this assignment

#### insert flowchart here when complete
