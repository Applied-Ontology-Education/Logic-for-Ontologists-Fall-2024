<header>
  <h1>Assignment 1</h1>
</header>

Part I - Elena Milivinti

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


Part II

# Table of Contents

1.  [Authors](#org96552c2)
2.  [Primary Table](#org2d94bb3)
3.  [Funct, x](#org40f4ebd)
4.  [iFunct, x](#orga2c05d9)
5.  [Trans, x](#org918898a)
6.  [Symm, x](#orgd02ec3b)
7.  [Asym, x](#org9d8084e)
8.  [Ref, x](#org1e4542d)
9.  [Irr, x](#orgceec1a2)


<a id="org96552c2"></a>

# Authors

Giacomo, Jisoo, Elena, Sean


<a id="org2d94bb3"></a>

# Primary Table

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-right">Funct</th>
<th scope="col" class="org-right">Ifunct</th>
<th scope="col" class="org-right">Trans</th>
<th scope="col" class="org-right">Symm</th>
<th scope="col" class="org-right">Asymm</th>
<th scope="col" class="org-left">Ref</th>
<th scope="col" class="org-left">Irref</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Funct</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-right">1</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>

<tr>
<td class="org-left">iFunct</td>
<td class="org-right">2</td>
<td class="org-right">2</td>
<td class="org-right">2</td>
<td class="org-right">2</td>
<td class="org-right">2</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>

<tr>
<td class="org-left">Trans</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">3</td>
<td class="org-right">3</td>
<td class="org-right">3</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>

<tr>
<td class="org-left">Symm</td>
<td class="org-right">4</td>
<td class="org-right">4</td>
<td class="org-right">4</td>
<td class="org-right">4</td>
<td class="org-right">4</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>

<tr>
<td class="org-left">Asymm</td>
<td class="org-right">5</td>
<td class="org-right">5</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">EM</td>
<td class="org-right">5</td>
<td class="org-left">X</td>
<td class="org-left">X</td>
</tr>

<tr>
<td class="org-left">Ref</td>
<td class="org-right">6</td>
<td class="org-right">6</td>
<td class="org-right">6</td>
<td class="org-right">6</td>
<td class="org-right">JS</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">X</td>
</tr>

<tr>
<td class="org-left">Irref</td>
<td class="org-right">7</td>
<td class="org-right">7</td>
<td class="org-right">&#xa0;</td>
<td class="org-right">7</td>
<td class="org-right">7</td>
<td class="org-left">GDC</td>
<td class="org-left">7</td>
</tr>
</tbody>
</table>


<a id="org40f4ebd"></a>

# Funct, x

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
<th scope="col" class="org-left">1</th>
<th scope="col" class="org-left">Funct</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">2</th>
<th scope="col" class="org-left">iFunct</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">3</th>
<th scope="col" class="org-left">Symm</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">4</th>
<th scope="col" class="org-left">Asymm</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">5</th>
<th scope="col" class="org-left">Ref</th>
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
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
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
<th scope="col" class="org-left">6</th>
<th scope="col" class="org-left">Irref.</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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

# iFunct, x

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
<th scope="col" class="org-left">1</th>
<th scope="col" class="org-left">Funct</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">2</th>
<th scope="col" class="org-left">iFunct</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">4</th>
<th scope="col" class="org-left">Symm</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">6</th>
<th scope="col" class="org-left">Ref</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">Irref</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>
</tbody>
</table>


<a id="org918898a"></a>

# Trans, x

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
<th scope="col" class="org-left">1</th>
<th scope="col" class="org-left">Func</th>
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
<th scope="col" class="org-left">2</th>
<th scope="col" class="org-left">iFunct</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">4</th>
<th scope="col" class="org-left">Symm</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">6</th>
<th scope="col" class="org-left">Ref</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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

# Symm, x

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
<th scope="col" class="org-left">1</th>
<th scope="col" class="org-left">Functional</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">2</th>
<th scope="col" class="org-left">Ifunct</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">6</th>
<th scope="col" class="org-left">Ref</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">Irref</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>
</tbody>
</table>


<a id="org9d8084e"></a>

# Asym, x

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
<th scope="col" class="org-left">1</th>
<th scope="col" class="org-left">Funct</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Asymm</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ai</td>
<td class="org-left">B</td>
<td class="org-left">Bi</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
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
<th scope="col" class="org-left">2</th>
<th scope="col" class="org-left">iFunct</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Asymm</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ai</td>
<td class="org-left">B</td>
<td class="org-left">Bi</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
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
<td class="org-left">Asymm</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ai</td>
<td class="org-left">B</td>
<td class="org-left">Bi</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">OK</td>
<td class="org-left">Ok</td>
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
<th scope="col" class="org-left">Irref</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Asymm</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ai</td>
<td class="org-left">B</td>
<td class="org-left">Bi</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>
</tbody>
</table>


<a id="org1e4542d"></a>

# Ref, x

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
<th scope="col" class="org-left">1</th>
<th scope="col" class="org-left">Funct</th>
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
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
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
<th scope="col" class="org-left">2</th>
<th scope="col" class="org-left">iFunct</th>
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
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">Ok</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">OK</td>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">Ok</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">OK</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
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
<th scope="col" class="org-left">6</th>
<th scope="col" class="org-left">Ref</th>
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
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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

# Irr, x

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
<td class="org-left">Irr</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ai</td>
<td class="org-left">B</td>
<td class="org-left">Bi</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
<td class="org-left">OK</td>
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
<th scope="col" class="org-left">6</th>
<th scope="col" class="org-left">Asymm</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
<th scope="col" class="org-left">&#xa0;</th>
</tr>
</thead>
<tbody>
<tr>
<td class="org-left">Irref</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ai</td>
<td class="org-left">B</td>
<td class="org-left">Bi</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">A</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Ai</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">B</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>

<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Bi</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
<td class="org-left">Ok</td>
</tr>
</tbody>
</table>

Exercise 2, part 2. Explanations

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
  <h3>Symmetry/Asymmetry</h3> (Elena)
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

- Bi/Bi:

  same as A/A

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

(Giacomo)

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
  <h3>Reflexivity/Asymmetry</h3> (Jisoo)
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
  <h3>Functionality/Transitivity </h>
</header>

(Elena)

- A/A
A property A that is both functional and transitive does not lead to a contradiction, but instead forms a non-simple (NS) chain. In such cases, while transitivity allows for a sequence of relations, functionality ensures that each element relates to only one other element in the chain. 

- Transitive A / Functional Ai
Given that Ai​ is the inverse of A, and if yAi​x, this implies that xAy.
Since Ai is functional, meaning each element has exactly one predecessor, A becomes inverse functional. This creates a scenario where A is both inverse functional and functional. As a result, the interaction between A and Ai forms a non-simple property chain, as explored in exercise 1.

- Transitive Ai / Functional A
IF Ai is transitive xAi​y (inverse relation) implies yAx, and for the transitivity of A yAz implies xAz.
Here there is no direct contradiction between transitivity and functionality.
This is because, in this case, y=zy=z, meaning transitivity holds without violating functionality.
Instead of creating a contradiction, these properties form a non-simple (NS) chain, where the functional constraint remains valid, but the relationship chain is more complex.

- Ai/Ai
same as A/A

- Transitive B / Functional A
If xBy (where B is a subproperty of A) implies xAy, and yAz holds, then by transitivity, xAz should hold as well. However, since B inherits functionality from A, the resulting chain where x relates to both y and z violates the functional constraint. This doesn’t create a direct contradiction, but it leads to a non-simple (NS) property chain, as explained in Exercise 1.

- Transitive B / Functional Ai
If xBy (where B is a subproperty of A) implies xAy, and xAiy implies yAix, this creates an inverse functional relationship for Ai.
Instead of generating a direct conflict, this results in a complex property chain where the transitivity of B leads to an inverse relationship, making Ai inverse functional. This creates an extended, non-simple chain rather than a contradiction.

- B/B
same as A/A

- Transitive B / Functional Bi
The combination of B (transitive) and Bi (functional inverse) creates a complex property chain because transitivity encourages multiple relationships, while inverse functionality restricts them to one. This interaction doesn't cause a contradiction but leads to a complex property chain.

- Transitive Bi / Functional A
If xBiy implies yAx (inverse), and xAy holds (transitivity), this doesn't lead to a contradiction. Rather, it forms a non-simple property chain where Bi's functionality interacts with the transitivity of A. Even though functionality suggests y can only relate to one instance, the transitivity still holds within the extended property structure.

- Transitive Bi / Functional Ai
The combination of Bi (functional inverse) and Ai (transitive inverse) forms a complex property chain because Bi limits relationships to one instance, while Ai's transitivity suggests multiple connections. This doesn't create a contradiction but a complex property chain.

- Transitive Bi / Functional B
If xBiy implies yBx (inverse), and xBy implies xBz (transitivity), the interaction between B's transitivity and Bi's inverse functionality doesn't cause a contradiction. Rather, it leads to a complex chain where y relates to multiple instances via different paths, preserving the consistency of the property relationships.


- Bi/Bi
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
