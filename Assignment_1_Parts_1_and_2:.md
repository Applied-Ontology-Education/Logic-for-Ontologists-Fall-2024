Assignment Part One: Object-Property Pair contradictions.

"PROVIDE OWL-2 DIRECT SEMANTIC BASED EXPLANATIONS
FOR UNSATISFIABILITY AND INCONSISTENCY RESULTS
STEMMING FROM ROLE CONSTRAINT PAIRS."


COMBINATIONS WHICH RESULT ARE UNDECIDEABLE:
These combinations become undecideable because it is impossible to achieve a yes/no answer. 
Example: Halting Problem.


1.) FUNCTIONAL COMBINED WITH TRANSITIVE 

-According to functional object property, if xRy and xRz then y = z 

-By transitive, if xRy, yRz, then xRz where x,y and z are distinct.

-xRy and xRz cannot hold simultaneously because this violates cardinality of functional object properties. 
Therefore, this expression becomes undecideable because it can be satisfied by more than one value. 



2.) INVERSE-FUNCTIONALITY AND TRANSITIVITY

-By inverse object property, if xRy and zRy then x = z. 

-By transitive, if zRx and xRy then zRy, where x,y and z are distinct.

-zRy and xRy cannot hold simultaneously because only one instance can relate to y by virtue of cardinality. 
Therefore this expression becomes undecideable because it can be satisfied by more than one value. 



3.) A-SYMMETRY + TRANSITIVITY = UNDECIDEABLE

-By asymmetry if xRy then ~(yRx)

-By transitive, if xRy, yRz, and zRx then yRx.

-yRx and ~(yRx) cannot hold at once. 



4.) TRANSITIVE + IRREFLEXIVE = UNDECIDEABLE

-By irreflexive, ~(xRx).

-By transitive, if xRy and yRx then xRx. 

-Since some symmetrical statements paired with a transitive expression become reflexive,
this violates the conditions of irreflexive object property. 




COMBINATIONS WHICH ARE UNSATISFIABLE: 
These combinations become unsatisfiable because no value exists such that it will yield as true for the equation. 


1.) SYMMETRY + ASYMMETRY 

-By Symmetry, if xRy then yRx

-By Asymmetry, if xRy, then ~(yRx)

-These statements will always contradict each other. 




2.) ASYMMETRY + REFLEXIVE

-By Reflexive, xRx.

-By Asymmetry, for all x ~(xRx)

-A Reflexive statement is inherently symmetric to itself which violates asymmetry. 




3.) REFLEXIVE + IRREFLEXIVE = UNSATISFIABLE

-By reflexive, xRx

-By irreflexive, ~(xRx)

-These statements cannot together will result in a contradiction. 


END OF PART 1.





PART 2: 

SUB-PROPERTY COMBINATIONS:

AXIOM: for [B] object_subProperty of [A], any {x,y} pair of instances in B will occur in [A].
AXIOM: For any object properties R, Ri: if R inverse of Ri then for any {x,y} in R then {y,x} in Ri

Consider combinations across object properties and their sub-properties and whether they violate the logical conditions of one another.

Categories:
 [A] is parent property
 [B] is sub-property of [A]
 [Ai] is the inverse of [A]
 [Bi] is the inverse of [B] AND subproperty of [Ai]



DERIVED HEURISTICS:


Functional Object Property pairs fine with all other object properties besides Transitive Object Property.

--This is because the transitive property may produce a chain that will break the cardinality restriction (1) of functional object properties.
By Functional, if (xRy) and (xRz) then (y = z). By Transitive if (xRy) and (yRb) then (xRb). (xRb) where b does not equal y or z violates cardinality of the relation.
However, it is the case that when [B] or [Bi] is functional and [A] or [Ai] is transitive the relation will hold. This is because the child, functional, conditonals of [B] or [Bi] do NOT violate the transitive conditions of its parent property, [A] / [Ai].



Inverse Functional Object Property pairs fine with all other object properties besides Transitive Object Property.

--This is because the transitive property may produce a chain that will break the cardinality restriction (1) of inverse functional object properties.
By inverse functional, if (xRy) and (zRy) then (x = z). By transitive, if (xRy) and (qRx) then (qRy). (qRy) violates the cardinality restriction of the relation. 
However, it is the case that when [B] or [Bi] is inverse functional and [A] or [Ai] is transitive the relation will hold. This is because the child, inverse functional, conditonals of [B] or [Bi] do NOT violate the transitive conditions of its parent property, [A] / [Ai].



