# Tim C Project 1: OWL Cheat Sheet

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
Since `R` is functional, x relates to only one y. However, if `R` is also transitive, this creates a scenario where x relates to both y and z, violating the functional rule. Therefore, 'R' cannot be both functional and transitive.

**(2) Inverse Functional and Transitive (XNS)**

Suppose 'R' is both inverse functional and transitive.
Because 'R' is inverse functional, if x'R'y and z'R'y, then x = z.
Because 'R' is transitive, if x'R'y and y'R'z, then x'R'z.
Since 'R' is inverse functional, z should relate to only one y. However, if 'R' is also transitive, z could relate to x, creating a scenario where z relates to both x and y, violating the inverse functional rule. Therefore, 'R' cannot be both inverse functional and transitive.

**(3) Transitive and Asymmetric (XNS)**

Suppose 'R' is both transitive and asymmetric.
Because 'R' is transitive, if x'R'y and y'R'z, then x'R'z.
Because 'R' is asymmetric, if x'R'y, then it is not the case that yRx.
By transitivity, x'R'z. However, if z'R'x were to occur, asymmetry would be violated, as z cannot relate back to x. Therefore, 'R' cannot be both transitive and asymmetric.

**(4) Transitive and Irreflexive (XNS)**

Suppose 'R' is both transitive and irreflexive.
Because 'R' is transitive, if x'R'y and y'R'z, then x'R'z.
Because 'R' is irreflexive, it is not the case that x'R'x for any x.
In transitivity, x'R'y and y'R'x implies x'R'x, which directly violates irreflexivity since xRx cannot hold for any x. Therefore, 'R' cannot be both transitive and irreflexive.

**(5) Symmetric and Asymmetric (XUNSAT)**

Suppose 'R' is both symmetric and asymmetric.
Because 'R' is symmetric, if x'R'y, then y'R'x.
Because 'R' is asymmetric, if x'R'y, then it is not the case that y'R'x.
Symmetry and asymmetry are in direct conflict because symmetry requires y'R'x whenever x'R'y, while asymmetry forbids y'R'x if x'R'y. Therefore, 'R' cannot be both symmetric and asymmetric.

**(6) Asymmetric and Reflexive (XUNSAT)**

Suppose 'R' is both asymmetric and reflexive.
Because 'R' is asymmetric, if x'R'y, then it is not the case that yRx.
Because 'R' is reflexive, x'R'x for every x.
Since reflexivity requires every element to relate to itself (x'R'x), and asymmetry prohibits x'R'x, 'R' cannot be both asymmetric and reflexive.

**(7) Reflexive and Irreflexive (XUNSAT)**

Suppose 'R' is both reflexive and irreflexive.
Because 'R' is reflexive, x'R'x for every x.
Because 'R' is irreflexive, it is not the case that x'R'x for any x.
These definitions are in direct conflict since it’s impossible for x'R'x to be both true and false at the same time. Therefore, 'R' cannot be both reflexive and irreflexive.

## Assignment Part 2

J Bittner, Tim Coleman & Matilde Miroir

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

### Variable Constraints

- `B` owl:subPropertyOf of `A`
- `Bi` owl:subPropertyOf of `Ai`
- `Ai` is the inverse of `A`
- `Bi` is the inverse of `B`

### Trials for Overlapping Transitive and Irreflexive Properties 
|            | A Trans | B Trans | Ai Trans | Bi Trans |
|------------|---------|---------|----------|----------|
| **A Irr**  | N<sub>1 | N<sub>2 | N<sub>3  | N<sub>4  |
| **B Irr**  | N<sub>5 | N<sub>6 | N<sub>7  | N<sub>8  |
| **Ai Irr** | N<sub>9 | N<sub>10| N<sub>11 | N<sub>12 |
| **Bi Irr** | Y<sub>13| N<sub>14| Y<sub>15 | N<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_

### [Object Property Expression Axioms](https://www.w3.org/TR/owl2-direct-semantics/)

SubObjectPropertyOf( OPE1 OPE2 )
- (OPE1)<sup>OP</sup> ⊆ (OPE2)<sup>OP</sup>

InverseObjectProperties( OPE1 OPE2 )
- (OPE1)<sup>OP</sup> = { ( x , y ) | ( y , x ) ∈ (OPE2)<sup>OP</sup> } 

IrreflexiveObjectProperty( OPE ) 
- ∀ x : x ∈ ΔI implies ( x , x ) ∉ (OPE)<sup>OP</sup>

TransitiveObjectProperty( OPE ) 
- ∀ x , y , z : ( x , y ) ∈ (OPE)<sup>OP</sup> and ( y , z ) ∈ (OPE)<sup>OP</sup> imply ( x , z ) ∈ (OPE)<sup>OP</sup>

