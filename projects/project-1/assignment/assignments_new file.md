<header>
  <h1>Assignment 1</h1>
</header>

<p><b>Jisoo Seo</b></p>

<p>The purpose of the assignment is to explain the two kinds of errors that occur when an object property R is attributed different pairs of role constraints. 
  This is summarized in the table 1 below.</p>

|        | Funct. | iFunct. | Trans. | Symm. | Asymm. | Ref. | Irref. |
|--------|--------|---------|--------|-------|--------|------|--------|
| **Funct.**   | -      | OK      | X<sup>NS</sup>    | OK    | OK     | OK   | OK     |
| **iFunct.**  | OK     | -       | X<sup>NS</sup>    | OK    | OK     | OK   | OK     |
| **Trans.**   | X<sup>NS</sup>    | X<sup>NS</sup>     | -      | OK    | X<sup>NS</sup>    | OK   | X<sup>NS</sup>    |
| **Symm.**    | OK     | OK      | OK     | -     | X<sup>UNSAT</sup> | OK   | OK     |
| **Asymm.**   | OK     | OK      | X<sup>NS</sup>    | X<sup>UNSAT</sup>| -      | X<sup>UNSAT</sup>| OK    |
| **Ref.**     | OK     | OK      | OK     | OK    | X<sup>UNSAT</sup> | -    | X<sup>UNSAT</sup> |
| **Irref.**   | OK     | OK      | X<sup>NS</sup>    | OK    | OK     | X<sup>UNSAT</sup>| -      |

<h2>Error type 1: X<sup>NS</sup></h2>
<p>This error occurs when Protege reasoner can not decide which logical model to follow. "NS" stands for "not simple."</p>

1. Transitivity/Functionality: R can't be contrainted by both transitivity and functionality. Because of transitivity when we suppose xRy and yRz, then xRz. This  leads to the possibility of multiple targets for a single source, which conflicts with the one-to-one constraint of functionality. In other words, functionality restricts an individual to being related to exactly one individual via the property. So, if xPy, then x cannot be related to any other individual via  P.

2. transitivity/Inverse Functionality: R can't be contrainted by both transitivity and inverse functionality. Because of transitivity when we suppose xRy and yRz, then xRz. This  leads to the possibility of multiple targets for a single source, which conflicts with the one-to-one constraint of functionality. In other words, inverse funtionality restricts an individual to being related to exactly one individual via the property. So, if xPy, then x cannot be related to any other individual via  P.

3. transitivity/Asymmetry: R can't be contrainted by both transitivity and asymmetry. Because of transitivity, when we suppose xRy and yRz, then xRz. But if there is a possibility that zRx results through further transitive chains, this could violate the asummetry constraint, which prohinits zRx. Therefore, it does not hold that R is contrainted by both transitivity and asymmetry.

<h2>Error type 2: X<sup>UNSAT</sup></h2>

<p>This error occurs when the object property R is constrained in a way that nothing satisfies R. In other words, when the two role constraints are logically contradictory, 
  no instance can satisfy the contradiction, thus the error. "UNSAT" stands for "unsatisfiable."</p>

1. Symmetry/Asymmetry: R can't both be contrainted by symmetry and asymmetry. This is contradictoty. Because of symmetry, if xRy, then yRx. However, because of asymmetry, it is not the case that yRx. Therefore, R can't be constrained by both symmetry and asymmetry.

2. Reflexivity/Asymmetry: R can't both be constrained by reflexive and asymmetry. This is contradictoty. Because of reflexivity, xRx. However, because of asymmetry, it is not the case that xRx. Therefore, R can't be constrained by both reflexive and asymmetry.

3. Reflexivity/Irrflexivity: R can't both be constrained by reflexive and irreflextivity. This is contradictoty. Because of reflexivity, xRx. However, because of irreflexivity, it is not the case that xRx. Therefore, R can't be constrained by both reflexive and irreflextivity.

<header>
  <h1>Assignment 2</h1>
</header>

<p><b>Jisoo Seo, Giacomo De Colle, Elena Milivinti, Sean Kindya</b></p>

<p>The purpose of the assignment is to explain the errors that occur when different pairs of role constraints are attributed to different object properties that bear 
either Sub Property and/or Inverse relation.</p>

