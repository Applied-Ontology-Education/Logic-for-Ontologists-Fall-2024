Part I

|        | Funct. | iFunct. | Trans. | Symm. | Asymm. | Ref. | Irref. |
|--------|--------|---------|--------|-------|--------|------|--------|
| **Funct.**   | -      | OK      | X<sup>NS</sup>    | OK    | OK     | OK   | OK     |
| **iFunct.**  | OK     | -       | X<sup>NS</sup>    | OK    | OK     | OK   | OK     |
| **Trans.**   | X<sup>NS</sup>    | X<sup>NS</sup>     | -      | OK    | X<sup>NS</sup>    | OK   | X<sup>NS</sup>    |
| **Symm.**    | OK     | OK      | OK     | -     | X<sup>UNSAT</sup> | OK   | OK     |
| **Asymm.**   | OK     | OK      | X<sup>NS</sup>    | X<sup>UNSAT</sup>| -      | X<sup>UNSAT</sup>| OK    |
| **Ref.**     | OK     | OK      | OK     | OK    | X<sup>UNSAT</sup> | -    | X<sup>UNSAT</sup> |
| **Irref.**   | OK     | OK      | X<sup>NS</sup>    | OK    | OK     | X<sup>UNSAT</sup>| -      |

Notation Key:

X<sup>NS</sup> stands for or "Not Satisfiable". It indicates that the property in the row is not satisfied or cannot coexist with the property in the column. 
For example, if the cell for Transitivity and Functionality shows X<sup>NS</sup>, it means that a relation cannot be both transitive and functional simultaneously.

X<sup>UNSAT</sup> stands for "Unsatisfiable." It signifies that the properties in question cannot coexist or are contradictory. 
For instance, if the cell for Symmetry and Asymmetry shows X<sup>UNSAT</sup>, it indicates that no relation can be both symmetric and asymmetric at the same time.

Transitivity & Functionality (NS)
If R is functional, it means that each element can only be related to one other element. So if xRy, x cannot be related to any other element, like z.
If R is transitive, it allows for more relationships. For example, if xRy and yRz, then xRy. But this creates a problem: if R is also functional, then x can only be related to one element, and having x related to both y and z would violate the functional rule. 

Transitivity & Inverse Functionality (NS)
Transitivity means that if xRy and yRz, then xRz 
Inverse functionality means that if x and z are both related to y, then x and z must be the same object. 
xRy and yRz implies x=z
These two properties cannot coexist because transitivity implies distinct relationships, while inverse functionality requires the related objects to be identical, leading to a contradiction.

Transitivity & Asymmetry (NS)
A relation R cannot be both transitive and asymmetric. Asymmetry means if xRy, then y cannot be related to x, forbidding reciprocal relationships. 
Transitivity, however, means that if xRy and yRz then xRz. This can lead to contradiction with asymmetry, as asymmetry prohibits such reverse or reciprocal links, making the two properties incompatible.

Transitivity & Irreflexivity (NS)
A relation R cannot be both transitive and irreflexive. 
Irreflexivity means no element can be related to itself, so it is not possible that xRx. 
However, transitivity can lead to self-relations: if xRy and yRx, then xRx, which violates irreflexivity. 
This makes the two properties incompatible.

Reflexivity & Asymmetry (UNSAT)
Reflexivity requires that every element be related to itself, meaning xRx. 
Asymmetry, however, forbids any element from being related to itself, so xRx cannot be in the relation. 
Therefore, a relation cannot satisfy both properties simultaneously.

Asymmetry & Symmetry (UNSAT)
explanation provided by JB

Reflexitivy & Irreflexivity (UNSAT)
Reflexivity requires every element to relate to itself, while irreflexivity prohibits self-relations entirely. 
Therefore, a relation cannot be both reflexive and irreflexive simultaneously.

Exercise 2, part 2. Explanations

- Symm/Asymm

