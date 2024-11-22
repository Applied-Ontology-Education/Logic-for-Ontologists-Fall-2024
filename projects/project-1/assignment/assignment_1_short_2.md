
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
  
- For A/Ai, suppose that A is irreflexive and Ai is reflexive. By irreflexivity, it is not the case that xAx. By reflexivity, it is the case that xAix. Since Ai is the inverse of A, xAx implies xAix.  But this contradicts the irreflexivity of A.
  
- For Ai/A, suppose that Ai is irreflexive and A is reflexive. By irreflexivity, it is not the case that xAix. By reflexivity, it is the case that xAx.Since Ai is the inverse of A, xAx implies xAix. But this contradicts the irreflexivity of Ai.
  
- For Ai/Ai, see Exercise 1
  
- For A/B, suppose that A is irreflexive and B is reflexive. By irreflexivity, it is not the case that xAx. By reflexivity, it is the case that xBx. Being a subproperty of A, B implies that all the couple of entities connected by B are also connected by A. That is, xBx implies xAx. But this contradicts irreflexivity of A.
  
- For Ai/B, suppose that Ai is irreflexive and B is reflexive. By irreflexivity, it is not the case that xAix. By reflexivity, it is the case that xBx. By being the inverse of A, the fact that it is not the case that xAix implies that it is not the case that the entities in the domain and range appear in the opposite range and domain of A. That is, it is not the case that xAx. Being a subproperty of A, B implies that all the couple of entities connected by B are also connected by A. That is, xBx implies xAx. This creates a contradiction with the previous step.
  
- For A/Bi, suppose that A is irreflexive and Bi is reflexive. By irreflexivity, it is not the case that xAx. By reflexivity, it is the case that xBix. Being a subproperty of Ai, Bi implies that all the couple of entities connected by Bi are also connected by Ai. That is, xBix implies xAix. Being A the inverse of Ai, it is the case that the relation A holds between the opposite instances in the relation Ai, which in this case are both x. That is, xAix implies xAx. But this contradicts th irreflexivity of A.
  
- For Ai/Bi, suppose that Ai is irreflexive and that Bi is reflexive. By irreflexivity, it is not the case that xAix. By reflexivity, it is the case that xBix. Since Bi is the inverse of B, xBix implies xBx. Being a subproperty of A, B implies that all the couple of entities connected by B are also connected by A. That is, xBx implies xAx. But this contradicts irreflexivity of A.
  
-  For B/B, see Exercise 1

- For B/Bi, suppose that B is irreflexive and Bi is reflexive. By irreflexivity, it is not the case that xBx. By reflexivity, it is the case that xBix. Being Bi the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi, which in this case are both x. That is, xBx. But this contradicts the irreflexivity of B.

- For Bi/B, suppose that Bi is irreflexive and B is reflexive. By irreflexivity, it is not the case that xBix. By reflexivity, it is the case that xBx. Being Bi the inverse of B, it is the case that the relation Bi holds between the opposite instances in the relation B, which in this case are both x. That is, xBix. But this contradicts the irreflexivity of Bi.

-  For Bi/Bi, see Exercise 1
  

- Symm/Asymm 