### Trials for Overlapping Transitive and Functional Properties
|             | A Trans | B Trans | Ai Trans | Bi Trans |
|-------------|---------|---------|----------|----------|
| **A  Func** | N<sub>1 | N<sub>2 | N<sub>3  | N<sub>4  |
| **B  Func** | N<sub>5 | N<sub>6 | N<sub>7  | N<sub>8  |
| **Ai Func** | Y<sub>9 | Y<sub>10| N<sub>11 | N<sub>12 |
| **Bi Func** | Y<sub>13| Y<sub>14| N<sub>15 | N<sub>16 |

## Conflict: Functional (A) and Transitive (B)
Suppose A is functional, and B is transitive. This corresponds to the first row (A) and the third column (B) of the table, marked with "N". Since B is transitive, if <x,y> and <y,z> hold, then <x,z> must also hold due to transitivity. 

This creates a conflict since A is functional, x can only relate to a single y. Since B transitive this implies that x could relate to multiple elements (both y and z), which violates the functionality constraint of A and OWL reasoners struggle to reconcile.

## Conflict: Inverse Functional (Ai) and Transitive (B)

Suppose Ai is inverse functional and B is transitive. This corresponds to the second row (Ai) and the third column (B), marked "N". For B, if <x,y> and <y,z>, then <x,z> by transitivity. Since Ai is inverse functional, each z should relate to only one x. 

This creates a conflict because of transitivity in B, z could relate to both x and y, which violates the inverse functionality of Ai and this contradiction makes it incompatible for OWL reasoners

## Conflict: Functional (A) and Inverse Transitive (Ai)

Suppose A is functional and Ai is transitive with B owl:subPropertyOf of A. This matches the first row (A) and the second column (Ai), marked “N”. With Ai being transitive, if <x,y> and <z,y>, then <x,z>. This creates a conflict because if A is functional, then <x,y> and <x,z>, then <y=z>. 

This creates a conflit When attempting to satisfy both properties simultaneously, you run into a situation where x and z must be both equal and distinct at the same time, which is logically impossible, and this contradiction makes it incompatible for OWL reasoners.

## Conflict: Functional (A) and Inverse Transitive (Bi)

Suppose A is functional and Bi is inverse transitive with B owl:subPropertyOf of A. Suppose Bi is inverse transitive. If Bi is inverse transitive, then if xR-1y and yR-1z, inverse transitivity, it can imply xR-1z. 

This creates a conflict because if A is functional then <x,y> and <x,z>, then <y=z>. The inverse transitivity of Ai suggests that z could be different from y but still related to x, which breaks the functional constraint and makes it incompatible for OWL reasoners.

## Conflict: Inverse Functional (Ai) and Transitive (A)

Suppose Ai is inverse functional and A is transitive, where B is owl:subPropertyOf of A. This corresponds to the second row (Ai) and the first column (A) of the table marked with X. Since Ai is inverse functional, each z should relate to only one x. For A, if <x,y> and <y,z>, then <x,z> by transitivity. Transitivity relates to more things, so the OWL reasoner states it is incompatible.

## Conflict: Inverse Functional (Ai) and Inverse Transitive (Bi)

Suppose Ai is inverse functional and Bi is inverse transitive. This corresponds to the third row (Ai) and the fourth column (Bi), marked "N<sub>12</sub>". Since Ai is inverse functional, for any <x,y> and <z,y>, it must hold that <x = z>. However, because Bi is inverse transitive, if <xRy> and <yRz>, then by inverse transitivity, <xRz>.

This creates a conflict because if Ai is inverse functional, <xRy> and <zRy> should imply that <x = z>. But due to the inverse transitivity of Bi, it's possible for <x> and <z> to both relate to <y>, which contradicts the inverse functionality constraint that requires <x> and <z> to be the same. This inconsistency makes it incompatible for OWL reasoners.

## Conflict: Functional (B) and Inverse Transitive (Bi)

Suppose B is functional and Bi is inverse transitive. This corresponds to the second row (B) and the fourth column (Bi) of the table, marked with "N" (N<sub>8</sub>). If B is functional, for any x, x relates to at most one y. If Bi is inverse transitive, then if xR<sup>-1</sup>y and yR<sup>-1</sup>z, inverse transitivity implies xR<sup>-1</sup>z.

This creates a conflict because B’s functionality requires x to relate to only one y, but inverse transitivity of Bi suggests that z could relate back to x in multiple ways through different y values. This scenario breaks the "one-to-one" restriction of functionality, making it logically incompatible for OWL reasoners.

## Conflict: Inverse Functional (Bi) and Transitive (B)

Suppose Bi is inverse functional and B is transitive. This corresponds to the fourth row (Bi) and the second column (B) of the table, marked with "N" (N<sub>14</sub>). If Bi is inverse functional, for any y, y relates to at most one x. If B is transitive, then if <x,y> and <y,z> hold, then <x,z> must also hold due to transitivity.

This creates a conflict because the inverse functionality of Bi means that each y should relate to only one x, ensuring a "one-to-one" correspondence. However, B being transitive allows x to relate to multiple z values via different y values. This situation violates the inverse functionality constraint, as it implies that a single y could relate back to multiple x values through B's transitivity. This conflict makes the properties incompatible for OWL reasoners.

