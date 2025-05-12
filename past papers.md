# [Past Papers](https://github.com/Khair9/Year-2-CompSci-Notes/tree/main)

[comp Sci past papers](https://moodle.gla.ac.uk/course/view.php?id=21505)

[pdf 2 .docx](https://www.adobe.com/acrobat/online/pdf-to-word.html)



## P2T
Paper|Percentage|Time|Review
-----|----------|--------|-------
[2018](https://moodle.gla.ac.uk/pluginfile.php/8608242/mod_resource/content/1/PHYS2003_1_Physics_2T__Prog_Under_Linux_201804.pdf)|65|idk a while tho|&,$,bash needs practical work done the most, some more practical work learning the basics of C as well, function prototypes
[2019](https://moodle.gla.ac.uk/pluginfile.php/8608244/mod_resource/content/1/PHYS2003_1_Physics_2T__Prog_Under_Linux_201904.pdf)|71|idk not too much over the set time|history 45!, git branching hotfix, standard and commandline arguments
[2024](https://moodle.gla.ac.uk/pluginfile.php/8608252/mod_resource/content/1/P2T%20Exam%202024.pdf)|54|--|make files,fscanf, function prototypes,preprocessor files


## Algs & Datas
Paper|Percentage(60 marks)|Time(1:30hr)|Review
-----|----------|-----|-------
2019|75(in accurate chat gpt)|2:39|Recurrsion tree, Linear recurrsion,!!Recurrence Equation,Merge Sort
2023|62|3:00|what to revise is listed below
2021|82|2:00|<img width="500" alt="image" src="https://github.com/user-attachments/assets/cba85039-348d-469c-8d8d-d07f101407ec" />


## OOSE
Paper|Percentage(50 marks)|Time(1:30hr)|Review
-----|----------|-----|-------
August 2022 (resit)|70% (28/40)| overtime| Topics of threat: **design spec class diagrams and uml** didnt do question 2 10 marks because there was only the paper with the soloutions which made it impossible to do the question
may 2023|58% (29/50)| overtime|Q1c bul commits, Q2a coupling, umls of every strategy, factory design pattern, extensibility
2024|61 (24/40)| ontime| mocking, testing






#### design spec (oose)
- The software doesn't do something that the product specification says it should do.
- The software does something that the product specification says it shouldn't do.
- The software does something that the product specification doesn't mention.
- The software doesn't do something that the product specification doesn't mention but should.
- The software is difficult to understand, hard to use, slow, or—in the software tester's eyes—will be viewed by the end user as just plain not right.

#### Coupling
Type of coupling|Worst to Best coupling|Description
----------------|---------|-----------
Content| worst | One module modifies or relies on the internal workings of another.
Common| 2nd|Multiple modules share the same global data. Changes in that data affect all modules that share it.
External|3rd|Modules share externally imposed formats, protocols, or device interfaces. Example: Two modules interact through a shared file format.
Control|4th|One module controls the flow of another by passing control flags or logic. Example: Passing a flag to tell the other module what to do.
Stamp(Data-Structured)|5th|Modules share a composite data structure and only use part of it. Example: Passing an object when only a field is needed.
Data Coupling |Best among direct couplings|Modules share data through parameters (only what's needed is passed). Promotes clarity and separation of concerns.
No Coupling|Ideal in some contexts|Modules are entirely independent and unaware of each other. Often seen in loosely coupled systems like microservices.



















------------------
Based on the marks you lost in the test, here are the main topics I recommend you focus on for revision:

Algorithm Analysis (Big-O, Recurrences):

1. Recurrence Relations: You missed solving recurrences (Q1e, Q2c). Practice solving recurrence relations, especially using the Master Theorem, as it's crucial for analyzing divide-and-conquer algorithms.
Detailed Analysis: Review how to perform line-by-line asymptotic analysis for iterative algorithms (Q1c) and how to determine worst-case and best-case running times (Q5b).
Algorithm Design Paradigms (Divide and Conquer):

1. The biggest loss of marks was in Q1d, where you didn't provide a divide-and-conquer solution as required. Focus on understanding the divide-and-conquer strategy: breaking a problem into smaller subproblems, solving them recursively (conquer), and combining the results. Study classic examples like Merge Sort, Quick Sort, and the majority element algorithm from the mark scheme.
Data Structures (Stacks, Design Constraints):

1. In Q4b, your proposed solution didn't meet the constant time (O(1)) requirement for all operations (PUSH, POP, MIN). Review standard data structures like stacks and how they can be combined or augmented (like the two-stack solution in the mark scheme) to achieve specific performance guarantees.
Sorting Algorithms (Properties & Implementation):

1. You correctly identified instability in Selection Sort (Q3a) but only partially described how to make it stable (Q3b). Review properties like stability for various sorting algorithms and understand the implementation details required to modify or ensure these properties.
Hashing:

 1. Your approach to generating hash collisions in Q5d was flawed. Review how basic polynomial rolling hash functions work and understand common techniques for finding collisions, such as finding small equivalent blocks as shown in the mark scheme solution.
Concentrating on these areas, particularly Algorithm Analysis (Big-O, Recurrences) and Divide and Conquer, should help address the major gaps highlighted by the test. Good luck with your revision!
