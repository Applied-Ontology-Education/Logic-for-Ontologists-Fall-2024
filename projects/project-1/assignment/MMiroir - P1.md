# Project 1: OWL Cheat Sheet
Collaborative attempt by Jay Bittner, Tim Coleman, and Mathilde Miroir

## Assignment Part 1

### Table I. OWL2 DL Direct Semantics Role Constraints

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



### Table II. Role Constraint Combinations***
|            | Funct. | iFunct.| Trans. | Symm.     | Asymm.    | Ref.      |Irref.     |
|--------    |--------|--------|--------|-------    |--------   |-----      |--------   |
| **Funct.** |-       | OK     |X<sup>NS| OK        | OK        | OK        | OK        |
| **iFunct.**|OK      | -      |X<sup>NS| OK        | OK        | OK        | OK        |
| **Trans.** |X<sup>NS|X<sup>NS| -      | OK        |X<sup>NS   | OK        |X<sup>NS   |
| **Symm.**  |OK      | OK     | OK     | -         |X<sup>UNSAT| OK        | OK        |
| **Asymm.** |OK      | OK     |X<sup>NS|X<sup>UNSAT| -         |X<sup>UNSAT| OK        |
| **Ref.**   |OK      | OK     | OK     |     OK    |X<sup>UNSAT| -         |X<sup>UNSAT|
| **Irref.** | OK     | OK     |X<sup>NS|     OK    |    OK     |X<sup>UNSAT| -         |

*_NS denotes a combination creates an object property chain that may lead to undecidability_

**_UNSAT denotes a combination that is unsatisfiable_

***_Provided by the assignment instructions_

For the purposes of this assignment, the diagonal of the matrix in the above table (II) was ignored as these are not combinations of properties. Given that the matrix is also reflective across the diagonal, only side of the diagonal was observed and tested. Please note that this assignment does not explore Transitive & Inverse Functional (**C**) of the **NS** results or any of the **UNSAT** results.

According to the table above (II), there are four property combinations which yielded an undecidable (**NS**) result: 

- (**A**) Irreflexive **&** Transitive

- (**B**) Transitive **&** Functional

- (**C**) Transitive **&** Inverse Functional

- (**D**) Transitive **&** Assymetric

There are three property combinations which yield an unsatifiable (**UNSAT**) result:

- (**E**) Assymetric **&** Symmetric

- (**F**)) Assymetric **&** Reflexive 

- (**G**) Reflexive **&** Irreflexive


### Explanations

The following example, provided in the assignment, serves as the guide for which all following explanations adhere to: 
- To explain why `R` cannot be both asymmetric and symmetric, your explanation may take the form: Suppose `R` is both symmetric and asymmetric. Then by symmetry for any x and y, if x`R`y it follows that y`R`x. However, by asymmetry it also follows that it is not the case that y`R`x. Hence, `R` cannot be both symmetric and asymmetric. Similarly, to explain why `R` cannot be both transitive and inverse functional.

#### (A) Transitive + Irreflexive (NS)
- Suppose `R` is both irreflexive and transitive.  By irreflexivity, it is not the case that xRx. By transitivity, for any x and y, if x`R`y and y`R`z, it follows that x`R`z.

When `R` is irreflexive it can never relate back to itself but when `R` is transitive, it can relate to multiple variables via the same relationship including but not necessarily limited to itself.

#### (B) Transitive + Functional (NS)
- Suppose `R` is both transitive and functional. By transitivity for any x and y, if x`R`y and y`R`z, it follows that x`R`z. By functionality, if x`R`y and x`R`z, then it follows that y=z. 

When `R` is functional, it relates to single variable where as when it is transitive it communicates a single type of relationship that can apply to multiple variables. These are in conflict.

#### (C) Transitive + Inverse Functional (NS)
- Suppose `R` is both transitive and inverse functional. By transitivity for any x and y, if x`R`y and y`R`z, it follows that x`R`z. By inverse functional, if xRy and zRy, it follows that x=z.

The argumentative limitations for the transitive and functional combination of properties applies here aswell.

#### (D) Transitive + Assymetric (NS)
- Suppose `R` is both assymetric and transitive. By assymetry, if xRy, then it is not the case that yRx. By transitivity, if xRy and yRz, then xRz.

When `R` is assymetric, the `R` relationship is unidirectional and when `R` is transitive, the `R` relationship can be applied circularly or bidirectionally which is in conflict with a limited unidirectional relationship.

#### (E) Assymetric + Symmetric (UNSAT) - _Explained in the assignment instructions_
- Suppose `R` is both symmetric and asymmetric. Then by symmetry for any x and y, if x`R`y it follows that y`R`x. However, by asymmetry it also follows that it is not the case that y`R`x. Hence, `R` cannot be both symmetric and asymmetric.

#### (F) Assymetric + Reflexive (UNSAT)
- Suppose `R` is both assymetric and reflexive. By assymetry, f xRy, then it is not the case that yRx. By reflexivity, xRx.

