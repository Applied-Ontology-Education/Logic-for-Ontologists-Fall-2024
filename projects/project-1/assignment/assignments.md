<header>
  <h1>Assignment 1</h1>
</header>

<p>Jisoo Seo</p>

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
<p>This error occurs when Protege reasoner can not decide which logical model to follow.</p>

1. Transivity/Functionality: R can't both be contrainted by both transivity and functionality. Because of transivity when we suppose xRy and yRz, then xRz. This creates a multiple relation.
However, funtionality restricts an individual to being related to exactly one individual via the property. So, if xPy, then x cannot be related to any other individual via  P.

2. Transivity/Inverse Functionality: R can't both be contrainted by both transivity and inverse functionality. Because of transivity when we suppose xRy and yRz, then xRz. This creates a multiple relation.
However, inverse funtionality restricts an individual to being related to exactly one individual via the property. So, if xPy, then x cannot be related to any other individual via  P.

3. Transivity/Asymmetry: R can't both be contrainted by both transivity and asymmetry. Because of transivity when we suppose xRy and yRz, then xRz.

<h2>Error type 2: X<sup>UNSAT</sup></h2>

<p>This error occurs when the object property R is constrained in a way that nothing satisfies R. In other words, when the two role constraints are logically contradictory, 
  no instance can satisfy the contradiction, thus the error.</p>

1. Symmetry/Asymmetry: R can't both be contrainted by symmetry and asymmetry. This is contradictoty. Because of symmetry, if xRy, then yRx. However, because of asymmetry, it is not the case that yRx. 
    Therefore, R can't be constrained by both symmetry and asymmetry.

2. Refelxivity/Aymmetry: R can't both be constrained by reflexive and asymmetry. This is contradictoty. Because of reflexivity, xRx. However, because of asymmetry, it is not the case that xRx. 
    Therefore, R can't be constrained by both reflexive and asymmetry.

3. Refelxivity/Irrflexivity: R can't both be constrained by reflexive and irreflextivity. This is contradictoty. Because of reflexivity, xRx. However, because of irreflexivity, it is not the case that xRx. 
    Therefore, R can't be constrained by both reflexive and irreflextivity.

<header>
  <h1>Assignment 2</h1>
</header>

<p>Jisoo Seo, Giacomo De Colle, Elena Militivi, Sean Kindya</p>

<p>The purpose of the assignment is to explain the errors that occur when different pairs of role constraints are attributed to different object properties that bear 
either SubObjectiveProperty and/or Inverse relation.</p>

<p>For this assignment, we created tables that represent the two role constraints and object properties A,B, Ai, and Bi where B is a subproperty of A and Ai has an inverse relation to A.
I have only added tables that have errors in them and those that are not redundant.</p>

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
<th scope="col" class="org-left">7</th>
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


<a id="orga2c05d9"></a>


 <header>
  <h2>Inverse functional, x</h2>
</header>

Jisoo

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">

<thead>
<tr>
<th scope="col" class="org-left">3</th>
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
<th scope="col" class="org-left">5</th>
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
<th scope="col" class="org-left">7</th>
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
<th scope="col" class="org-left">5</th>
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
  <h3>Symmetry/Asymmetry</h3>
</header>

A/A:
If A is symmetric, xAy implies yAx. If A is asymmetric, xAy implies ¬(y A x). Both cannot hold simultaneously, causing a conflict (X).

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
  <h3>Reflexivity/Asymmetry</h3>
</header>

- <b>A/A, Ai/Ai, B/B, Bi/Bi</b>: see Exercise 1

- <b>A/Ai</b>: suppose that A is asymmetric and Ai is reflexive. By reflexivity, xAix. Since A is inverse Ai, xAx also holds.
However, because of asymmetricity, xAx should not hold.   

- <b>A/B</b>: suppose that A is asymmetric and B is reflexive. By reflexivity, xBx. However, since B is a subproperty of A meaning that all the instances of B have to be a part of
instances of A, the same problem that occured with A/A occurs. Therefore, it is not the case that A is asymmetric and B is reflexive.

- <b>A/Bi</b>: suppose that A is asymmetric and Bi is reflexive. By reflexivity, xBix. And since Bi is a subproperty of Ai meaning that all the instances of Bi have to be a part of
instances of Ai, the same problem that occured with A/Ai occurs. Therefore, it is not the case that A is asymmetric and Bi is reflexive.

- <b>Ai/A</b>: suppose that Ai is asymmetric and A is reflexive. By reflexivity, xAx. Since A is inverse Ai, xAix also holds.
However, because of asymmetricity, xAix should not hold.
    
- <b>Ai/B</b>: suppose that Ai is asymmetric and B is reflexive. By reflexivity, xBx. Since B is a subproperty of A that is inverse Ai, xAix should hold.
However, because of asymmetricity, xAix should not hold.
  
- <b>Ai/Bi</b>: suppose that Ai is asymmetric and Bi is reflexive. The explanation for this error will be the same for A being asymmetric and B being reflexive.
    
- <b>B/Bi</b>: suppose that B is asymmetric and Bi is reflexive. By reflexivity, xBix. Since Bi is inverse B, xBx also holds.
However, because of asymmetricity, xBx does not hold. Therefore, it does not hold that B is asymmetric and Bi is reflexive.

- <b>Bi/B</b>: suppose that Bi is asymmetric and B is reflexive. By reflexivity, xBx. Since Bi is inverse B, xBix also holds.
However, because of asymmetricity, if xBiy, then it is not the case that yBix.  

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
  <h3>Reflexivity/Irreflexivity</h3>
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

