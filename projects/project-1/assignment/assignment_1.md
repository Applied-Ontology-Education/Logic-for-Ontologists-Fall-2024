
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

- Ref/Irref

![image](https://github.com/user-attachments/assets/745b2fa1-7bbf-4f0e-bdea-fb27a40496c4)

- For A/A, see Exercise 1
  
- For A/Ai, suppose that A is irreflexive and Ai is reflexive. By irreflexivity, it is not the case that xAx. By reflexivity, it is the case that xAix. Being Ai the inverse of A, it is the case that the relation A holds between the opposite instances in the relation Ai, which in this case are both x. That is, xAx. But this contradicts the irreflexivity of A.
  
- For Ai/A, suppose that Ai is irreflexive and A is reflexive. By irreflexivity, it is not the case that xAix. By reflexivity, it is the case that xAx. Being A the inverse of Ai, it is the case that the relation Ai holds between the opposite instances in the relation A, which in this case are both x. That is, xAix. But this contradicts the irreflexivity of Ai.
  
- For Ai/Ai, see Exercise 1
  
- For A/B, suppose that A is irreflexive and B is reflexive. By irreflexivity, it is not the case that xAx. By reflexivity, it is the case that xBx. Being a subproperty of A, B implies that all the couple of entities connected by B are also connected by A. That is, xBx implies xAx. But this contradicts irreflexivity of A.
  
- For Ai/B, suppose that Ai is irreflexive and B is reflexive. By irreflexivity, it is not the case that xAix. By reflexivity, it is the case that xBx. By being the inverse of A, the fact that it is not the case that xAix implies that it is not the case that the entities in the domain and range appear in the opposite range and domain of A. That is, it is not the case that xAx. Being a subproperty of A, B implies that all the couple of entities connected by B are also connected by A. That is, xBx implies xAx. This creates a contradiction with the previous step.
  
- For A/Bi, suppose that A is irreflexive and Bi is reflexive. By irreflexivity, it is not the case that xAx. By reflexivity, it is the case that xBix. Being a subproperty of Ai, Bi implies that all the couple of entities connected by Bi are also connected by Ai. That is, xBix implies xAix. Being A the inverse of Ai, it is the case that the relation A holds between the opposite instances in the relation Ai, which in this case are both x. That is, xAix implies xAx. But this contradicts th irreflexivity of A.
  
- For Ai/Bi, suppose that Ai is irreflexive and that Bi is reflexive. By irreflexivity, it is not the case that xAix. By reflexivity, it is the case that xBix. Being Bi the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi, which in this case are both x. Being a subproperty of A, B implies that all the couple of entities connected by B are also connected by A. That is, xBx implies xAx. But this contradicts irreflexivity of A.
  
-  For B/B, see Exercise 1

- For B/Bi, suppose that B is irreflexive and Bi is reflexive. By irreflexivity, it is not the case that xBx. By reflexivity, it is the case that xBix. Being Bi the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi, which in this case are both x. That is, xBx. But this contradicts the irreflexivity of B.

-  For Bi/Bi, see Exercise 1



