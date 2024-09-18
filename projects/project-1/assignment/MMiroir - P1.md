# Project 1: OWL Cheat Sheet
Collaborative attempt by Jay Bittner, Tim Coleman, and Mathilde Miroir

## Assignment Part 1
### Role Constraint Combinations**
|            | Funct. | iFunct.| Trans. | Symm.     | Asymm.    | Ref.      |Irref.     |
|--------    |--------|--------|--------|-------    |--------   |-----      |--------   |
| **Funct.** |-       | OK     |X<sup>NS| OK        | OK        | OK        | OK        |
| **iFunct.**|OK      | -      |X<sup>NS| OK        | OK        | OK        | OK        |
| **Trans.** |X<sup>NS|X<sup>NS| -      | OK        |X<sup>NS   | OK        |X<sup>NS   |
| **Symm.**  |OK      | OK     | OK     | -         |X<sup>UNSAT| OK        | OK        |
| **Asymm.** |OK      | OK     |X<sup>NS|X<sup>UNSAT| -         |X<sup>UNSAT| OK        |
| **Ref.**   |OK      | OK     | OK     |     OK    |X<sup>UNSAT| -         |X<sup>UNSAT|
| **Irref.** | OK     | OK     |X<sup>NS|     OK    |    OK     |X<sup>UNSAT| -         |

**_provided by the assignment instructions_

### Explanations

The following example, provided in the assignment, serves as the guide for which all following explanations adhere to: 
- To explain why `R` cannot be both asymmetric and symmetric, your explanation may take the form: Suppose `R` is both symmetric and asymmetric. Then by symmetry for any x and y, if x`R`y it follows that y`R`x. However, by asymmetry it also follows that it is not the case that y`R`x. Hence, `R` cannot be both symmetric and asymmetric. Similarly, to explain why `R` cannot be both transitive and inverse functional.

#### (1) Transitive + Functional (NS)
- Suppose `R` is both transitive and functional. By transitivity for any x and y, if x`R`y and y`R`z, it follows that x`R`z. By functionality, if x`R`y and x`R`z, then it follows that y=z. 

####  (2) Transitive + Inverse Functional (NS)
- Suppose `R` is both transitive and inverse functional. By transitivity for any x and y, if x`R`y and y`R`z, it follows that x`R`z. By inverse functional, if xRy and zRy, it follows that x=z.


#### (3) Assymetric + Transitive (NS)
- Suppose `R` is both assymetric and transitive. By assymetry, if xRy, then it is not the case that yRx. By transitivity, if xRy and yRz, then xRz.

#### (4) Assymetric + Symmetric (UNSAT)
- _Explained in the assignment instructions_ : Suppose `R` is both symmetric and asymmetric. Then by symmetry for any x and y, if x`R`y it follows that y`R`x. However, by asymmetry it also follows that it is not the case that y`R`x. Hence, `R` cannot be both symmetric and asymmetric.

#### (5) Assymetric + Reflexive (UNSAT)
- Suppose `R` is both assymetric and reflexive. By assymetry, f xRy, then it is not the case that yRx. By reflexivity, xRx.

#### (6)Reflexive + Irreflexive (UNSAT)
- Suppose `R` is both reflexive and irreflexive. Then by reflexivity for any x, x`R`x. However by irreflexivity, it also follows that it is not the case that xRx. Hence, `R` cannot be both reflexive and irreflexive. Similary for the case of why `R` cannot be both symmetric and assymetric.


#### (7) Irreflexive + Transitive (NS)
- Suppose `R` is both irreflexive and transitive.  By irreflexivity, it is not the case that xRx. By transitivity, for any x and y, if x`R`y and y`R`z, it follows that x`R`z.

## Assignment Part 2

### Note

- reflexive vs irreflexive (low priority)

- symm vs asymm (low priority)

### Variable Constraints

- `B` owl:subPropertyOf of `A`
- `Bi` owl:subPropertyOf of `Ai`
- `Ai` is the inverse of `A`
- `Bi` is the inverse of `B`

### (A) Transitive and Irreflexive Trials 
|            | A Trans | B Trans | Ai Trans | Bi Trans |
|------------|---------|---------|----------|----------|
| **A Irr**  | N<sub>1 | N<sub>2 | N<sub>3  | N<sub>4  |
| **B Irr**  | Y<sub>5 | N<sub>6 | Y<sub>7  | N<sub>8  |
| **Ai Irr** | N<sub>9 | N<sub>10| N<sub>11 | N<sub>12 |
| **Bi Irr** | Y<sub>13| N<sub>14| Y<sub>15 | N<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_

### (B) Transitive and Functional Trials  (j's previous contribution - replace A with x or y)

|             | A Trans | B Trans | Ai Trans | Bi Trans |
|-------------|---------|---------|----------|----------|
| **A Func**  | A<sub>1 | A<sub>2 | A<sub>3  | A<sub>4  |
| **B Func**  | A<sub>5 | A<sub>6 | A<sub>7  | A<sub>8  |
| **Ai Func** | A<sub>9 | A<sub>10| A<sub>11 | A<sub>12 |
| **Bi Func**  | A<sub>13| A<sub>14| A<sub>15 | A<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_