When `R` is assymetric, the `R` relationship is unidirectional, but by reflexivity, the `R` 'flows' back to itself and therefore works bidirectionaly.

#### (G) Reflexive + Irreflexive (UNSAT)
- Suppose `R` is both reflexive and irreflexive. Then by reflexivity for any x, x`R`x. However by irreflexivity, it also follows that it is not the case that xRx. Hence, `R` cannot be both reflexive and irreflexive. Similary for the case of why `R` cannot be both symmetric and assymetric.

The `R` relationship cannot be defined such that it relates something to itself and also cannot relate something to itself.

## Assignment Part 2 **PLEASE NOTE THIS IS INCOMPLETE

### Variable Constraints

- `B` owl:subPropertyOf of `A`
- `Bi` owl:subPropertyOf of `Ai`
- `Ai` is the inverse of `A`
- `Bi` is the inverse of `B`

### (A) Transitive and Irreflexive

#### Table III. (A) Transitive and Irreflexive Trials 
|            | A Trans | B Trans | Ai Trans | Bi Trans |
|------------|---------|---------|----------|----------|
| **A Irr**  | N<sub>1 | N<sub>2 | N<sub>3  | N<sub>4  |
| **B Irr**  | Y<sub>5 | N<sub>6 | Y<sub>7  | N<sub>8  |
| **Ai Irr** | N<sub>9 | N<sub>10| N<sub>11 | N<sub>12 |
| **Bi Irr** | Y<sub>13| N<sub>14| Y<sub>15 | N<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_

- The trials performed, for the combination of transitive and irreflexive roles, indicated that when a property (A or Ai) is transitive and its subproperty (B or Bi) or the inverse of its subproperty (Bi or B) is irreflexive there are no conflicts in OWL.


- Conversley, any instance in which a property (A or Ai) was irreflexive and its inverse (Ai or A) or its subproperty (B or Bi) or the inverse of its subproperty (Bi or B) was transitive, there is a conflict in OWL.

#### (A) Transitive and Irreflexive Explanations

- (A-1) Suppose `A` is both irreflexive and transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. A single property cannot be both irreflexive and transitive as explained in the above part of this assignment. _This applies to instances in which A is both irreflexive and transitive (**A-1**), B is both irreflexive and transitive (**A-6**), Ai is both irreflexive and transitive (**A-11**), Bi is both irreflexive and transitive (**A-16**)._

- (A-2) Suppose `A` is irreflexive and `B` is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

ADD EXPLANATION HERE - 

Defining `A` as irreflexive insinuates that `B`, which is a subproperty of `A` also bears the irreflexive role. Since `B` has been defined to bear the transitive role, this is in direct conflict since a property cannot bear both an irreflexive and transitive role, as has been explained above in part 1 of this assignment. _This explanation applies to where (), (), (), and () similarly as the combinations of subproperties and their roles result in a single subproperty bearing both the transitive and irreflexive role._


- (A-3) Suppose `A` is irreflexive and its inverse , `Ai`, is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `Ai` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

ADD EXPLANATION HERE - 

- (A-4) Suppose `A` is irreflexive and `Bi` is transitive. Because `A` is irreflexive, it is not the case for any `x` that `<x,x>` is in `A`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

ADD EXPLANATION HERE

- (A-8) Suppose `B` is irreflexive and its inverse , `Bi`, is transitive. Because `B` is irreflexive, it is not the case for any `x` that `<x,x>` is in `B`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

ADD EXPLANATION HERE

- (A-9) Suppose `Ai` is irreflexive and its inverse , `A`, is transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `A` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

ADD EXPLANATION HERE

- (A-10) Suppose `Ai` is irreflexive and `B` is transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

ADD EXPLANATION HERE