Symmetric Object Property pairs fine with all other object properties besides Asymmetric.

--For an Asymmetric object property if (aRb) then ~(bRa). By Symmetry if (aRb) then (bRa). (bRa) and ~(bRa) cannot hold at once. This is the case anytime where [A] or [Ai] is Asymmetric as well as if [B] or [Bi] is paired with Asymmetric and Symmetric properties at once. However, when [A] or [Ai] is Symmetric and [B] and or [Bi] is asymmetric there not a contradiction. This is because the conditions of asymmetry will not violate those of its parent symmetric parent property. Rather, it is symmetry which violates asymmetry.



Reflexive Object Property pairs fine with Functional, Inverse Functional, Symmetric, and Transitive properties. Irreflexive and Asymmetric pairings lead to violations. 

--Irreflexive object property and Reflexive property lead to violations because Reflexive holds for all (x), xRx while Irreflexive holds ~(xRx) which is a direct contradiction. However, where [A] or [Ai] is Reflexive and [B] or [Bi] is Irreflexive, the relation will hold. This is because the irreflexive conditions of the subproperty or its inverse will not violate the reflexive condtions of its parent. Rather it is the conditions of relexivity that violate irreflexivity in all other cases. 
--Reflexive and Asymmetric object property combinations lead to violations. Example: by reflexive, xRx, by Asymmetry for all (x) ~(xRx). (xRx) and ~(xRx) result in a contradiction. However, when [B] or [Bi] is Asymmetric and [A] or [Ai] is Reflexive, the relation will hold this is because here asymmetry does not violate the reflexive conditons of its parent property. Asymmetry and Reflexive expressions can never hold at once nor when the parent property is Asymmetric. 
 


Asymmetric Object Property pairs fine with Functional, Inverse Functional, and Irreflexive properties. Pairings with Symmetric, Reflexive and Transitive properties lead to violations.

--Symmtric property violations have already been explained.
--Reflexive property violations have already been explained. 
--Asymmetric object property paired with a transitive object property leads to violation because a transitive chain could result in a symmetric expression which would violate asymmetry. For example, by asymmetry is (xRy) then ~(yRx). By transitive, if (yRz) and (zRx) then (yRx). (yRx) and ~(yRx) is a contradiction. However, when [A] or [Ai] is transitive and its subproperty [B] or inverse [Bi] is Asymmetric, the relation holds. This is because asymmetry does not violate the conditons of the parent object property which is transitive. 




Irreflexive Object Property pairs fine with Functional, Inverse-Functional, Symmetric, Asymmetric properties. Pairing with a Reflexive or Transitive property leads to violations.

--Irreflexive paired with Reflexive property has already been explained. 
--Irreflexive property paired with a Transitive object property leads to violations because a transitive chain can cause a reflexive expression which violates irreflexivity. For example, by irreflexivity for all (x) ~(xRx). By transitive, if (xRy) and (yRx) then (xRx). (xRx) and ~(xRx) cannot hold at once. However when the parent object property or its inverse is transitive and its subproperty or inverse is irreflexive the relation holds. This is because the irreflexive conditions of the child do NOT violate the transitive conditions of its parent or parent inverse. 









SUPPORTING EVIDENCE OF ALL PAIRINGS IN QUESTION:



COMBINATIONS BETWEEN FUNCTIONAL AND INVERSE FUNCTIONAL OBJECT PROPERTY EXPRESSIONS:

[A] as Functional AND Inverse Functional: No issues detected.
[A] as Functional (+) [B] as Inverse Functional: No issues detected. 
[A] as Functional (+) [Ai] as Inverse Functional: No issues detected.
[A] as Functional (+) [Bi] as Inverse Functional: No issues detected.

[B] as Functional (+) [A] as Inverse Functional: No issues detected.
[B] as Functional AND Inverse Functional: No issues detected.
[B] as Functional (+) [Ai] as Inverse Functional: No issues detected. 
[B] as Functional (+) [Bi] as Inverse Functional: No issues detected.

[Ai] as Functional (+) [A] as Inverse Functional: No issues detected.
[Ai] as Functional (+) [B] as Inverse Functional: No issues detected.
[Ai] as Functional AND Inverse Functional: No issues detected.
[Ai] as Functional (+) [Bi] as Inverse Functional: No issues detected. 