![image](https://github.com/user-attachments/assets/04f01e22-a5bc-4e12-bb6a-af93eb7274fa)

A/A:
If A is symmetric, xAy implies yAx. If A is asymmetric, xAy implies ¬(y A x). Both cannot hold simultaneously, causing a contradiction.

Symmetric A / Asymmetric Ai

If A is symmetric, xAy implies yAx. If Ai is asymmetric, xAiy implies ¬(yAix). Therefore, this creates a conflict as symmetry and asymmetry cannot coexist.

Symmetric Ai / Asymmetric A

If Ai is symmetric, xAiy implies yAix If A, being is asymmetric, xAy implies ¬(yAx) Since Ai is the inverse of A, the symmetric nature of Ai contradicts the asymmetry of A, as an inverse property cannot exhibit symmetry while its original property is asymmetric.

Ai/Ai:
same as A/A

Symmetric B / Asymmetric A

If B is symmetric xBy implies yBx. However, A being asymmetric means tht xAy implies ¬(yAx). Since B is a subproperty of A, the symmetric nature of B contradicts the asymmetry of A.

Symmetric B / Asymmetric Ai

If B is symmetric, xBy implies yBx If Ai, as the inverse of A, is asymmetric and requires that xAiy implies ¬(yAix) The symmetry of B and the asymmetry of Ai cannot coexist without contradiction due to the inverse relationship between A and Ai

B/B:
same as A/A

Symmetric B / Asymmetric Bi:

If B is symmetric, xBy implies yBx. If Bi, as the inverse of B, is asymmetric, meaning xBiy implies ¬(yBix). The symmetry of B contradicts the asymmetry of Bi.

Symmetric Bi / Asymmetric A

If Bi is symmetric, xBiy implies yBix. However, if A is asymmetric, xAy implies ¬(yAx) Since Bi is the inverse of B the symmetric nature of Bi contradicts the asymmetry of A, as an asymmetric property A cannot have a symmetric inverse Bi.

Symmetric Bi / Asymmetric Ai

If Bi is symmetric, then xBiy implies yBix must also hold. However, if Ai is asymmetric, then xAiy implies yAix cannot hold. Since Bi is the inverse of B its symmetry contradicts the asymmetry of Ai. A symmetric inverse cannot exist when its corresponding property is asymmetric.

Symmetric Bi / Asymmetric B

if Bi is symmetric, then xBiy implies yBix must also hold. However, if B is asymmetric, then xBy implies ¬(yBx). Since Bi is the inverse of B, its symmetry contradicts the asymmetry of B; an asymmetric property cannot have a symmetric inverse.


Bi/Bi:
same as A/A


- Functionality/Transitivity 
  
![image](https://github.com/user-attachments/assets/5da454fa-a86b-4a11-8ed2-d1921b823846)


  A/A produce a complex role (see exercise 1)

  Transitive A / Functional Ai: Given that Ai is the inverse of A, and yAix, this implies that xAy. Given that Ai is functional, A becomes inverse functional. This makes A both transitive and inverse functional, which creates a non-simple property according to exercise 1.

  Transitive Ai / Functional A: Given that Ai is the inverse of A, and yAx, this implies that xAiy. Given that A is functional, Ai becomes inverse functional. This makes Ai both transitive and inverse functional, which creates a non-simple property according to exercise 1.

  Ai/Ai same as A/A

  Transitive B / Functional A: Given that A is a subproperty of B, and that xBy, this implies that xAy. Given that B is transitive, A becomes transitive. This makes A both functional and transitive, which creates a non-simple property according to exercise 1.

  Transitive B / Functional Ai: Transitive B / Functional A: Given that A is a subproperty of B, and that xBy, this implies that xAy. Given that B is transitive, A becomes transitive. Given that Ai is inverse of A, this makes A inverse functional. This makes A both inverse functional and transitive, which creates a non-simple property according to exercise 1.

  B/B same as A/A

  Transitive B / Functional Bi: Given that Bi is the inverse of B, and yBix, this implies that xBy. Given that Bi is functional, B becomes inverse functional. This makes B both transitive and inverse functional, which creates a non-simple property according to exercise 1.

  Transitive Bi / Functional A: Given that Bi is the inverse of B, and yBix, this implies that xBy. Given that A is a subproperty of B, and that xBy, this implies that xAy. Given that B is transitive, A becomes transitive. This makes A both functional and transitive, which creates a non-simple property according to exercise 1.

  Transitive Bi / Functional Ai: Given that Ai is a subproperty of Bi, and that xBiy, this implies that xAiy. Given that Bi is transitive, Ai becomes transitive. This makes Ai both functional and transitive, which creates a non-simple property according to exercise 1.

  Transitive Bi / Functional B: Given that Bi is the inverse of B, and yBix, this implies that xBy. Given that Bi is functional, B becomes inverse functional. This makes B both transitive and inverse functional, which creates a non-simple property according to exercise 1.

 Bi/Bi same as A/A


- Trans/Asymm 

- <img width="639" alt="image" src="https://github.com/user-attachments/assets/f713b95b-ed69-413e-bc04-1580acf8bb98">

A/A:
See exercise 1

- For A/Ai, suppose that A is transitive and Ai is asymmetric. Ai being the inverse of A, it is the case that the relation A holds between the opposite instances in the relation Ai. But this creates a complex role (see exercise 1).
  
- For Ai/A, suppose that Ai is transitive and A is asymmetric. A being the inverse of Ai, it is the case that the relation Ai holds between the opposite instances in the relation A. But this creates a complex role (see exercise 1).
  
- For Ai/Ai, see Exercise 1

- For A/A, see Exercise 1
  
- For B/A, suppose that B is transitive and A is asymmetric. B being a subproperty of A, xBy implies xAy. But this creates a complex role (see exercise 1).
  
-  For B/B, see Exercise 1

- For B/Bi, suppose that B is transitive and Bi is asymmetric. Bi being the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi. But this creates a complex role (see exercise 1).

- For Bi/A, suppose that Bi is transitive and A is asymmetric. Bi being the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi. Being B a subproperty of A, xBy implies xAy. But this creates a complex role (see exercise 1).

- For Bi/Ai, suppose that Bi is transitive and Ai is asymmetric. Being Bi the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi. B being a subproperty of A, xBy implies xAy. A being the inverse of Ai, it is the case that the relation Ai holds between the opposite instances in the relation A. But this creates a complex role (see exercise 1).

-  For Bi/Bi, see Exercise 1

- For B/Ai, suppose that B is transitive and Ai is asymmetric. B being a subproperty of A, xBy implies xAy. Being A the inverse of Ai, it is the case that the relation Ai holds between the opposite instances in the relation A. But this creates a complex role (see exercise 1).

- For Bi/B, suppose that Bi is transitive and B is asymmetric. Bi being the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi. But this creates a complex role (see exercise 1).


- Reflexivity/Asymmetry 

<img width="643" alt="image" src="https://github.com/user-attachments/assets/cf5ae51e-1d23-4001-a15a-aa67e25e137c">


- For A/A, Ai/Ai, B/B, Bi/Bi: see Exercise 1

- A/Ai: Suppose that A is asymmetric and Ai is reflexive. By reflexivity, xAix. Since A is inverse Ai, xAx also holds. However, because of asymmetry, xAx should not hold.  

- A/B: Suppose that A is asymmetric and B is reflexive. By reflexivity, xBx. However, since B is a subproperty of A meaning that all the instances of B have to be a part of instances of A, the same problem that occured with A/A occurs. In other words, because of asymmetry, xAx should not hold. Therefore, it is not the case that A is asymmetric and B is reflexive.

- A/Bi: Suppose that A is asymmetric and Bi is reflexive. By reflexivity, xBix. And since Bi is a subproperty of Ai meaning that all the instances of Bi have to be a part of instances of Ai, the same problem that occured with A/Ai occurs. In other words, because of asymmetry, xAx should not hold. Therefore, it is not the case that A is asymmetric and Bi is reflexive.

- Ai/A: Suppose that Ai is asymmetric and A is reflexive. By reflexivity, xAx. Since A is inverse Ai, xAix also holds. However, because of asymmetry, xAix should not hold.
    
- Ai/B: Suppose that Ai is asymmetric and B is reflexive. By reflexivity, xBx. Since B is a subproperty of A that is inverse of Ai, xAix should hold. However, because of asymmetry, xAix should not hold.
  
- Ai/Bi: Suppose that Ai is asymmetric and Bi is reflexive. By reflexivity, xBix. However, since Bi is a subproperty of Ai meaning that all the instances of Bi have to be a part of instances of Ai, the same problem that occured with A/Ai occurs. Therefore, it is not the case that Ai is asymmetric and Bi is reflexive.
    
- B/Bi: Suppose that B is asymmetric and Bi is reflexive. By reflexivity, xBix. Since Bi is inverse B, xBx also holds. However, because of asymmetry, xBx does not hold. Therefore, it does not hold that B is asymmetric and Bi is reflexive.

- Bi/B: Suppose that Bi is asymmetric and B is reflexive. By reflexivity, xBx. Since Bi is inverse B, xBix also holds. However, because of asymmetry, if xBiy, then it is not the case that yBix.


Inverse Functional/Transitive 

![image](https://github.com/user-attachments/assets/1670e82a-f623-4396-9c20-84bef8d20f90)


A/Ai: suppose that A is transitive and Ai is inverse functional. This implies that A is functional. However, according to Exercise 1, an object property can't both be transitive and functional because it creates a complex property. Therefore, it does not hold that A is transitive and Ai is inverse functional.

Ai/A: suppose that Ai is transitive and A is inverse functional. This implies that Ai is functional. However, according to Exercise 1, an object property can't both be transitive and functional because it creates a complex property. Therefore, it does not hold that Ai is transitive and A is inverse functional.

B/A: suppose that B is transitive and A is inverse functional. Since B is a subproperty of A, any instance of B should be that of A. However, according to Exercise 1, an object property can't both be transitive and functional because it creates a complex property. Therefore, it does not hold that B is transitive and A is inverse functional.

B/Ai: suppose that B is transitive and Ai is inverse functional. This implies that A is functional. Since B is a subproperty of A, any instance of B should be that of A. However, according to Exercise 1, an object property can't both be transitive and functional because it creates a complex property. Therefore, it does not hold that B is transitive and Ai is inverse functional.

B/Bi: suppose that B is transitive and Bi is inverse functional. This implies that B is functional. However, according to Exercise 1, an object property can't both be transitive and functional because it creates a complex property. Therefore, it does not hold that B is transitive and Bi is inverse functional.

Bi/A: suppose that Bi is transitive and A is inverse functional. This implies that Ai is functional. Since Bi is a subproperty of Ai, any instance of B should be that of A. However, according to Exercise 1, an object property can't both be transitive and inverse functional because it creates a complex property. Therefore, it does not hold that Bi is transitive and A is inverse functional.

Bi/Ai: suppose that Bi is transitive and Ai is inverse functional. Since Bi is a subproperty of Ai, any instance of Bi should be that of Ai. However, according to Exercise 1, an object property can't both be transitive and inverse functional because it creates a complex property. Therefore, it does not hold that Bi is transitive and Ai is inverse functional.

Bi/B: suppose that Bi is transitive and B is inverse functional. This implies that Bi is functional. However, according to Exercise 1, an object property can't both be transitive and functional because it creates a complex property. Therefore, it does not hold that Bi is transitive and B is inverse functional.



Transitive-Irreflexive 

![image](https://github.com/user-attachments/assets/97d1d056-1c8d-4393-92ad-f05ac96eaaba)

  A/A, Ai/Ai, B/B, Bi/Bi: see Exercise 1

  A/Ai: Suppose that A is transitive and Ai is irreflexive. Ai being the inverse of A, xAiy implies that yAx. In order to check irreflexivity of A, a reasoner has to loop over A each time it needs to also check for transitivity. This creates a complex role.
  
  Ai/A: Suppose that Ai is transitive and A is irreflexive. Ai being the inverse of A, xAiy implies that yAx. In order to check irreflexivity of A, a reasoner has to loop over A each time it needs to also check for transitivity. This creates a complex role.

  B/A: Suppose that B is transitive and A is irreflexive. B being a subclass of A implies that A is also transitive. As seen in ex 1, this creates a complex role.

  B/Ai: Suppose that B is transitive and Ai is irreflexive. B being a subclass of A implies that A is also transitive. Ai being the inverse of A, xAiy implies that yAx. In order to check for irreflexivy and transitivity of this relation, a reasoner loops over because of the presence of a complex role.

  B/Bi: Suppose that B is transitive and Bi is irreflexive. Bi being the inverse of B, xBiy implies that yBx. In order to check irreflexivity of B, a reasoner has to loop over B each time it needs to also check for transitivity. This creates a complex role.

  Bi/A: Suppose that Bi is transitive and A is irreflexive. Bi being the inverse of B, xBiy implies that yBx. B being a subclass of A implies yAx. In order to check irreflexivity of A, a reasoner has to loop over A each time it needs to also check for transitivity. This creates a complex role.

  Bi/Ai: Suppose that Bi is transitive and Ai is irreflexive. Bi being a subclass of A implies that Ai is also transitive. As seen in ex 1, this creates a complex role.
  
  Bi/B: Suppose that Bi is transitive and B is irreflexive. Bi being the inverse of B, xBiy implies that yBx. In order to check irreflexivity of B, a reasoner has to loop over B each time it needs to also check for transitivity. This creates a complex role.

