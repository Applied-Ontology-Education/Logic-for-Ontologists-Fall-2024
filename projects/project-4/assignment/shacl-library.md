# Born Free But Everywhere in SHACL #

For this project, the class will divide into two teams competing for fame and glory. Each team will have the same task, to construct and validate SHACL files for the following artifacts:

1. [Basic Formal Ontology Core](https://github.com/BFO-ontology/BFO-2020/blob/master/src/owl/bfo-core.owl)
2. The eleven modules of the [Common Core Ontologies 2.0 release](https://github.com/CommonCoreOntology/CommonCoreOntologies/tree/master/src/cco-modules)

Each team will accordingly need to submit the following deliverables: 
1. BFO SHACL file
2. 11 CCO SHACL files
3. BFO Knowledge Graph Test Data file
4. 11 CCO Knowlegde Graph Test Data files
5. Validation Report for BFO SHACL file
6. Validation Report for each of the 11 CCO SHACL files

## Guidelines ##

If you are at all familiar with CCO and have a bit of awareness about SHACL, then I suspect you see already how much work is being requested here. Rest assured, I am aware too. 

There are ways to lighten the work, however, and part of the point of this exercise is to encourage you to think in terms of **automation** and **tool support**. I include a list of tools and resources below that will be helpful, if you take them seriously. You should, of course, take them seriously. What I *do not want* and indeed will *not be happy with* is if I catch any of you spending a bunch of time hand-crafting shapes. Better that you hand craft code to create shapes; even better that you leverage an existing tool to create shapes. 

If it is not yet clear, I am dividing the class for this project in part because *about a third of the class has experience automating such things*. This will be a learning opportunity. 

To emphasize the importance of automating as much as you can, I'll add that it's not enough to simply create SHACL files paralleling the relevant ontology files. As I said, that can and should be largely automated. Even if you did this perfectly with the files cited above using existing tooling, your result would not quite be what I'm looking for. 

This is because automation of the sort I have in mind will in almost every case need to leverage semantic relationships that have been **asserted** in the relevant ontology files using OWL. This raises two issues for automation: 
```
1. OWL is not expressive enough to reflect the intended interpretations of all CCO definitions
2. CCO elements do not have many axioms asserted
```
We have lived with the limitations of OWL referenced in **1** for years. With respect to **2**, because CCO is designed to be extended in a variety of ways, early developers kept the axiomatization light so as not to exclude unforeseen extensions. For you see, any time you add a non-redundant axiom to an ontology element, you exclude some collection of possible instances as falling within the scope of that element. 

Traditionally, our community has addressed **1** and **2** by leveraging textual definitions for class terms and relational expressions. Textual definitions is where you should expect to find the intended interpretations of ontology elements. They're free text annotations and so are not constrained by the limitations of OWL or whether axioms have been asserted. Unfortunately, accurately extracting semantics from free text is not particularly easy to automate...

All of which is to say, to complete this exercise you are required to leverage whatever tooling you can to automate as much of the process as you can. There will nevertheless be considerable work to do to reflect the textual definitions in SHACL, however. If you try to do it **all** by hand, you will not finish by project end. If you automate as much as you can, you at least have a chance. 

May the odds be ever in your favor. 

## Validation ##

To validate your SHACL files, you will need to generate knowledge graphs based CCO with (new) instance data added. I again *do not* want to hear of anyone creating instance data by hand. 

For validation, you will need to run your SHACL files against the knowledge graphs and generate a report absent errors or warnings. You will need to submit your error report as part of this assignment. 

You may find the following resources useful: 
1. [SHACL Playground](https://shacl.org/playground/)
2. [Astrea](https://github.com/oeg-upm/Astrea?tab=readme-ov-file)
3. [PySHACL](https://github.com/RDFLib/pySHACL)
4. [SHACLGEN](https://github.com/AKSW/shaclgen)
5. [SHACL Validator](https://rdfshape.weso.es/shaclValidate)

You may also find the following documentation useful:

1. [SHACL W3C](https://www.w3.org/TR/shacl/)
2. [DASH Library](https://datashapes.org/dash.html)
3. [BFO 2.0 User Guide](https://ncorwiki.buffalo.edu/index.php/Basic_Formal_Ontology_2.0) - Link under "Background Information" 
4. [CCO Documentation](https://github.com/CommonCoreOntology/CommonCoreOntologies/tree/master/documentation/user-guides)

## Teaming ##

The class will be divided evenly. Students are expected to determine allotment, but teams must be comprised of the same number of members (with a +1/-1 deviation allowed). In addition to urging you to think in terms of automation, this exercise is also designed to encourage project management skills. I encourage you to identify a strategy early for dividing sub-tasks, setting deadlines, and addressing blockers to progress.  

I suggest setting up 15 minute 'stand-up' meetings every other day, where team members are expected to join. zoom call or meet in person and (a) explain what progress they have made on their sub-task, (b) explain what they intend to achieve before the next stand-up, and (c) share any blockers that have to progress. This is an effective way to keep members focused on a team goal, as well as opportunities to overcome challenges. 

## Submission ##

I will expect at most **two** submissions, one reflecting the results of each team. 