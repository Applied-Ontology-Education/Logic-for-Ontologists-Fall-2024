
|        | Funct. | iFunct. | Trans. | Symm. | Asymm. | Ref. | Irref. |
|--------|--------|---------|--------|-------|--------|------|--------|
| **Funct.**   | -      | OK      | X<sup>NS</sup>    | OK    | OK     | OK   | OK     |
| **iFunct.**  | OK     | -       | X<sup>NS</sup>    | OK    | OK     | OK   | OK     |
| **Trans.**   | X<sup>NS</sup>    | X<sup>NS</sup>     | -      | OK    | X<sup>NS</sup>    | OK   | X<sup>NS</sup>    |
| **Symm.**    | OK     | OK      | OK     | -     | X<sup>UNSAT</sup> | OK   | OK     |
| **Asymm.**   | OK     | OK      | X<sup>NS</sup>    | X<sup>UNSAT</sup>| -      | X<sup>UNSAT</sup>| OK    |
| **Ref.**     | OK     | OK      | OK     | OK    | X<sup>UNSAT</sup> | -    | X<sup>UNSAT</sup> |
| **Irref.**   | OK     | OK      | X<sup>NS</sup>    | OK    | OK     | X<sup>UNSAT</sup>| -      |

\
Trans.-Funct (NS)

Suppose that a relation R is both transitive and functional. This creates a complex role, which known proofs show creates undecidability.

Trans.-iFunct (NS)

Suppose that a relation R is both transitive and inverse functional. This creates a complex role, which known proofs show creates undecidability.

Asymm-Trans (NS)

Suppose that a relation R is both transitive and inverse functional. This creates a complex role, which known proofs show creates undecidability.

Asymm-Symm (UNSAT) (done by JB)

Ref-Asymm (UNSAT)

Suppose that a relation R is both reflexive and asymmetric. By reflexivity, for any x, x is related to itself by R, i.e. xRx. By asymmetry, for any x and any y, if it is the case that xRy, then it is not the case that yRx. But for reflexivity, the only entities in R are x. That is, y=x. Plugging that in, we both have that xRx for reflexivity, and that it is not the case that xRx for asymmetry. This is thus not satisfiable.

Ref-Irref (UNSAT)

Suppose that a relation R is both reflexive and irreflexive. By reflexivity, we have that xRx. By irreflexivity, we have that it is not the case that xRx. This is a contradiction, and thus not a satisfiable formula.

Exercise 2

Exercise 2, part 2. Explanations

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

- For Bi/B, suppose that Bi is irreflexive and B is reflexive. By irreflexivity, it is not the case that xBix. By reflexivity, it is the case that xBx. Being Bi the inverse of B, it is the case that the relation Bi holds between the opposite instances in the relation B, which in this case are both x. That is, xBix. But this contradicts the irreflexivity of Bi.

-  For Bi/Bi, see Exercise 1
  

- Symm/Asymm

![image](https://github.com/user-attachments/assets/04f01e22-a5bc-4e12-bb6a-af93eb7274fa)

A/A:
If A is symmetric, xAy implies yAx. If A is asymmetric, xAy implies ¬(y A x). Both cannot hold simultaneously, causing a contradiction.

A/Ai:
If A is symmetric, xAy implies yAx. For Ai, xAiy implies yAix. Asymmetry of A would conflict with symmetry of Ai. Hence, inconsistency (X).

Ai/A:
If Ai is symmetric implies xAi and yAix, but since Ai​ is the inverse of A (which is asymmetric), this creates a contradiction where xAy forbids yAx. Symmetry and asymmetry cannot coexist for inverse properties.

Ai/Ai:
same as A/A

B/A:
If A is symmetric or asymmetric, B must align with these characteristics due to its sub-property status

B/Ai
If B, inverse of A, is symmetric it means that yAx and xAy both hold. This contradicts Ai´s asymmetry, where xAiy forbids yAix. making it impossible for B to be symmetric and Ai asymmetric.

B/B:
same as A/A

B/Bi:
Bi as the inverse of B can conflict if B is symmetric or asymmetric. The inverse relationship can cause contradictions with symmetry or asymmetry (X).

B/Ai:
If xAy implies yAx (symmetry) or ¬(yAx) (asymmetry), then B as a sub-property of A and Ai​ as its inverse can conflict because xBy and xAi​y may not align due to the inverse relationship (X).

Bi/Bi:
same as A/A


- Trans/Asymm

- <img width="639" alt="image" src="https://github.com/user-attachments/assets/f713b95b-ed69-413e-bc04-1580acf8bb98">

A/A:
See exercise 1

- For A/Ai, suppose that A is transitive and Ai is asymmetric. Being Ai the inverse of A, it is the case that the relation A holds between the opposite instances in the relation Ai. But this creates a complex role chain (see exercise 1).
  
- For Ai/A, suppose that Ai is transitive and A is asymmetric. Being A the inverse of Ai, it is the case that the relation Ai holds between the opposite instances in the relation A. But this creates a complex role chain (see exercise 1).
  
- For Ai/Ai, see Exercise 1
  
- For B/A, suppose that B is transitive and A is asymmetric. Being B a subproperty of A, xBy implies xAy. But this creates a complex role chain (see exercise 1).
  
-  For B/B, see Exercise 1

- For B/Bi, suppose that B is transitive and Bi is asymmetric. Being Bi the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi. But this creates a complex role chain (see exercise 1).

- For Bi/A, suppose that Bi is transitive and A is asymmetric. Being Bi the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi. Being B a subproperty of A, xBy implies xAy. But this creates a complex role chain (see exercise 1).

- For Bi, Ai, suppose that Bi is transitive and Ai is asymmetric. Being Bi the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi. Being B a subproperty of A, xBy implies xAy. Being A the inverse of Ai, it is the case that the relation Ai holds between the opposite instances in the relation A. But this creates a complex role chain (see exercise 1).

-  For Bi/Bi, see Exercise 1


- Reflexivity/Asymmetry

<img width="643" alt="image" src="https://github.com/user-attachments/assets/cf5ae51e-1d23-4001-a15a-aa67e25e137c">


- For A/A, Ai/Ai, B/B, Bi/Bi: see Exercise 1

- A/Ai: suppose that A is reflexive and Ai is asymmetric. By reflexivity, xAx. Since Ai is inverse A, xAix also holds.
However, because of asymmetry, xAix should not hold.   

- A/B: OK

- A/Bi: Ok

- Ai/A: suppose that Ai is reflexive and A is asymmetric. By reflexivity, xAix. Since A is inverse Ai, xAix also holds.
However, because of asymmetricity, xAx should not hold.
    
- Ai/B: Ok
  
- Ai/Bi: Ok
    
- B/Bi: suppose that B is reflexive and Bi is asymmetric. By reflexivity, xBx. Since Bi is inverse B, xBix also holds.
However, because of asymmetricity, if xBiy, then it is not the case that yBix.

- B/Ai

- Bi/A

- Bi/Ai

- B/A