### (C) trans vs infunc??? same as previous?
|              | A Trans | B Trans | Ai Trans | Bi Trans |
|--------------|---------|---------|----------|----------|
| **A iFunc**  | A<sub>1 | A<sub>2 | A<sub>3  | A<sub>4  |
| **B iFunc**  | A<sub>5 | A<sub>6 | A<sub>7  | A<sub>8  |
| **Ai iFunc** | A<sub>9 | A<sub>10| A<sub>11 | A<sub>12 |
| **Bi iFUnc** | A<sub>13| A<sub>14| A<sub>15 | A<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_

### (D) Transitive and Asymmetric Trials  (Tim's HW - replace A with x or y)
|              | A Trans | B Trans | Ai Trans | Bi Trans |
|--------------|---------|---------|----------|----------|
| **A Asymm**  | A<sub>1 | A<sub>2 | A<sub>3  | A<sub>4  |
| **B Asymm**  | A<sub>5 | A<sub>6 | A<sub>7  | A<sub>8  |
| **Ai Asymm** | A<sub>9 | A<sub>10| A<sub>11 | A<sub>12 |
| **Bi Asymm** | A<sub>13| A<sub>14| A<sub>15 | A<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_


### (E) Transitive and Asymmetric Trials  (J's HW - replace A with x or y)
|              |A Reflex |B Reflex |Ai Reflex |Bi Reflex |
|--------------|---------|---------|----------|----------|
| **A Asymm**  | A<sub>1 | A<sub>2 | A<sub>3  | A<sub>4  |
| **B Asymm**  | A<sub>5 | A<sub>6 | A<sub>7  | A<sub>8  |
| **Ai Asymm** | A<sub>9 | A<sub>10| A<sub>11 | A<sub>12 |
| **Bi Asymm** | A<sub>13| A<sub>14| A<sub>15 | A<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_



### Explanations (IN PROGRESS)

#### (A) Transitive and Irreflexive Explanations
- (A-1) Suppose `A` is both irreflexive and transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-2) Suppose `A` is irreflexive and `B` is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-3) Suppose `A` is irreflexive and its inverse , `Ai`, is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-4) Suppose `A` is irreflexive and `Bi` is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-5) Suppose `B` is irreflexive and `A` is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-6) Suppose `B` is both irreflexive and transitive. Because `B` is irreflexive, it is not the case for any `x` that `<x,x>` is in `B`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-7) Suppose `B` is irreflexive and `Ai` is transitive. Because `B` is irreflexive, it is not the case for any `x` that `<x,x>` is in `B`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-8) Suppose `B` is irreflexive and its inverse , `Bi`, is transitive. Because `B` is irreflexive, it is not the case for any `x` that `<x,x>` is in `B`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-9) Suppose `Ai` is irreflexive and its inverse , `A`, is transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-10) Suppose `Ai` is irreflexive and `B` is transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-11) Suppose `Ai` is both irreflexive and transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-12) Suppose `Ai` is irreflexive and `Bi` is transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-13) Suppose `Bi` is irreflexive and `A` is transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-14) Suppose `Bi` is irreflexive and its inverse , `B`, is transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-15) Suppose `Bi` is irreflexive and `Ai` is transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

- (A-16) Suppose `Bi` is both irreflexive and transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 



#### (B) Transitive and Functional

- (B-1) Suppose `A` is both transitive and functional. 

Because `A` is transitive, it is 

Because `A` is functional, if  

- (B-2) Suppose `A` is transitive and `B` is functional. 

Because `A` is transitive, 

Because `B` is functional, if  

- (B-3) Suppose `A` is transitive and its inverse , `Ai`, is functional. 

Because `A` is transitive, it is 

Because `Ai` is functional, if 

- (B-4) Suppose `A` is transitive and `Bi` is functional. 

Because `A` is transitive,

Because `Bi` is functional,

- (B-5) Suppose `B` is transitive and `A` is functional. 

Because `A` is transitive,  

Because `A` is functional,

- (B-6) Suppose `B` is both transitive and functional. 

Because `B` is transitive, 

Because `B` is functional, 

- (B-7) Suppose `B` is transitive and `Ai` is functional. 

Because `B` is transitive,  

Because `Ai` is functional,

- (B-8) Suppose `B` is transitive and its inverse , `Bi`, is functional. 

Because `B` is transitive,  

Because `Bi` is functional,

- (B-9) Suppose `Ai` is transitive and its inverse , `A`, is functional. 

Because `Ai` is transitive,  

Because `A` is functional, 

- (B-10) Suppose `Ai` is transitive and `B` is functional. 

Because `Ai` is transitive, 

Because `B` is functional, 

- (B-11) Suppose `Ai` is both transitive and functional. 

Because `Ai` is transitive,  

Because `Ai` is functional, 

- (B-12) Suppose `Ai` is transitive and `Bi` is functional. 

Because `Ai` is transitive, 

Because `Bi` is functional, 

- (B-13) Suppose `Bi` is transitive and `A` is functional. 

