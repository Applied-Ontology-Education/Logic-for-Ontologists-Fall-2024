
|        | Funct. | iFunct. | Trans. | Symm. | Asymm. | Ref. | Irref. |
|--------|--------|---------|--------|-------|--------|------|--------|
| **Funct.**   | -      | OK      | X<sup>NS</sup>    | OK    | OK     | OK   | OK     |
| **iFunct.**  | OK     | -       | X<sup>NS</sup>    | OK    | OK     | OK   | OK     |
| **Trans.**   | X<sup>NS</sup>    | X<sup>NS</sup>     | -      | OK    | X<sup>NS</sup>    | OK   | X<sup>NS</sup>    |
| **Symm.**    | OK     | OK      | OK     | -     | X<sup>UNSAT</sup> | OK   | OK     |
| **Asymm.**   | OK     | OK      | X<sup>NS</sup>    | X<sup>UNSAT</sup>| -      | X<sup>UNSAT</sup>| OK    |
| **Ref.**     | OK     | OK      | OK     | OK    | X<sup>UNSAT</sup> | -    | X<sup>UNSAT</sup> |
| **Irref.**   | OK     | OK      | X<sup>NS</sup>    | OK    | OK     | X<sup>UNSAT</sup>| -      |


Trans.-Funct (NS)

Suppose that a relation R is both transitive and functional. This means that R 

Trans.-iFunct (NS)

Suppose that a relation

Asymm-Trans (NS)

Suppose that a relation R is both transitive and asymmetric. This means that if xRy and yRz, then xRz, and that if xRy, then it is not the case that yRx. This means that for all 

Asymm-Symm (UNSAT) (done by JB)

Ref-Asymm (UNSAT)

Suppose that a relation R is both reflexive and asymmetric. By reflexivity, for any x, x is related to itself by R, i.e. xRx. By asymmetry, for any x and any y, if it is the case that xRy, then it is not the case that yRx. But for reflexivity, the only entities in R are x. That is, y=x. Plugging that in, we both have that xRx for reflexivity, and that it is not the case that xRx for asymmetry. This is thus not satisfiable.

Ref-Irref (UNSAT)

Suppose that a relation R is both reflexive and irreflexive. By reflexivity, we have that xRx. By irreflexivity, we have that it is not the case that xRx. This is not a satisfiable formula.


Exercise 2

iFunct-Trans

<img width="616" alt="image" src="https://github.com/user-attachments/assets/f0c0db1e-5bd0-4e2f-82b3-b43cc5412b33">


Funct-Trans

<img width="605" alt="image" src="https://github.com/user-attachments/assets/f4e8da51-221f-46fa-98ad-06e93d5009ba">

