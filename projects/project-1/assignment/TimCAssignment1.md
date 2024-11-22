# Tim C Project 1: OWL Cheat Sheet

Collaborative attempt by J Bittner, Tim Coleman, and Mathilde Miroir

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

Leveraring the [OWL2 DL Direct Semantics](https://www.w3.org/TR/owl2-direct-semantics/), please provide explanations for each X<sup>NS</sup> and X<sup>NS</sup> result in the table. 

For example, to explain why `R` cannot be both asymmetric and symmetric, your explanation may take the form: 
- Suppose `R` is both symmetric and asymmetric. Then by symmetry for any x and y, if x`R`y it follows that y`R`x. However, by asymmetry it also follows that it is not the case that y`R`x. Hence, `R` cannot be both symmetric and asymmetric.
Similarly, to explain why `R` cannot be both transitive and inverse functional.

**(1) Functional and Transitive (XNS)**

Suppose `R` is both functional and transitive.
Because `R` is functional, if x`R`y and x`R`z, then y = z.
Because `R` is transitive, if x`R`y and y`R`z, then x`R`z.
Since `R` is functional, x relates to only one y. However, if `R` is also transitive, this creates a scenario where x relates to both y and z, violating the functional rule. Therefore, `R` cannot be both functional and transitive.

**(2) Inverse Functional and Transitive (XNS)**

Suppose `R` is both inverse functional and transitive.
Because `R` is inverse functional, if x`R`y and z`R`y, then x = z.
Because `R` is transitive, if x`R`y and y`R`z, then x`R`z.
Since `R` is inverse functional, z should relate to only one y. However, if `R` is also transitive, z could relate to x, creating a scenario where z relates to both x and y, violating the inverse functional rule. Therefore, `R` cannot be both inverse functional and transitive.

**(3) Transitive and Asymmetric (XNS)**

Suppose `R` is both transitive and asymmetric.
Because `R` is transitive, if x`R`y and y`R`z, then x`R`z.
Because `R` is asymmetric, if x`R`y, then it is not the case that yRx.
By transitivity, x`R`z. However, if z`R`x were to occur, asymmetry would be violated, as z cannot relate back to x. Therefore, `R` cannot be both transitive and asymmetric.

**(4) Transitive and Irreflexive (XNS)**

Suppose `R` is both transitive and irreflexive.
Because `R` is transitive, if x`R`y and y`R`z, then x`R`z.
Because `R` is irreflexive, it is not the case that x`R`x for any x.
In transitivity, x`R`y and y`R`x implies x`R`x, which directly violates irreflexivity since xRx cannot hold for any x. Therefore, `R` cannot be both transitive and irreflexive.

**(5) Symmetric and Asymmetric (XUNSAT)**

Suppose `R` is both symmetric and asymmetric.
Because `R` is symmetric, if x`R`y, then y`R`x.
Because `R` is asymmetric, if x`R`y, then it is not the case that y`R`x.
Symmetry and asymmetry are in direct conflict because symmetry requires y`R`x whenever x`R`y, while asymmetry forbids y`R`x if x`R`y. Therefore, `R` cannot be both symmetric and asymmetric.

**(6) Asymmetric and Reflexive (XUNSAT)**

Suppose `R` is both asymmetric and reflexive.
Because `R` is asymmetric, if x`R`y, then it is not the case that yRx.
Because `R` is reflexive, x`R`x for every x.
Since reflexivity requires every element to relate to itself (x`R`x), and asymmetry prohibits x`R`x, `R` cannot be both asymmetric and reflexive.

**(7) Reflexive and Irreflexive (XUNSAT)**

Suppose `R` is both reflexive and irreflexive.
Because `R` is reflexive, x`R`x for every x.
Because `R` is irreflexive, it is not the case that x`R`x for any x.
These definitions are in direct conflict since it’s impossible for x`R`x to be both true and false at the same time. Therefore, `R` cannot be both reflexive and irreflexive.

## Assignment Part 2

### Variable Constraints

- `B` owl:subPropertyOf of `A`
- `Bi` owl:subPropertyOf of `Ai`
- `Ai` is the inverse of `A`
- `Bi` is the inverse of `B`

### Table III. (A) Transitive and Irreflexive Trials 
|            | A Trans | B Trans | Ai Trans | Bi Trans |
|------------|---------|---------|----------|----------|
| **A Irr**  | N<sub>1 | N<sub>2 | N<sub>3  | N<sub>4  |
| **B Irr**  | Y<sub>5 | N<sub>6 | Y<sub>7  | N<sub>8  |
| **Ai Irr** | N<sub>9 | N<sub>10| N<sub>11 | N<sub>12 |
| **Bi Irr** | Y<sub>13| N<sub>14| Y<sub>15 | N<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_

### Table IV. (B) Transitive and Functional Trials

|             | A Trans | B Trans | Ai Trans | Bi Trans |
|-------------|---------|---------|----------|----------|
| **A  Func** | N<sub>1 | N<sub>2 | N<sub>3  | N<sub>4  |
| **B  Func** | N<sub>5 | N<sub>6 | N<sub>7  | N<sub>8  |
| **Ai Func** | Y<sub>9 | Y<sub>10| N<sub>11 | N<sub>12 |
| **Bi Func** | Y<sub>13| Y<sub>14| N<sub>15 | N<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_


### Table V. (C) Transivitive vs Inverse Functional 

|              | A Trans | B Trans | Ai Trans | Bi Trans |
|--------------|---------|---------|----------|----------|
| **A iFunc**  | N<sub>1 | N<sub>2 | Y<sub>3  | N<sub>4  |
| **B iFunc**  | N<sub>5 | N<sub>6 | Y<sub>7  | Y<sub>8  |
| **Ai iFunc** | Y<sub>9 | Y<sub>10| N<sub>11 | N<sub>12 |
| **Bi iFUnc** | Y<sub>13| Y<sub>14| N<sub>15 | N<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_

### Table VI. (D) Transitive and Asymmetric Trials  (Tim's HW)

|            | A Trans | B Trans | Ai Trans | Bi Trans |
|------------|---------|---------|----------|----------|
| **A Asym** | N<sub>1 | N<sub>2 | N<sub>3  | N<sub>4  |
| **B Asym** | N<sub>5 | N<sub>6 | N<sub>7  | N<sub>8  |
| **Ai Asym**| Y<sub>9 | Y<sub>10| N<sub>11 | N<sub>12 |
| **Bi Asym**| Y<sub>13| Y<sub>14| N<sub>15 | N<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_


### Explanations

#### (A) Transitive and Irreflexive Explanations
- (A-1) Suppose `A` is both irreflexive and transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This creates a conflict because the irreflexive property of `A` forbids any element from relating to itself (`<x,x>`), but transitivity could imply this relation when applied across a chain of relationships, which violates the irreflexive property. This contradiction makes it incompatible for OWL reasoners.

- (A-2) Suppose `A` is irreflexive and `B` is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This creates a conflict because `B` transitivity implies connections between multiple elements that may lead to reflexive relationships (`<x,x>`), which violates the irreflexivity of `A`. This contradiction makes it incompatible for OWL reasoners.

- (A-3) Suppose `A` is irreflexive and its inverse, `Ai`, is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This creates a conflict because transitivity in `Ai` can suggest reflexive connections, whereas `A` irreflexivity prevents reflexive relations (`<x,x>`), leading to a violation of the irreflexive property of `A`. This contradiction makes it incompatible for OWL reasoners.

- (A-4) Suppose `A` is irreflexive and `Bi` is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This creates a conflict because transitivity in `Bi` can lead to reflexive relationships across chains of elements, violating the irreflexivity condition of `A` that prevents `<x,x>`. This contradiction makes it incompatible for OWL reasoners.

- (A-5) Suppose `B` is irreflexive and `A` is transitive. Because `B` is irreflexive, it is not the case for any `x` that `<x,x>` is in `B`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This creates a conflict because `A`'s transitivity can result in reflexive connections between elements, which directly violates the irreflexivity requirement of `B`. This contradiction makes it incompatible for OWL reasoners.

- (A-6) Suppose `B` is both irreflexive and transitive. Because `B` is irreflexive, it is not the case for any `x` that `<x,x>` is in `B`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This creates a conflict because transitivity in `B` allows multiple relationships that could imply reflexive relationships (`<x,x>`), directly contradicting the irreflexive constraint of `B`. This contradiction makes it incompatible for OWL reasoners.

- (A-7) Suppose `B` is irreflexive and `Ai` is transitive. Because `B` is irreflexive, it is not the case for any `x` that `<x,x>` is in `B`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This creates a conflict because transitivity in `Ai` could create reflexive relationships, which would violate the irreflexive property of `B`. This contradiction makes it incompatible for OWL reasoners.

- (A-8) Suppose `B` is irreflexive and its inverse, `Bi`, is transitive. Because `B` is irreflexive, it is not the case for any `x` that `<x,x>` is in `B`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This creates a conflict because transitivity in `Bi` can imply reflexive connections, which violates the irreflexive property of `B`. This contradiction makes it incompatible for OWL reasoners.

- (A-9) Suppose `Ai` is irreflexive and its inverse, `A`, is transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This does not create a conflict because transitivity in `A` is compatible with the irreflexivity of `Ai`, allowing both properties to coexist without contradiction.

- (A-10) Suppose `Ai` is irreflexive and `B` is transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This does not create a conflict because the transitivity of `B` and the irreflexivity of `Ai` can work together without violation of constraints.

- (A-11) Suppose `Ai` is both irreflexive and transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This creates a conflict because transitivity in `Ai` implies connections that can lead to reflexive relationships (`<x,x>`), which violates the irreflexive property of `Ai`. This contradiction makes it incompatible for OWL reasoners.

- (A-12) Suppose `Ai` is irreflexive and `Bi` is transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This creates a conflict because transitivity in `Bi` can imply reflexive connections, which violates the irreflexivity condition of `Ai`. This contradiction makes it incompatible for OWL reasoners.

- (A-13) Suppose `Bi` is irreflexive and `A` is transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This does not create a conflict because the transitivity of `A` and the irreflexivity of `Bi` can work together without violation of constraints.

- (A-14) Suppose `Bi` is irreflexive and its inverse, `B`, is transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This does not create a conflict because the transitivity of `B` and the irreflexivity of `Bi` can coexist without contradiction.

- (A-15) Suppose `Bi` is irreflexive and `Ai` is transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This creates a conflict because transitivity in `Ai` implies reflexive relationships, which would violate the irreflexive property of `Bi`. This contradiction makes it incompatible for OWL reasoners.

- (A-16) Suppose `Bi` is both irreflexive and transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 
- This creates a conflict because transitivity in `Bi` could lead to reflexive connections, which directly violates the irreflexive property of `Bi`. This contradiction makes it incompatible for OWL reasoners.


#### (B) Transitive and Functional

- (B-1) Suppose `A` is both transitive and functional. Because `A` is transitive, if x`R`y and y`R`z, then x`R`z. Because `A` is functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity allows x to relate to multiple elements, but functionality restricts x to relating to only one element. This contradiction makes it incompatible for OWL reasoners.

- (B-2) Suppose `A` is transitive and `B` is functional. Because `A` is transitive, if x`R`y and y`R`z, then x`R`z. Because `B` is functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because `B` (a subclass of `A`) allows x to relate to both y and z through transitivity, but `B` restricts the relation to one element. This contradiction makes it incompatible for OWL reasoners.

- (B-3) Suppose `A` is transitive and its inverse, `Ai`, is functional. Because `A` is transitive, if x`R`y and y`R`z, then x`R`z. Because `Ai` is functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity in `A` allows multiple connections, but `Ai` functionality restricts x to only one y. This contradiction makes it incompatible for OWL reasoners.

- (B-4) Suppose `A` is transitive and `Bi` is functional. Because `A` is transitive, if x`R`y and y`R`z, then x`R`z. Because `Bi` is functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because `A` transitivity allows multiple connections, while `Bi` functionality restricts the relation to only one element. This contradiction makes it incompatible for OWL reasoners.

- (B-5) Suppose `B` is transitive and `A` is functional. Because `B` is transitive, if x`R`y and y`R`z, then x`R`z. Because `A` is functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because `B` transitivity allows for multiple connections through intermediaries, while `A` restricts the relation to one element. This contradiction makes it incompatible for OWL reasoners.

- (B-6) Suppose `B` is both transitive and functional. Because `B` is transitive, if x`R`y and y`R`z, then x`R`z. Because `B` is functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity allows x to relate to multiple elements, while functionality restricts x to one element. This contradiction makes it incompatible for OWL reasoners.

- (B-7) Suppose `B` is transitive and `Ai` is functional. Because `B` is transitive, if x`R`y and y`R`z, then x`R`z. Because `Ai` is functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity in `B` allows multiple connections, but `Ai` functionality restricts the relation to only one element. This contradiction makes it incompatible for OWL reasoners.

- (B-8) Suppose `B` is transitive and its inverse, `Bi`, is functional. Because `B` is transitive, if x`R`y and y`R`z, then x`R`z. Because `Bi` is functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because `B` transitivity allows multiple connections, while `Bi` functionality restricts x to relate to only one element. This contradiction makes it incompatible for OWL reasoners.

- (B-9) Suppose `Ai` is transitive and its inverse, `A`, is functional. Because `Ai` is transitive, if x`R`y and y`R`z, then x`R`z. Because `A` is functional, if x`R`y and x`R`z, then y=z.
- This scenario does not create a conflict because transitivity and functionality are aligned, and the restrictions on relationships are respected.

- (B-10) Suppose `Ai` is transitive and `B` is functional. Because `Ai` is transitive, if x`R`y and y`R`z, then x`R`z. Because `B` is functional, if x`R`y and x`R`z, then y=z.
- This scenario does not create a conflict because transitivity and functionality are aligned, and the restrictions on relationships are respected.

- (B-11) Suppose `Ai` is both transitive and functional. Because `Ai` is transitive, if x`R`y and y`R`z, then x`R`z. Because `Ai` is functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity allows for multiple connections between elements, while functionality restricts x to relate to only one element. This contradiction makes it incompatible for OWL reasoners.

- (B-12) Suppose `Ai` is transitive and `Bi` is functional. Because `Ai` is transitive, if x`R`y and y`R`z, then x`R`z. Because `Bi` is functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because `Ai` transitivity allows multiple connections between elements, while `Bi` functionality restricts x to relate to only one element. This contradiction makes it incompatible for OWL reasoners.

- (B-13) Suppose `Bi` is transitive and `A` is functional. Because `Bi` is transitive, if x`R`y and y`R`z, then x`R`z. Because `A` is functional, if x`R`y and x`R`z, then y=z.
- This scenario does not create a conflict because the transitivity of `Bi` and the functionality of `A` are aligned, allowing both properties to coexist.

- (B-14) Suppose `Bi` is transitive and its inverse, `B`, is functional. Because `Bi` is transitive, if x`R`y and y`R`z, then x`R`z. Because `B` is functional, if x`R`y and x`R`z, then y=z.
- This scenario does not create a conflict because the transitivity of `Bi` and the functionality of `B` operate together without violation of constraints.

#### (C) Transitive and Inverse Functional

- (A-1) Suppose `A` is transitive and its inverse, `A`, is inverse functional. Because `A` is transitive, if x`R`y and y`R`z, then x`R`z. Because `A` is inverse functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity allows x to relate to multiple elements, but inverse functionality restricts x to relating to only one element. This contradiction makes it incompatible for OWL reasoners.

- (B-2) Suppose `B` is transitive and its inverse, `A`, is inverse functional. Because `B` is transitive, if x`R`y and y`R`z, then x`R`z. Because `A` is inverse functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity in `B` allows x to relate to both y and z, but `A` inverse functional restricts the relation to one element. This contradiction makes it incompatible for OWL reasoners.

- (Ai-3) Suppose `Ai` is transitive and its inverse, `A`, is inverse functional. Because `Ai` is transitive, if x`R`y and y`R`z, then x`R`z. Because `A` is inverse functional, if x`R`y and x`R`z, then y=z.
- This scenario does not create a conflict because transitivity and inverse functionality are aligned, allowing both properties to coexist.

- (Ai-4) Suppose `Ai` is transitive and its inverse, `A`, is inverse functional. Because `Ai` is transitive, if x`R`y and y`R`z, then x`R`z. Because `A` is inverse functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity in `Ai` creates multiple connections through intermediaries, but `A` inverse functional restricts x to relate to only one element. This contradiction makes it incompatible for OWL reasoners.

- (A-5) Suppose `A` is transitive and its inverse, `B`, is inverse functional. Because `A` is transitive, if x`R`y and y`R`z, then x`R`z. Because `B` is inverse functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity in `A` allows multiple connections through intermediaries, but `B` inverse functional restricts y to only one relationship. This contradiction makes it incompatible for OWL reasoners.

- (B-6) Suppose `B` is transitive and its inverse, `B`, is inverse functional. Because `B` is transitive, if x`R`y and y`R`z, then x`R`z. Because `B` is inverse functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity in `B` allows multiple relationships between x, y, and z, while `B` inverse functional restricts x to only one relation. This contradiction makes it incompatible for OWL reasoners.

- (Ai-7) Suppose `Ai` is transitive and its inverse, `B`, is inverse functional. Because `Ai` is transitive, if x`R`y and y`R`z, then x`R`z. Because `B` is inverse functional, if x`R`y and x`R`z, then y=z.
- This scenario does not create a conflict because transitivity and inverse functionality are aligned, allowing both properties to coexist.

- (B-8) Suppose `B` is transitive and its inverse, `Bi`, is inverse functional. Because `B` is transitive, if x`R`y and y`R`z, then x`R`z. Because `Bi` is inverse functional, if x`R`y and x`R`z, then y=z.
- This scenario does not create a conflict because transitivity and inverse functionality are aligned, allowing both properties to coexist.

- (Ai-9) Suppose `Ai` is transitive and its inverse, `A`, is inverse functional. Because `Ai` is transitive, if x`R`y and y`R`z, then x`R`z. Because `A` is inverse functional, if x`R`y and x`R`z, then y=z.
- This scenario does not create a conflict because transitivity and inverse functionality are aligned, allowing both properties to coexist.

- (Bi-10) Suppose `Bi` is transitive and its inverse, `A`, is inverse functional. Because `Bi` is transitive, if x`R`y and y`R`z, then x`R`z. Because `A` is inverse functional, if x`R`y and x`R`z, then y=z.
- This scenario does not create a conflict because transitivity and inverse functionality are aligned, allowing both properties to coexist.

- (Ai-11) Suppose `Ai` is transitive and its inverse, `Ai`, is inverse functional. Because `Ai` is transitive, if x`R`y and y`R`z, then x`R`z. Because `Ai` is inverse functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity in `Ai` allows multiple connections through intermediaries, while `Ai` inverse functionality restricts these relationships. This contradiction makes it incompatible for OWL reasoners.

- (Ai-12) Suppose `Ai` is transitive and its inverse, `Bi`, is inverse functional. Because `Ai` is transitive, if x`R`y and y`R`z, then x`R`z. Because `Bi` is inverse functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity in `Ai` allows x to relate to multiple elements through intermediaries, whereas `Bi` inverse functional restricts relationships to one element. This contradiction makes it incompatible for OWL reasoners.

- (Bi-13) Suppose `Bi` is transitive and its inverse, `A`, is inverse functional. Because `Bi` is transitive, if x`R`y and y`R`z, then x`R`z. Because `A` is inverse functional, if x`R`y and x`R`z, then y=z.
- This scenario does not create a conflict because transitivity and inverse functionality are aligned, allowing both properties to coexist.

- (Bi-14) Suppose `Bi` is transitive and its inverse, `B`, is inverse functional. Because `Bi` is transitive, if x`R`y and y`R`z, then x`R`z. Because `B` is inverse functional, if x`R`y and x`R`z, then y=z.
- This scenario does not create a conflict because transitivity and inverse functionality are aligned, allowing both properties to coexist.

- (Bi-15) Suppose `Bi` is transitive and its inverse, `Ai`, is inverse functional. Because `Bi` is transitive, if x`R`y and y`R`z, then x`R`z. Because `Ai` is inverse functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity in `Bi` allows multiple relationships, while `Ai` inverse functional restricts each y to only one relationship with x. This contradiction makes it incompatible for OWL reasoners.

- (Bi-16) Suppose `Bi` is transitive and its inverse, `Bi`, is inverse functional. Because `Bi` is transitive, if x`R`y and y`R`z, then x`R`z. Because `Bi` is inverse functional, if x`R`y and x`R`z, then y=z.
- This creates a conflict because transitivity in `Bi` allows multiple connections between elements, whereas `Bi` inverse functionality restricts relationships to only one connection. This contradiction makes it incompatible for OWL reasoners.



#### (D) Transitive and Asymmetric

- (D-1) Suppose `A` is both transitive and asymmetric. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `A` is asymmetric, if xRy, then it is not the case that yRx.
- This creates a conflict because `A` is asymmetric, meaning if `xRy`, then `yRx` must not hold. Since `A` is transitive, this implies that `x` could relate to multiple elements, which violates the asymmetric constraint of `A`. This contradiction makes it incompatible for OWL reasoners.

- (D-2) Suppose `A` is transitive and `B` is asymmetric. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `B` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict since `B` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold. However, asymmetry can’t hold because asymmetry prevents the case that `yRx`. This contradiction makes it incompatible for OWL reasoners.

- (D-3) Suppose `A` is transitive and its inverse, `Ai`, is asymmetric. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Ai` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict because `Ai` is asymmetric, meaning if `xRy`, then `yRx` must not hold. Since `A` is transitive, this implies that `x` could relate to multiple elements, which violates the asymmetric constraint of `Ai`. This contradiction makes it incompatible for OWL reasoners.

- (D-4) Suppose `A` is transitive and `Bi` is asymmetric. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Bi` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict since `Bi` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold, but asymmetry can’t hold as asymmetry prevents the case that `yRx`. Since `xRy`, then `yRx` cannot hold because asymmetry prevents reciprocal relations. This contradiction makes it incompatible for OWL reasoners.

- (D-5) Suppose `B` is transitive and `A` is asymmetric. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `A` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict because `A` is asymmetric, meaning if `xRy`, then `yRx` must not hold. Since `B` is transitive, this implies that `x` could relate to multiple elements, which violates the asymmetric constraint of `A`. This contradiction makes it incompatible for OWL reasoners.

- (D-6) Suppose `B` is both transitive and asymmetric. Because `B` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `B` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict because `B` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold, but asymmetry can’t hold as asymmetry prevents the case that `yRx`. This contradiction makes it incompatible for OWL reasoners.

- (D-7) Suppose `B` is transitive and `Ai` is asymmetric. Because `B` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Ai` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict since `Ai` is asymmetric, meaning if `xRy`, then `yRx` must not hold. Since `B` is transitive, this implies that `x` could relate to multiple elements, which violates the asymmetric constraint of `Ai`. This contradiction makes it incompatible for OWL reasoners.

- (D-8) Suppose `B` is transitive and its inverse, `Bi`, is asymmetric. Because `B` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Bi` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict since `Bi` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold, but asymmetry can’t hold as asymmetry prevents the case that `yRx`. This contradiction makes it incompatible for OWL reasoners.

- (D-9) Suppose `Ai` is transitive and its inverse, `A`, is asymmetric. Because `Ai` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `A` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict because `A` is asymmetric, meaning if `xRy`, then `yRx` must not hold. Since `Ai` is transitive, this implies that `x` could relate to multiple elements, which violates the asymmetric constraint of `A`. This contradiction makes it incompatible for OWL reasoners.

- (D-10) Suppose `Ai` is transitive and `B` is asymmetric. Because `Ai` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `B` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict since `B` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold, but asymmetry can’t hold as asymmetry prevents the case that `yRx`. This contradiction makes it incompatible for OWL reasoners.

- (D-11) Suppose `Ai` is both transitive and asymmetric. Because `Ai` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Ai` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict because `Ai` is asymmetric, meaning if `xRy`, then `yRx` must not hold. Since `Ai` is transitive, this implies that `x` could relate to multiple elements, which violates the asymmetric constraint of `Ai`. This contradiction makes it incompatible for OWL reasoners.

- (D-12) Suppose `Ai` is transitive and `Bi` is asymmetric. Because `Ai` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Bi` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict since `Bi` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold, but asymmetry can’t hold as asymmetry prevents the case that `yRx`. This contradiction makes it incompatible for OWL reasoners.

- (D-13) Suppose `Bi` is transitive and `A` is asymmetric. Because `Bi` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `A` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict because `A` is asymmetric, meaning if `xRy`, then `yRx` must not hold. Since `Bi` is transitive, this implies that `x` could relate to multiple elements, which violates the asymmetric constraint of `A`. This contradiction makes it incompatible for OWL reasoners.

- (D-14) Suppose `Bi` is transitive and its inverse, `B`, is asymmetric. Because `Bi` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `B` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict because `B` is asymmetric, meaning if `xRy`, then `yRx` must not hold. Since `Bi` is transitive, this implies that `x` could relate to multiple elements, which violates the asymmetric constraint of `B`. This contradiction makes it incompatible for OWL reasoners.

- (D-15) Suppose `Bi` is transitive and `Ai` is asymmetric. Because `Bi` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Ai` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict because `Ai` is asymmetric, meaning if `xRy`, then `yRx` must not hold. Since `Bi` is transitive, this implies that `x` could relate to multiple elements, which violates the asymmetric constraint of `Ai`. This contradiction makes it incompatible for OWL reasoners.

- (D-16) Suppose `Bi` is both transitive and asymmetric. Because `Bi` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Bi` is asymmetric, if xRy, then it is not the case that yRx.  
- This creates a conflict because `Bi` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold, but asymmetry can’t hold as asymmetry prevents the case that `yRx`. This contradiction makes it incompatible for OWL reasoners.