<p>For this assignment, we created tables that represent the two role constraints and object properties A,B, Ai, and Bi where B is a subproperty of A and Ai has an inverse relation to A.
I have only added tables that have errors in them and are not redundant.</p>

<header>
  <h2>Functional, x</h2>
</header>


<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
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
<td class="org-left">Funct</td>
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

 <header>
  <h3>Functional/Transitivity (Elena)</h>
</header>

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


<header>
  <h2>Transitive, x</h2>
</header>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">Asymm</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Trans</td>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>
</tbody>
</table>

 <header>
  <h3>Transitivity/Aysmmetry (Giacomo)</h3>
</header>

A/A:
See exercise 1

- For A/Ai, suppose that A is transitive and Ai is asymmetric. Ai being the inverse of A, it is the case that the relation A holds between the opposite instances in the relation Ai. But this creates a complex role chain (see exercise 1).
  
- For Ai/A, suppose that Ai is transitive and A is asymmetric. A being the inverse of Ai, it is the case that the relation Ai holds between the opposite instances in the relation A. But this creates a complex role chain (see exercise 1).
  
- For Ai/Ai, see Exercise 1

- For A/A, see Exercise 1
  
- For B/A, suppose that B is transitive and A is asymmetric. B being a subproperty of A, xBy implies xAy. But this creates a complex role chain (see exercise 1).
  
-  For B/B, see Exercise 1

- For B/Bi, suppose that B is transitive and Bi is asymmetric. Bi being the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi. But this creates a complex role chain (see exercise 1).

- For Bi/A, suppose that Bi is transitive and A is asymmetric. Bi being the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi. Being B a subproperty of A, xBy implies xAy. But this creates a complex role chain (see exercise 1).

- For Bi/Ai, suppose that Bi is transitive and Ai is asymmetric. Being Bi the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi. B being a subproperty of A, xBy implies xAy. A being the inverse of Ai, it is the case that the relation Ai holds between the opposite instances in the relation A. But this creates a complex role chain (see exercise 1).

-  For Bi/Bi, see Exercise 1

- For B/Ai, suppose that B is transitive and Ai is asymmetric. B being a subproperty of A, xBy implies xAy. Being A the inverse of Ai, it is the case that the relation Ai holds between the opposite instances in the relation A. But this creates a complex role chain (see exercise 1).

- For Bi/B, suppose that Bi is transitive and B is asymmetric. Bi being the inverse of B, it is the case that the relation B holds between the opposite instances in the relation Bi. But this creates a complex role chain (see exercise 1).

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">Irr</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Trans</td>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>
</tbody>
</table>

<header>
  <h3>Transitivity/Irreflexivity (Jisoo)</h3>
</header>

- <b>A/A, Ai/Ai, B/B, Bi/Bi</b>: see Exercise 1

- <b>A/Ai</b>: Suppose that A is transitive and Ai is irreflexive. Ai being the inverse of A, xAiy implies that yAx. In order to check irreflexivity of A, a reasoner has to loop over A each time it needs to also check for transitivity. This creates a complex role.
  
- <b>Ai/A</b>: Suppose that Ai is transitive and A is irreflexive. Ai being the inverse of A, xAiy implies that yAx. In order to check irreflexivity of A, a reasoner has to loop over A each time it needs to also check for transitivity. This creates a complex role.

- <b>B/A</b>: Suppose that B is transitive and A is irreflexive. B being a subclass of A implies that A is also transitive. As seen in ex 1, this creates a complex role.
  
- <b>B/Ai</b>: Suppose that B is transitive and Ai is irreflexive. B being a subclass of A implies that A is also transitive. Ai being the inverse of A, xAiy implies that yAx. In order to check for irreflexivy and transitivity of this relation, a reasoner loops over because of the presence of a complex role.

- <b>B/Bi</b>: Suppose that B is transitive and Bi is irreflexive. This means that if xBy and yBx hold, xBx holds. It also means that xBix should hold. However, Bi is irreflextive so xBix doesn't hold. Therefore, it does not hold that B is transitive and Bi is irreflexive.
  
