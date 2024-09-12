# Project 1: OWL Cheat Sheet

## Note
My results for assignment 2 vary significantly from the example chart provided. I believe I set everything up correctly but only achieved a single successful combination. Still learning how to write axioms/arguments...

## Assignment Part 1
### Role Constraint Combinations**
|            | Funct.  | iFunct. | Trans. | Symm.    | Asymm.    | Ref.      |Irref.     |
|--------    |-------- |---------|--------|-------   |--------   |-----      |--------   |
| **Funct.** |-       | OK      |X<sup>NS| OK        | OK        | OK        | OK        |
| **iFunct.**|OK      | -       |X<sup>NS| OK        | OK        | OK        | OK        |
| **Trans.** |X<sup>NS| X<sup>NS| -      | OK        |X<sup>NS   | OK        |X<sup>NS   |
| **Symm.**  |OK      | OK      | OK     | -         |X<sup>UNSAT| OK        | OK        |
| **Asymm.** |OK      | OK      |X<sup>NS|X<sup>UNSAT| -         |X<sup>UNSAT| OK        |
| **Ref.**   |OK      | OK      | OK     |     OK    |X<sup>UNSAT| -         |X<sup>UNSAT|
| **Irref.** | OK     | OK      |X<sup>NS|     OK    |    OK     |X<sup>UNSAT| -         |

**_provided by the assignment instructions_

For example, to explain why `R` cannot be both asymmetric and symmetric, your explanation may take the form: 
- Suppose `R` is both symmetric and asymmetric. Then by symmetry for any x and y, if x`R`y it follows that y`R`x. However, by asymmetry it also follows that it is not the case that y`R`x. Hence, `R` cannot be both symmetric and asymmetric.
Similarly, to explain why `R` cannot be both transitive and inverse functional.

#### Transitive + Functional -> NS
- Suppose `R` is both transitive and functional. By transitivity for any x and y, if x`R`y and y`R`z, it follows that x`R`z. By functionality, if x`R`y and x`R`z, then it follows that y=z. 

####  Transitive + Inverse Functional -> NS
- Suppose `R` is both transitive and inverse functional. By transitivity for any x and y, if x`R`y and y`R`z, it follows that x`R`z. By inverse functional, if xRy and zRy, it follows that x=z.


#### Assymetric + Transitive -> NS
- Suppose `R` is both assymetric and transitive. By assymetry, if xRy, then it is not the case that yRx. By transitivity, if xRy and yRz, then xRz.

#### Assymetric + Symmetric -> UNSAT
- _Explained in the assignment instructions_ : Suppose `R` is both symmetric and asymmetric. Then by symmetry for any x and y, if x`R`y it follows that y`R`x. However, by asymmetry it also follows that it is not the case that y`R`x. Hence, `R` cannot be both symmetric and asymmetric.


#### Assymetric + Reflexive -> UNSAT
- Suppose `R` is both assymetric and reflexive. By assymetry, f xRy, then it is not the case that yRx. By reflexivity, xRx.

#### Reflexive + Irreflexive -> UNSAT
- Suppose `R` is both reflexive and irreflexive. Then by reflexivity for any x, x`R`x. However by irreflexivity, it also follows that it is not the case that xRx. Hence, `R` cannot be both reflexive and irreflexive. Similary for the case of why `R` cannot be both symmetric and assymetric.
xRx
It is not the case that xRx

#### Irreflexive + Transitive -> NS
- Suppose `R` is both irreflexive and transitive.  By irreflexivity, it is not the case that xRx. By transitivity, for any x and y, if x`R`y and y`R`z, it follows that x`R`z.

## Assignment Part 2

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


### Explanations (IN PROGRESS)

- (1)

- (2)

- (3)

- (4)

- (5)

- (6)

- (7)

- (8)

- (9)

- (10)

- (11)

- (12)

- (13)

- (14)

- (15)

- (16)

### Sentences
- (1) Suppose `A` is both irreflexive and transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (2) Suppose `A` is irreflexive and `B` is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (3) Suppose `A` is irreflexive and its inverse , `Ai`, is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (4) Suppose `A` is irreflexive and `Bi` is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (5) Suppose `B` is irreflexive and `A` is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (6) Suppose `B` is both irreflexive and transitive. Because `B` is irreflexive, it is not the case for any `x` that `<x,x>` is in `B`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (7) Suppose `B` is irreflexive and `Ai` is transitive. Because `B` is irreflexive, it is not the case for any `x` that `<x,x>` is in `B`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (8) Suppose `B` is irreflexive and its inverse , `Bi`, is transitive. Because `B` is irreflexive, it is not the case for any `x` that `<x,x>` is in `B`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (9) Suppose `Ai` is irreflexive and its inverse , `A`, is transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (10) Suppose `Ai` is irreflexive and `B` is transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (11) Suppose `Ai` is both irreflexive and transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (12) Suppose `Ai` is irreflexive and `Bi` is transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (13) Suppose `Bi` is irreflexive and `A` is transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (14) Suppose `Bi` is irreflexive and its inverse , `B`, is transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (15) Suppose `Bi` is irreflexive and `Ai` is transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (16) Suppose `Bi` is both irreflexive and transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