- (A-12) Suppose `Ai` is irreflexive and `Bi` is transitive. Because `Ai` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Ai`. Because `Bi` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

ADD EXPLANATION HERE

- (A-14) Suppose `Bi` is irreflexive and its inverse , `B`, is transitive. Because `Bi` is irreflexive, it is not the case for any `x` that `<x,x>` is in `Bi`. Because `B` is transitive, if `<x,y>` and `<y,z>`, then `<x,z>`. 

ADD EXPLANATION HERE - SUCCESSFUL

## EXPLANATIONS PAST THIS POINT TO BE EXPLORED (I just had surgery so could not explore this fully)

### (B) Transitive and Functional

#### Table IV. (B) Transitive and Functional Trials

|             | A Trans | B Trans | Ai Trans | Bi Trans |
|-------------|---------|---------|----------|----------|
| **A  Func** | N<sub>1 | N<sub>2 | N<sub>3  | N<sub>4  |
| **B  Func** | N<sub>5 | N<sub>6 | N<sub>7  | N<sub>8  |
| **Ai Func** | Y<sub>9 | Y<sub>10| N<sub>11 | N<sub>12 |
| **Bi Func** | Y<sub>13| Y<sub>14| N<sub>15 | N<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_

- (B-1) Suppose `A` is both transitive and functional. Because `A` is transitive, if x`R`y and y`R`z, then x`R`z. Because `A` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-2) Suppose `A` is transitive and `B` is functional. Because `A` is transitive, if x`R`y and y`R`z, then x`R`z. Because `B` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-3) Suppose `A` is transitive and its inverse , `Ai`, is functional. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Ai` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-4) Suppose `A` is transitive and `Bi` is functional. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Bi` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-5) Suppose `B` is transitive and `A` is functional. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `A` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-6) Suppose `B` is both transitive and functional. Because `B` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `B` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-7) Suppose `B` is transitive and `Ai` is functional. Because `B` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Ai` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-8) Suppose `B` is transitive and its inverse , `Bi`, is functional. Because `B` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Bi` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-9) Suppose `Ai` is transitive and its inverse , `A`, is functional. Because `Ai` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `A` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-10) Suppose `Ai` is transitive and `B` is functional. Because `Ai` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `B` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-11) Suppose `Ai` is both transitive and functional. Because `Ai` is transitive,  if  x`R`y and y`R`z, then x`R`z. Because `Ai` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-12) Suppose `Ai` is transitive and `Bi` is functional. Because `Ai` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Bi` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-13) Suppose `Bi` is transitive and `A` is functional. Because `Bi` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `A` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-14) Suppose `Bi` is transitive and its inverse , `B`, is functional. Because `Bi` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `B` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-15) Suppose `Bi` is transitive and `Ai` is functional. Because `Bi` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Ai` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE

- (B-16) Suppose `Bi` is both transitive and functional. Because `Bi` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Bi` is functional, if x`R`y and x`R`z, then y=z.

ADD EXPLANATION HERE


### (C) Transitive and Inverse Functional - Not to be developed in this assignment.


#### Table V. (C) Transitive and Inverse Functional

|              | A Trans | B Trans | Ai Trans | Bi Trans |
|--------------|---------|---------|----------|----------|
| **A iFunc**  | -<sub>1 | -<sub>2 | -<sub>3  | -<sub>4  |
| **B iFunc**  | -<sub>5 | -<sub>6 | -<sub>7  | -<sub>8  |
| **Ai iFunc** | -<sub>9 | -<sub>10| -<sub>11 | -<sub>12 |
| **Bi iFUnc** | -<sub>13| -<sub>14| -<sub>15 | -<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_

### (D) Transitive and Asymmetric

#### Table VI. (D) Transitive and Asymmetric Trials

|            | A Trans | B Trans | Ai Trans | Bi Trans |
|------------|---------|---------|----------|----------|
| **A Asym** | N<sub>1 | N<sub>2 | N<sub>3  | N<sub>4  |
| **B Asym** | N<sub>5 | N<sub>6 | N<sub>7  | N<sub>8  |
| **Ai Asym**| Y<sub>9 | Y<sub>10| N<sub>11 | N<sub>12 |
| **Bi Asym**| Y<sub>13| Y<sub>14| N<sub>15 | N<sub>16 |

*_N denotes an error while Y denotes a successful run_

**_Subscripts denote corresponding explantion below_


- (D-1) Suppose `A` is both transitive and asymmetric. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `A` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-2) Suppose `A` is transitive and `B` is functional. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `B` is asymmetric, if xRy, then it is not the case that yRx.   

ADD EXPLANATION HERE

- (D-3) Suppose `A` is transitive and its inverse , `Ai`, is functional. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Ai` is asymmetric, if xRy, then it is not the case that yRx.  

ADD EXPLANATION HERE

- (D-4) Suppose `A` is transitive and `Bi` is functional. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Bi` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-5) Suppose `B` is transitive and `A` is functional. Because `A` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `A` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-6) Suppose `B` is both transitive and functional. Because `B` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `B` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-7) Suppose `B` is transitive and `Ai` is functional. Because `B` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Ai` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-8) Suppose `B` is transitive and its inverse , `Bi`, is functional. Because `B` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Bi` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-9) Suppose `Ai` is transitive and its inverse , `A`, is functional. Because `Ai` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `A` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-10) Suppose `Ai` is transitive and `B` is functional. Because `Ai` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `B` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-11) Suppose `Ai` is both transitive and functional. Because `Ai` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Ai` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-12) Suppose `Ai` is transitive and `Bi` is functional. Because `Ai` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Bi` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-13) Suppose `Bi` is transitive and `A` is functional. Because `Bi` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `A` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-14) Suppose `Bi` is transitive and its inverse , `B`, is functional. Because `Bi` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `B` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-15) Suppose `Bi` is transitive and `Ai` is functional. Because `Bi` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Ai` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE

- (D-16) Suppose `Bi` is both transitive and functional. Because `Bi` is transitive, if  x`R`y and y`R`z, then x`R`z. Because `Bi` is asymmetric, if xRy, then it is not the case that yRx. 

ADD EXPLANATION HERE