Because `Bi` is transitive, 

Because `A` is functional, 

- (B-14) Suppose `Bi` is transitive and its inverse , `B`, is functional. 

Because `Bi` is transitive,

Because `B` is functional,  

- (B-15) Suppose `Bi` is transitive and `Ai` is functional. 

Because `Bi` is transitive,

Because `Ai` is functional, 

- (B-16) Suppose `Bi` is both transitive and functional. 

Because `Bi` is transitive, 

Because `Bi` is functional, 

#### (C) Transitive and Inverse Functional

#### (D) Transitive and Asymmetric

- (D-1) Suppose `A` is both transitive and functional. 

Because `A` is transitive, it is 

Because `A` is functional, if  

- (D-2) Suppose `A` is transitive and `B` is functional. 

Because `A` is transitive, 

Because `B` is functional, if  

- (D-3) Suppose `A` is transitive and its inverse , `Ai`, is functional. 

Because `A` is transitive, it is 

Because `Ai` is functional, if 

- (D-4) Suppose `A` is transitive and `Bi` is functional. 

Because `A` is transitive,

Because `Bi` is functional,

- (D-5) Suppose `B` is transitive and `A` is functional. 

Because `A` is transitive,  

Because `A` is functional,

- (D-6) Suppose `B` is both transitive and functional. 

Because `B` is transitive, 

Because `B` is functional, 

- (D-7) Suppose `B` is transitive and `Ai` is functional. 

Because `B` is transitive,  

Because `Ai` is functional,

- (D-8) Suppose `B` is transitive and its inverse , `Bi`, is functional. 

Because `B` is transitive,  

Because `Bi` is functional,

- (D-9) Suppose `Ai` is transitive and its inverse , `A`, is functional. 

Because `Ai` is transitive,  

Because `A` is functional, 

- (D-10) Suppose `Ai` is transitive and `B` is functional. 

Because `Ai` is transitive, 

Because `B` is functional, 

- (D-11) Suppose `Ai` is both transitive and functional. 

Because `Ai` is transitive,  

Because `Ai` is functional, 

- (D-12) Suppose `Ai` is transitive and `Bi` is functional. 

Because `Ai` is transitive, 

Because `Bi` is functional, 

- (D-13) Suppose `Bi` is transitive and `A` is functional. 

Because `Bi` is transitive, 

Because `A` is functional, 

- (D-14) Suppose `Bi` is transitive and its inverse , `B`, is functional. 

Because `Bi` is transitive,

Because `B` is functional,  

- (D-15) Suppose `Bi` is transitive and `Ai` is functional. 

Because `Bi` is transitive,

Because `Ai` is functional, 

- (D-16) Suppose `Bi` is both transitive and functional. 

Because `Bi` is transitive, 

Because `Bi` is functional, 


#### (E) Transitive and Asymmetric

- (E-1) Suppose `A` is both transitive and asymmetric. 

Because `A` is transitive, it is 

Because `A` is asymmetric, if  

- (E-2) Suppose `A` is transitive and `B` is functional. 

Because `A` is transitive, 

Because `B` is asymmetric, if  

- (E-3) Suppose `A` is transitive and its inverse , `Ai`, is functional. 

Because `A` is transitive, it is 

Because `Ai` is asymmetric, if 

- (E-4) Suppose `A` is transitive and `Bi` is functional. 

Because `A` is transitive,

Because `Bi` is asymmetric,

- (E-5) Suppose `B` is transitive and `A` is functional. 

Because `A` is transitive,  

Because `A` is asymmetric,

- (E-6) Suppose `B` is both transitive and functional. 

Because `B` is transitive, 

Because `B` is asymmetric, 

- (E-7) Suppose `B` is transitive and `Ai` is functional. 

Because `B` is transitive,  

Because `Ai` is asymmetric,

- (E-8) Suppose `B` is transitive and its inverse , `Bi`, is functional. 

Because `B` is transitive,  

Because `Bi` is asymmetric,

- (E-9) Suppose `Ai` is transitive and its inverse , `A`, is functional. 

Because `Ai` is transitive,  

Because `A` is asymmetric, 

- (E-10) Suppose `Ai` is transitive and `B` is functional. 

Because `Ai` is transitive, 

Because `B` is asymmetric, 

- (E-11) Suppose `Ai` is both transitive and functional. 

Because `Ai` is transitive,  

Because `Ai` is asymmetric, 

- (E-12) Suppose `Ai` is transitive and `Bi` is functional. 

Because `Ai` is transitive, 

Because `Bi` is asymmetric, 

- (E-13) Suppose `Bi` is transitive and `A` is functional. 

Because `Bi` is transitive, 

Because `A` is asymmetric, 

- (E-14) Suppose `Bi` is transitive and its inverse , `B`, is functional. 

Because `Bi` is transitive,

Because `B` is asymmetric,  

- (E-15) Suppose `Bi` is transitive and `Ai` is functional. 

Because `Bi` is transitive,

Because `Ai` is asymmetric, 

- (E-16) Suppose `Bi` is both transitive and functional. 

Because `Bi` is transitive, 

Because `Bi` is asymmetric, 