[Bi] as Functional (+) [A] as Inverse Functional: No issues detected.
[Bi] as Functional (+) [B] as Inverse Functional: No issues detected.
[Bi] as Functional (+) [Ai] as Inverse Functional: No issues detected.
[Bi] as Functional AND Inverse Functional: No issues detected. 


COMBINATIONS OF FUNCTIONAL AND 

    SYMMETRIC Object Property Expressions: No issues detected.

    ASYMMETRIC Object Property Expressions: No issues detected.

    REFLEXIVE Object Property Expressions: No issues detected. 

    IRREFLEXIVE Object Property Expressions: No issues detected.


COMBINATIONS BETWEEN FUNCTIONAL AND TRANSITIVE OBJECT PROPERTY EXPRESSIONS:

[A] as Functional AND Transitive: Non-simple property 'A' or its inverse appears in the cardinality restriction 'A max 1 Thing'
[A] as Functional and [Ai] as Transitive: Non-simple property 'A' or its inverse appears in the cardinality restriction 'A max 1 Thing'
[A] as Functional and [B] as Transitive: Non-simple property 'A' or its inverse appears in the cardinality restriction 'A max 1 Thing'
[A] as Functional and [Bi] as Transitive: Non-simple property 'A' or its inverse appears in the cardinality restriction 'A max 1 Thing'

[B] as Functionl and [A] as Transitive: Non-simple property 'B' or its inverse appears in the cardinality restriction 'B max 1 Thing'
[B] as Functional AND Transitive:  Non-simple property 'B' or its inverse appears in the cardinality restrict
[B] as Functional and [Ai] as Transitive: No issues detected.
[B] as Functionla and [Bi] as Transitive: Non-simple property 'B' or its inverse appears in the cardinality restriction 'B max 1 Thing'

[Ai] as Functional and [A] as Transitive: Non-simple property 'Ai' or its inverse appears in the cardinality restriction 'Ai max 1 Thing'
[Ai] as Functional AND Transitive: Non-simple property 'Ai' or its inverse appears in the cardinality restriction 'Ai max 1 Thing'
[Ai] as Functional and [B] as Transitive: Non-simple property 'Ai' or its inverse appears in the cardinality restriction 'Ai max 1 Thing'
[Ai] as Functional and [Bi] as Transitive: Non-simple property 'Ai' or its inverse appears in the cardinality restriction 'Ai max 1 Thing'

[Bi] as Functional and [A] as Transitive: No issues detected.
[Bi] as Functional and [Ai] as Transitive: No issues detected.
[Bi] as Functional and [B] as Transitive: Non-simple property 'Bi' or its inverse appears in the cardinality restriction 'Bi max 1 Thing'
[Bi] as Functional AND Transitive: Non-simple property 'Bi' or its inverse appears in the cardinality restriction 'Bi max 1 Thing'






COMBINATIONS OF INVERSE FUNCTIONAL 

    SYMMETRIC Object Properties: No issues detected.

    ASYMMETRIC Object Properties: No issues detected.

    REFLEXIVE Object Properties: No issues detected. 

    IRREFLEXIVE Object Properties: No issues detected.

    FUNCTIONAL Object Properties: No issues detected.

Combinations between Inverse Functional and Transitive Object Properties:

[A] as Inverse Functional AND Transitive: Non-simple property ' inverse (A)' or its inverse appears in the cardinality restriction ' inverse (A) max 1 Thing'
[A] as Inverse Functional and [Ai] as Transitive: Non-simple property ' inverse (A)' or its inverse appears in the cardinality restriction ' inverse (A) max 1 Thing'
[A] as Inverse Functional and [B] as Transitive: Non-simple property ' inverse (A)' or its inverse appears in the cardinality restriction ' inverse (A) max 1 Thing'
[A] as Inverse Functional and [Bi] as Transitive: Non-simple property ' inverse (A)' or its inverse appears in the cardinality restriction ' inverse (A) max 1 Thing'

[Ai] as Inverse Functional and [A] as Transitive: Non-simple property ' inverse (Ai)' or its inverse appears in the cardinality restriction ' inverse (Ai) max 1 Thing'
[Ai] as Inverse Functional AND Transitive: Non-simple property ' inverse (Ai)' or its inverse appears in the cardinality restriction ' inverse (Ai) max 1 Thing'
[Ai] as Inverse Functional and [B] as Transitive: Non-simple property ' inverse (Ai)' or its inverse appears in the cardinality restriction ' inverse (Ai) max 1 Thing'
[Ai] as Inverse Functional and [Bi] as Transitive: Non-simple property ' inverse (Ai)' or its inverse appears in the cardinality restriction ' inverse (Ai) max 1 Thing'

