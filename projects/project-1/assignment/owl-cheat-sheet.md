# Project 1: OWL Cheat Sheet

The goal of this project is to complete OWL documentation concerning logical combinations of role constraints over object properties. It includes two sub-assignments: (1) Providing OWL 2 direct semantics-based explanations for unsatisfiability and inconsistency results stemming from role constraint pairs; (2) Providing OWL 2 direct semantics-based explanations for results stemming from role constraint combinations under the owl:subPropertyOf relationship.

I will remind you that my goal in this exercise is to produce a publishable paper on this topic by the end of the project; I aim to include anyone on the paper as an author who completes the project. The content of this paper will be a great benefit to the ontology engineering community, so it is important to have this work presented to the broader public sooner rather than later. 

## Assignment Part 1

### OWL2 DL Direct Semantics Role Constraints

[OWL2 DL Direct Semantics](https://www.w3.org/TR/owl2-direct-semantics/) allows for constraints on object properties of the following sort, where `R` is an arbitrary object property:

| **Constraint**         | **Definition**                                             | **Example** |
|------------------------|------------------------------------------------------------|-------------|
| **Functional**          | If xRy and xRz, then y=z                                   | If x *has birthdate* y and x *has birthdate* z, then y=z. |
| **Inverse Functional**  | If xRy and zRy, then x=z                                   | If x *has social security number* y and z *has social security number* y, then x=z. |
| **Transitive**          | If xRy and yRz, then xRz                                   | If x *is contained in* y and y *is contained in* z, then x *is contained in* z. |
| **Symmetric**           | If xRy, then yRx                                           | If x *is a friend of* y, then y *is a friend of* x. |
| **Asymmetric**          | If xRy, then it is not the case that yRx                   | If x *is the parent of* y, then it is not the case that y *is the parent of* x. |
| **Reflexive**           | xRx                                                        | x *is as tall as* itself. |
| **Irreflexive**         | It is not the case that xRx                                | No x *is taller than* itself. |

### Role Constraint Combinations

These role constraints may be combined in some cases, but not others. The following table illustrates when combinations of two role constraints are permitted and when they are not. If they are not permitted, then it is either because the combination is unsatisfiable (**X<sup>UNSAT</sup>**) or because the combination creates an object property chain (**X<sup>NS</sup>**) that may lead to undecidability. The table was validated using the OWL2 reasoners Fact++, Pellet, and HermiT:

|        | Funct. | iFunct. | Trans. | Symm. | Asymm. | Ref. | Irref. |
|--------|--------|---------|--------|-------|--------|------|--------|
| **Funct.**   | -      | OK      | X<sup>NS</sup>    | OK    | OK     | OK   | OK     |
| **iFunct.**  | OK     | -       | X<sup>NS</sup>    | OK    | OK     | OK   | OK     |
| **Trans.**   | X<sup>NS</sup>    | X<sup>NS</sup>     | -      | OK    | X<sup>NS</sup>    | OK   | X<sup>NS</sup>    |
| **Symm.**    | OK     | OK      | OK     | -     | X<sup>UNSAT</sup> | OK   | OK     |
| **Asymm.**   | OK     | OK      | X<sup>NS</sup>    | X<sup>UNSAT</sup>| -      | X<sup>UNSAT</sup>| OK    |
| **Ref.**     | OK     | OK      | OK     | OK    | X<sup>UNSAT</sup> | -    | X<sup>UNSAT</sup> |
| **Irref.**   | OK     | OK      | X<sup>NS</sup>    | OK    | OK     | X<sup>UNSAT</sup>| -      |

For example, asserting `R` is both asymmetric and symmetric will result in an unsatisfiable combination, since such a combination is straightforwardly inconsistent. 
Similarly, given an object property `R`, it is possible to assert that `R` is both Functional and Inverse Functional. However, asserting `R` is both Inverse Functional and Transitive will result in an object property chain that may lead to undecidability. 

Some heuristics emerging from the table:
- Transitivity can only be combined usefully with symmetry or reflexivity.
- Asymmetry can only be combined usefully with functionality, inverse functionality, and irreflexivity.
- Reflexivity cannot be combined usefully with asymmetry.
- Irreflexivity cannot be combined usefully with transitivity.

### Assignment Part 1 Details

Leveraging the [OWL2 DL Direct Semantics](https://www.w3.org/TR/owl2-direct-semantics/), please provide explanations for each X<sup>NS</sup> and X<sup>NS</sup> result in the table. 

For example, to explain why `R` cannot be both asymmetric and symmetric, your explanation may take the form: 
- Suppose `R` is both symmetric and asymmetric. Then by symmetry for any x and y, if x`R`y it follows that y`R`x. However, by asymmetry it also follows that it is not the case that y`R`x. Hence, `R` cannot be both symmetric and asymmetric.
Similarly, to explain why `R` cannot be both transitive and inverse functional, your explanation may take the form:

## Assignment Part 2

Let us focus now on combinations of role constraints that do not result in inconsistency or undecidability. Moreover, let us focus on combinations of role constraints spread across parent-child object property relationships. To illustrate, suppose `B` is an owl:subPropertyOf `A`, `Ai` is the inverse of `A`, and `Bi` is the inverse of `B`. Keep in mind that: 
- For any object properties `A`, `B`: if `B` owl:subPropertyOf `A` then for any  `<x,y>` in `B` that `<x,y>` is also in `A`
- For any object properties `R`, `Ri`: if `R` inverse of `Ri` then for any `<x,y>` in `R` then `<y,x>` in `Ri`

|            |**Trans**|                |                |                |
|------------|----------------|----------------|----------------|----------------|
|**Irr**| **A** | **Ai** | **B** | **Bi** |
| **A**      | X     | X      | X    | X     |
| **Ai**     | X     | X      | X    | X     |
| **B**      | OK     | OK      | X     | X      |
| **Bi**     | OK     | OK      | X     | X      |


For the cells with "X", where irreflexivity and transitivity were applied to the same object property, OWL reasoners throw errors or ignore role constraints. For example, the above "X" combinations resulted in Fact++ and HermiT generating internal errors, while Pellet ignored the transitivity constraint but kept the irreflexivity constraint.

Suppose `B` owl:subPropertyOf of `A`, `A` is irreflexive and `B` is transitive. This corresponds to the first row of letters and and the third column of values, which in this case is "X". Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `B` owl:subPropertyOf of `A`, it follows that if `<x,y>` and `<y,z>`, in then `<x,z>` is in `A` as well. The result of such chaining and checking whether `<x,x>` is in `A` is however forbidden in many OWL 2 reasoners, as it involves a non-simple property exhibiting an irreflexive role constraint. 
 
### Assignment Part 2 Details

For this part of the assignment, I would like you to explore combinations of role contraints under owl:subPropertyOf, creating tables of the sort described above. I understand this will be a cumbersome, potentially time-consuming undertaking, so I will make it a bit easier by _allowing you to work in teams_ and divide the labor among yourselves. There must, however, be at least two teams participating in the project. 

As you are working through combinations of object properties and role constraints, I would additionally like you to leveraring the [OWL2 DL Direct Semantics](https://www.w3.org/TR/owl2-direct-semantics/), to provide explanations for each "X" cell you encounter in the tables you construct. I woould also like you to leverage OWL reasoners that come euipped in the [Protege](https://protege.stanford.edu/) ontology editor to check your work. I'll note too that in Protege, when you encounter an inconsistency, internal error, etc. when attempting to run a reasoner to check these cells, you'll learn quite a bit by exploring the debug messages that populate. They are full of information explaining why the reasoner ran into trouble. 