![image](https://github.com/user-attachments/assets/04f01e22-a5bc-4e12-bb6a-af93eb7274fa)

- A/A:

  If A is symmetric, xAy implies yAx.
  If A is asymmetric, xAy implies ¬(y A x).
  Both cannot hold simultaneously, causing a conflict (X).

- Symmetric A / Asymmetric Ai

  If A is symmetric, xAy implies yAx.
  If Ai is asymmetric, xAiy implies ¬(yAix).
  Therefore, this creates a conflict as symmetry and asymmetry cannot coexist.

- Symmetric Ai / Asymmetric A

  If Ai is symmetric, xAiy implies yAix
  If A, being is asymmetric, xAy implies ¬(yAx)
  Since Ai is the inverse of A, the symmetric nature of Ai contradicts the asymmetry of A, as an inverse property         cannot exhibit symmetry while its original property is asymmetric.

- Ai/Ai:

  Same as A/A

- Symmetric B / Asymmetric A

  If B is symmetric xBy implies yBx.
  However, A being asymmetric means xAy implies ¬(yAx).
  Since B is a subproperty of A, the symmetric nature of B contradicts the asymmetry of A.
  
- Symmetric B / Asymmetric Ai

  If B is symmetric, xBy implies yBx
  If Ai, as the inverse of A, is asymmetric and requires that xAiy implies ¬(yAix)
  The symmetry of B and the asymmetry of Ai cannot coexist without contradiction due to the inverse relationship          between A and Ai

- B/B:

  same as A/A

- Symmetric B / Asymmetric Bi:

  If B is symmetric, xBy implies yBx
  If Bi, as the inverse of B, is asymmetric, meaning xBiy implies ¬(yBix).
  The symmetry of B contradicts the asymmetry of Bi, as their inverse relationship requires consistency that cannot       hold simultaneously.
  
- Symmetric Bi / Asymmetric A

  If Bi is symmetric, xBiy implies yBix.
  However, if A is asymmetric, xAy implies ¬(yAx) 
  Since Bi is the inverse of B the symmetric nature of Bi contradicts the asymmetry of A, as an asymmetric property A     cannot have a symmetric inverse Bi.

- Symmetric Bi / Asymmetric Ai

  If Bi is symmetric, then xBiy implies yBix must also hold.
  However, if Ai is asymmetric, then xAiy implies yAix cannot hold.
  Since Bi is the inverse of B its symmetry contradicts the asymmetry of Ai.
  A symmetric inverse cannot exist when its corresponding property is asymmetric.

- Symmetric Bi / Asymmetric B

  if Bi is symmetric, then xBiy implies yBix must also hold.
  However, if B is asymmetric, then xBy implies ¬(yBx).
  Since Bi is the inverse of B, its symmetry contradicts the asymmetry of B; an asymmetric property cannot have a         symmetric inverse.

- Bi/Bi:

  same as A/A

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


<header>
  <h3>Reflexivity/Asymmetry</h3>
</header>

- <b>A/A, Ai/Ai, B/B, Bi/Bi</b>: see Exercise 1

- <b>A/Ai</b>: suppose that A is reflexive and Ai is asymmetric. By reflexivity, xAx. Since Ai is inverse A, xAix also holds.
However, because of asymmetricity, xAix should not hold.   

- <b>A/B</b>: suppose that A is reflexive and B is asymmetric. By reflexivity, xAx. However, since B is a subproperty of A meaning that all the instances of B have to be a part of
instances of A, the same problem that occured with A/A occurs. Therefore, it is not the case that A is reflexive and B is asymmetric.

- <b>A/Bi</b>: suppose that A is reflexive and Bi is asymmetric. By reflexivity, xAx. And since B is a subproperty of A xBx should hold. Since Bi is inverse B, xBix also holds.
However, because of asymmetricity, xBix should not hold.   

- <b>Ai/A</b>: suppose that Ai is reflexive and A is asymmetric. By reflexivity, xAix. Since A is inverse Ai, xAix also holds.
However, because of asymmetricity, xAx should not hold.
    
- <b>Ai/B</b>: suppose that Ai is reflexive and B is asymmetric. By reflexivity, xAix. Since B is a subproperty of A that is inverse Ai, xBx should hold.
However, because of asymmetricity, xBx should not hold.
  
- <b>Ai/Bi</b>: suppose that Ai is reflexive and Bi is asymmetric. The explanation for this error will be the same for A being refelxive and B being asymmetric.
    
- <b>B/Bi</b>: suppose that B is reflexive and Bi is asymmetric. By reflexivity, xBx. Since Bi is inverse B, xBix also holds.
However, because of asymmetricity, if xBiy, then it is not the case that yBix.   


Functionality / Transitivity

![image](https://github.com/user-attachments/assets/94f987df-41cd-4d1c-b278-1c45ad5ba4a3)

1. A/A
If xAy and yAz (transitivity), then xAz must hold.
However, if A is functional, x can only have one y, leading to a conflict because xAz contradicts functionality (X).

3. Transitive A / Functional Ai
If xAy implies yAx (inverse of A as Ai), and xAi​z implies zAi​y, the transitive relationship between A and Ai creates a conflict since A is functional, and x cannot relate to multiple y's (X).

4. Transitive Ai / Functional A
If xAi​y implies yAx (inverse relationship), and yAz implies xAz (transitivity), functionality is violated because x can only have one relationship, but transitivity implies multiple connections for x (X).

5. Ai/Ai
same as A/A

6. Transitive B / Functional A
If xBy (B is a subproperty of A) implies xAy, and yAz holds, then xAz should hold (transitivity).
However, since Bi nherits functionality from A, xAz contradicts the functional nature of A, creating a conflict (X).

8. Transitive B / Functional Ai
If xBy implies xAy, and xAi​z implies zAi​y, the inverse relationship causes a conflict because B inherits transitivity and functionality from A, while Ai creates an inverse that doesn't align with these constraints (X).

9. B/B
same as A/A

10. Transitive B / Functional Bi
If xBy implies yBi​x (inverse), and yBz implies xBz, the combination of B and its inverse Bi creates a conflict because the inverse relationship breaks the functionality of B, as y would relate to multiple instances (X).

11. Transitive Bi / Functional A
If xBi​y implies yAx (inverse), and xAy holds (transitivity), this creates a conflict because Bi is functional, and y can only relate to one instance, but transitivity suggests multiple relations (X).

12. Transitive Bi / Functional Ai
If xBi​y implies yAx, and yAi​z implies xAi​z (transitivity), functionality is violated because y can only relate to one instance, but transitivity requires multiple relationships (X).

13. Transitive Bi / Functional B
If xBi​y implies yBx (inverse), and xBy implies xBz (transitivity), the combination creates a conflict because B's transitivity contradicts Bi's functionality, as y can only relate to one instance (X).

14. Bi/Bi
same as A/A

 <header>
  <h2>Inverse functional, x</h2>
</header>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">Trans</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">iFunct</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ai</td>
<td class="org-left">B</td>
<td class="org-left">Bi</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>
</tbody>
</table>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<header>
  <h3>Inverse functional/Transitivity (Jisoo)</h3>
</header>

- <b>A/A, Ai/Ai, B/B, Bi/Bi</b>: see Exercise 1

- <b>A/Ai</b>: suppose that A is transitive and Ai is inverse functional. This implies that A is functional. However, according to Exercise 1, an object property can't both be transitive and functional because it creates a complex property chain. Therefore, it does not hold that A is transitive and Ai is inverse functional.

- <b>Ai/A</b>: suppose that Ai is transitive and A is inverse functional. This implies that Ai is functional. However, according to Exercise 1, an object property can't both be transitive and functional because it creates a complex property chain. Therefore, it does not hold that Ai is transitive and A is inverse functional.

- <b>B/A</b>: suppose that B is transitive and A is inverse functional. Since B is a subproperty of A, any instance of B should be that of A. However, according to Exercise 1, an object property can't both be transitive and functional because it creates a complex property chain. Therefore, it does not hold that B is transitive and A is inverse functional.

- <b>B/Ai</b>: suppose that B is transitive and Ai is inverse functional. This implies that A is functional. Since B is a subproperty of A, any instance of B should be that of A. However, according to Exercise 1, an object property can't both be transitive and functional because it creates a complex property chain. Therefore, it does not hold that B is transitive and Ai is inverse functional.
    
- <b>B/Bi</b>: suppose that B is transitive and Bi is inverse functional. This implies that B is functional. However, according to Exercise 1, an object property can't both be transitive and functional because it creates a complex property chain. Therefore, it does not hold that B is transitive and Bi is inverse functional.

- <b>Bi/A</b>: suppose that Bi is transitive and A is inverse functional. This implies that Ai is functional. Since Bi is a subproperty of Ai, any instance of B should be that of A. However, according to Exercise 1, an object property can't both be transitive and inverse functional because it creates a complex property chain. Therefore, it does not hold that Bi is transitive and A is inverse functional.
    
- <b>Bi/Ai</b>: suppose that Bi is transitive and Ai is inverse functional. Since Bi is a subproperty of Ai, any instance of Bi should be that of Ai. However, according to Exercise 1, an object property can't both be transitive and inverse functional because it creates a complex property chain. Therefore, it does not hold that Bi is transitive and Ai is inverse functional.

- <b>Bi/B</b>: suppose that Bi is transitive and B is inverse functional. This implies that Bi is functional. However, according to Exercise 1, an object property can't both be transitive and functional because it creates a complex property chain. Therefore, it does not hold that Bi is transitive and B is inverse functional. 