[B] as Inverse Functional and [A] as Transitive: No issues detected.
[B] as Inverse Functional and [Ai] as Transitive: No issues detected.
[B] as Inverse Functional AND Transitive: Non-simple property ' inverse (B)' or its inverse appears in the cardinality restriction ' inverse (B) max 1 Thing'
[B] as Inverse Functional and [Bi] as Transitive: Non-simple property ' inverse (B)' or its inverse appears in the cardinality restriction ' inverse (B) max 1 Thing'






COMBINATIONS OF SYMMETRIC AND 

    FUNCTIONAL Object Properties: No issues detected.

    INVERSE FUNCTIONAL Object Properties: No Issues detected. 

    REFLEXIVE Object Properties: No issues detected. 

    IRREFLEXIVE Object Properties: No issues detected.

    TRANSITIVE Object Properties: No issues detected.

COMBINATIONS OF SYMMETRIC AND ASYMMETRIC OBJECT PROPERTIES: 

[A] as BOTH Symetric AND Asymmetric: Reasoner runs, however, inconsistencies are inferred.
[A] as Symmetric and [Ai] as Asymmetric: Reasoner runs, however, inconsistencies are inferred.
[A] as Symmetric and [B] as Asymmetric: No issues detected.
[A] as Symmetric and [Bi] as Asymmetric: No issues detected. 

[Ai] as BOTH Symetric AND Asymmetric: Reasoner runs, however, inconsistencies are inferred.
[Ai] as Symmetric and [A] as Asymmetric: Reasoner runs, however, inconsistencies are inferred.
[Ai] as Symmetric and [B] as Asymmetric: No issues detected.
[Ai] as Symmetric and [Bi] as Asymmetric: No issues detected. 

[B] as Symmetric and [A] as Asymmetric: Reasoner runs, however, inconsistencies are inferred.
[B] as Symmetric and [Ai] as Asymmetric: Reasoner runs, however, inconsistencies are inferred.
[B] as BOTH Symmetric and Asymmetric: Reasoner runs, however, inconsistencies are inferred.
[B] as Symmetric and [Bi] as Asymmetric: Reasoner runs, however, inconsistencies are inferred.

[Bi] as Symmetric with all other as Asymmetric same results as [B] Symmetric






COMBINATIONS OF ASYMMETRIC AND 

    FUNCTIONAL Object Properties: No issues detected.

    INVERSE FUNCTIONAL Object Properties: No issues detected.

    IRREFLEXIVE Object Properties: No issues detected.

COMBINATIONS OF ASYMMETRIC AND REFLEXIVE OBJECT PROPERTIES: 

[A] as Asymmetric AND Reflexive: Ontology becomes inconsistent
[A] as Asymmetric and [Ai] as Reflexive: Ontology becomes inconsistent.
[A] as Asymmetric and [B] as Reflexive: Ontology becomes inconsistent.
[A] as Asymmetric and [Bi] as Reflexive: Ontology becomes inconsistent. 

IBID as above where all variations of [Ai] is Asymmetric

[B] as Asymmetric and [A] as Reflexive: No issues detected.
[B] as Asymmetric and [Ai] as Reflexive: No issues detected.
[B] as Asymmetric AND Reflexive: Ontology becomes inconsistent.
[B] as Asymmetric and [Bi] as Reflexive: Ontology becomes inconsistent.

[Bi] as Asymmetric and [A] as Reflexive: No issues detected.
[Bi] as Asymmetric and [Ai] as Reflexive: No issues detected.
[Bi] as Asymmetric and [B] as Reflexive: Ontology becomes inconsistent.
[Bi] as Asymmetric AND Reflexive: Ontology becomes inconsistent.


COMBINATIONS OF ASYMMETRIC AND REFLEXIVE OBJECT PROPERTIES: 

[A] as BOTH Asymmetric AND Reflexive: Ontology becomes inconsistent.
[A] as Asymmetric and [Ai] as Reflexive: Ontology becomes inconsistent.
[A] as Asymmetric and [B] as Reflexive: Ontology becomes inconsistent.
[A] as Asymmetric and [Bi] as Reflexive: Ontology becomes inconsistent.