### Trials for Overlapping Transitive and Asymmetric Properties
|             | A Trans | B Trans | Ai Trans | Bi Trans |
|-------------|---------|---------|----------|----------|
| **A  Asym** | N<sub>1 | N<sub>2 | N<sub>3  | N<sub>4  |
| **B  Asym** | N<sub>5 | N<sub>6 | N<sub>7  | N<sub>8  |
| **Ai Asym** | Y<sub>9 | Y<sub>10| N<sub>11 | N<sub>12 |
| **Bi Asym** | Y<sub>13| Y<sub>14| N<sub>15 | N<sub>16 |

- **Conflict: Asymmetric Ai and Transitive A**  

  Suppose `Ai` is asymmetric, and `A` is transitive. This corresponds to the second row (Ai) and the second column (A) of the table, marked with "No". Since `A` is transitive, if `<x,y>` and `<y,z>` hold, then `<x,z>` must also hold due to transitivity. Since `Ai` is asymmetric, if `xRy`, then it is not the case that `yRx`.  

  This creates a conflict because `Ai` is asymmetric, meaning if `xRy`, then `yRx` must not hold. Since `A` is transitive, this implies that `x` could relate to multiple elements, which violates the asymmetric constraint of `Ai`. This contradiction makes it incompatible for OWL reasoners.

- **Conflict: Asymmetric A and Transitive Ai**  
  
  Suppose `A` is asymmetric, and `Ai` is transitive. This corresponds to the first row (A) and the third column (Ai) of the table, marked with "No". Since `A` is asymmetric, if `xRy` holds, then `yRx` cannot hold because `y` cannot be related to `x`.  

  This creates a conflict because `Ai` is transitive; if `<x,y>` and `<y,z>` hold, then `<x,z>` must also hold due to transitivity. However, asymmetry states that if `xRy`, then it is not the case that `yRx`. This contradiction makes it incompatible for OWL reasoners.

- **Conflict: Asymmetric A and Transitive B**  
  
  Suppose `A` is asymmetric, and `B` is transitive. This corresponds to the first row (A) and the fourth column (B) of the table, marked with "No". Since asymmetry holds, if `xRy`, then it is not the case that `yRx`.  
  
  This creates a conflict since `B` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold. However, asymmetry can’t hold because asymmetry prevents the case that `yRx`. This contradiction makes it incompatible for OWL reasoners.

- **Conflict: Asymmetric A and Transitive Bi**  
  
  Suppose `A` is asymmetric, and `Bi` is transitive. This corresponds to the first row (A) and the fifth column (Bi) of the table, marked with “N”. Since asymmetry holds, if `xRy`, then it is not the case that `yRx`.  
  
  This creates a conflict since `Bi` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold, but asymmetry can’t hold as asymmetry prevents the case that `yRx`. Since `xRy`, then `yRx` cannot hold because asymmetry prevents reciprocal relations. This contradiction makes it incompatible for OWL reasoners.

- **Conflict: Asymmetric Ai and Transitive B**  
  
  Suppose `Ai` is asymmetric, and `B` is transitive. This corresponds to the second row (Ai) and the second column (B) of the table, marked with “N”. Since asymmetry holds, if `xRy`, then it is not the case that `yRx`.  
  
  This creates a conflict since `B` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold, but asymmetry can’t hold as asymmetry prevents the case that `yRx`. Asymmetric `Ai` restricts reciprocal interactions, and transitive `B` extends relationships across elements to suggest connections that conflict with the asymmetry of `Ai`. This contradicti

- **Conflict: Asymmetric Ai and Transitive Bi**  
  
  Suppose `Ai` is asymmetric, and `Bi` is transitive. This corresponds to the second row (Ai) and the fourth column (Bi) of the table, marked with “N”. Since asymmetry holds, if `xRy`, then it is not the case that `yRx`.  
  
  This creates a conflict since `Bi` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold, but asymmetry can’t hold as asymmetry prevents the case that `yRx`. This contradiction makes it incompatible for OWL reasoners.

- **Conflict: Asymmetric B and Transitive Bi**  
  
  Suppose `B` is asymmetric, and `Bi` is transitive. This corresponds to the third row (B) and the fifth column (Bi) of the table, marked with “N”.  
  
  This creates a conflict since `Bi` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold, but asymmetry can’t hold as asymmetry prevents the case that `yRx`. This contradiction makes it incompatible for OWL

- **Conflict: Asymmetric Bi and Transitive Bi**  
  
  Suppose `Bi` is asymmetric, and `Bi` is transitive. This corresponds to the fourth row (Bi) and the fourth column (Bi) of the table, marked with “N”.  
  
  This creates a conflict since `Bi` is transitive; because in transitivity, if `xRy` and `yRz`, then `xRz` must hold, but asymmetry can’t hold as asymmetry prevents the case that `yRx`. This contradiction makes it incompatible for OWL reasoners.