- <b>Bi/A</b>: SSuppose that B is transitive and Bi is irreflexive. Bi being the inverse of B, xBiy implies that yBx. In order to check irreflexivity of B, a reasoner has to loop over B each time it needs to also check for transitivity. This creates a complex role.

- <b>Bi/Ai</b>: Suppose that Bi is transitive and Ai is irreflexive. Bi being a subclass of A implies that Ai is also transitive. As seen in ex 1, this creates a complex role.

- <b>Bi/B</b>: Suppose that Bi is transitive and B is irreflexive. Bi being the inverse of B, xBiy implies that yBx. In order to check irreflexivity of B, a reasoner has to loop over B each time it needs to also check for transitivity. This creates a complex role.

<a id="orgd02ec3b"></a>

<header>
  <h2>Symmetry, x</h2>
</header>
<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">



<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">Asymm</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Symm</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ai</td>
<td class="org-left">B</td>
<td class="org-left">Bi</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
<td class="org-left">x</td>
</tr>
</tbody>
</table>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<a id="org9d8084e"></a>

<header>
  <h3>Symmetry/Asymmetry (Elena)</h3>
</header>

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

- Symmetric Bi/ Asymmetric Bi:

  same as A/A

<header>
  <h2>Reflexive, x</h2>
</header>

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">Asymm</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Ref</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ai</td>
<td class="org-left">B</td>
<td class="org-left">Bi</td>
<td class="org-left">&#xa0;</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">OK</td>
<td class="org-left">Ok</td>
<td class="org-left">&#xa0;</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">&#xa0;</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">&#xa0;</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>

<header>
  <h3>Reflexivity/Asymmetry (Jisoo)</h3>
</header>

- <b>A/A, Ai/Ai, B/B, Bi/Bi</b>: see Exercise 1

- <b>A/Ai</b>: Suppose that A is asymmetric and Ai is reflexive. By reflexivity, xAix. Since A is inverse Ai, xAx also holds.
However, because of asymmetry, xAx should not hold.   

- <b>A/B</b>: Suppose that A is asymmetric and B is reflexive. By reflexivity, xBx. However, since B is a subproperty of A meaning that all the instances of B have to be a part of
instances of A, the same problem that occured with A/A occurs. In other words, because of asymmetry, xAx should not hold. Therefore, it is not the case that A is asymmetric and B is reflexive.

- <b>A/Bi</b>: Suppose that A is asymmetric and Bi is reflexive. By reflexivity, xBix. And since Bi is a subproperty of Ai meaning that all the instances of Bi have to be a part of
instances of Ai, the same problem that occured with A/Ai occurs. In other words, because of asymmetry, xAx should not hold. Therefore, it is not the case that A is asymmetric and Bi is reflexive.

- <b>Ai/A</b>: Suppose that Ai is asymmetric and A is reflexive. By reflexivity, xAx. Since A is inverse Ai, xAix also holds.
However, because of asymmetry, xAix should not hold.
    
- <b>Ai/B</b>: Suppose that Ai is asymmetric and B is reflexive. By reflexivity, xBx. Since B is a subproperty of A that is inverse Ai, xAix should hold.
However, because of asymmetry, xAix should not hold.
  
- <b>Ai/Bi</b>: Suppose that Ai is asymmetric and Bi is reflexive. By reflexivity, xBix. However, since Bi is a subproperty of Ai meaning that all the instances of Bi have to be a part of
instances of Ai, the same problem that occured with A/A occurs. Therefore, it is not the case that Ai is asymmetric and Bi is reflexive.
    
- <b>B/Bi</b>: Suppose that B is asymmetric and Bi is reflexive. By reflexivity, xBix. Since Bi is inverse B, xBx also holds.
However, because of asymmetry, xBx does not hold. Therefore, it does not hold that B is asymmetric and Bi is reflexive.

- <b>Bi/B</b>: Suppose that Bi is asymmetric and B is reflexive. By reflexivity, xBx. Since Bi is inverse B, xBix also holds.
However, because of asymmetry, if xBiy, then it is not the case that yBix.  

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
  
<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">Irr</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Ref</td>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>
</tbody>
</table>


<a id="orgceec1a2"></a>

<header>
  <h3>Reflexivity/Irreflexivity (Giacomo)</h3>
</header>

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