Ibid results as above where [Ai] is Asymmetric paired with Reflexive for all others.

[B] as Asymmetric and [A] as Reflexive: No issues detected.
[B] as Asymmetric and [Ai] as Reflexive: No issues detected.
[B] as BOTH Asymmetric AND Reflexive: Ontology becomes inconsistent.
[B] as Asymmetric and [Bi] as Reflexive: Ontology becomes inconsistent. 

Ibid results as above where [Bi] is Asymmetric paired with Reflexive for all others.


COMBINATIONS OF ASYMMETRIC AND TRANSITIVE PROPERTIES:

[A] as Asymmetric and Transitive: Non-simple property 'A' or its inverse appears in asymmetric object property axiom.
[A] as Asymmetric and [Ai] as Transitive: Non-simple property 'Ai' or its inverse appears in asymmetric object property axiom.
[A] as Asymmetric and [B] as Transitive: Non-simple property 'A' or its inverse appears in asymmetric object property axiom.
[A] as Asymmetric and [Bi] as Transitive: Non-simple property 'A' or its inverse appears in asymmetric object property axiom.

Same results where [Ai] is Asymmetric and all others are Transitive

[B] as Asymmetric and [A] Transitive: No issues detected.
[B] as Asymmetric and [Ai] Transitive: No issues detected.
[B] as BOTH Asymmetric AND TRANSITIVE: Non-simple property 'B' or its inverse appears in asymmetric object property axiom.
[B] as Asymmetric and [Bi] as Transitive: Non-simple property 'B' or its inverse appears in asymmetric object property axiom.

Same results as above where [Bi] is Asymmetric and all others are Transitive. 





COMBINATIONS OF IRREFLEXIVE AND REFLEXIVE OBJECT PROPERTIES: 

[A] as BOTH Irreflexive AND Reflexive: Ontology becomes inconsistent.
[A] as Irreflexive and [Ai] as Reflexive: Ontology becomes inconsistent.
[A] as Irreflexive and [B] as Reflexive: Ontology becomes inconsistent.
[A] as Irreflexive and [Bi] as Reflexive: Ontology becomes inconsistent.

IBID FOR ALL VARIATIONS WHERE [Ai] is Irreflexive and paired with Reflexive.

[B] as Irreflexive and [A] as Reflexive: No issues detected.
[B] as Irreflexive and [Ai] as Reflexive: No issues detected.
[B] as BOTH Irreflexive AND Reflexive: Ontology becomes inconsistent.
[B] as Irreflexive and [Bi] as Reflexive: Ontology becomes inconsistent. 

ALL VARIATIONS FOR [Bi] as Irreflexive paired with Reflexive HAVE SAME OUTCOMES AS ABOVE.


COMBINATION OF IRREFLEXIVE AND TRANSITIVE OBJECT PROPERTIES:

[A] as BOTH Irreflexive and Transitive: Non-simple property 'A' or its inverse appears in irreflexive object property axiom
[A] as Irreflexive and [Ai] as Transitive: Non-simple property 'A' or its inverse appears in irreflexive object property axiom.
[A] as Irreflexive and [B] as Transitive: Non-simple property 'A' or its inverse appears in irreflexive object property axiom.
[A] as Irreflexive and [Bi] as Transitive:  Non-simple property 'A' or its inverse appears in irreflexive object property axiom.

VARIATIONS of [Ai] as Irreflexive and paired with Transitive HAVE SAME OUTCOMES AS ABOVE.

[B] as Irreflexive and [A] as Transitive: No issues detected.
[B] as Irreflexive and [Ai] as Transitive: No issues detected.
[B] as BOTH Irreflexive AND Transitive: Non-simple property 'B' or its inverse appears in irreflexive object property axiom.
[B] as Irreflexive and [Bi] as Transitive: Non-simple property 'B' or its inverse appears in irreflexive object property axiom.

[Bi] as Irreflexive and [A] as Transitive: No issues detected.
[Bi] as Irreflexive and [Ai] as Transitive: No issues detected.
[Bi] as Irreflexive and [B] as Transitive: Non-simple property 'Bi' or its inverse appears in irreflexive object property axiom.
[Bi] as BOTH Irreflexive AND Transitive: Non-simple property 'Bi' or its inverse appears in irreflexive object property axiom.







    


