# Lab Exam
## Design Decisions
### Task One
* Design Pattern -
* Reason -
* Implementation - 
### Task Two
* Design Pattern -
* Reason -
* Implementation - 
### Task Three
* Design Pattern -
* Reason -
* Implementation - 

## Required
* We expect you, as University students, to be responsible and act honourably. We will trust you to follow these rules. We will, however, take disciplinary action if you are caught violating them.
* All work you submit must be your own. You must not copy or reuse someone else's code, or discuss or work together on any aspect of your solution. It must be your own independent work.
* You may not discuss any of the content of the lab exam with others before the submission deadline. The University can and will take disciplinary action against you even if you are passively a member of a social media group caught discussing an exam.
* We will use automatic similarity detection software, which is very effective at detecting potential collusion. If cheating is suspected, you will be referred for disciplinary action.

## Marking
* Use style guide [https://stgit.dcs.gla.ac.uk/software-engineering-practices/starting-a-lab/-/wikis/home/Languages/Java/Style-Guide](https://stgit.dcs.gla.ac.uk/software-engineering-practices/starting-a-lab/-/wikis/home/Languages/Java/Style-Guide), 10 marks will be awarded for clean code.
* You must include the name of the Design Pattern in the names of files using that design pattern. For example `CommunicationStrategy.java` if using the Strategy Design Pattern.

## Task One
* The `Exam.java` file has a private list of students. Ensure this cannot be amended by other classes by using a design pattern you have been taught. (15 Marks)
* Describe in the ReadMe at the top the design decision, your reasoning behind it in maximum 150 words and a short description with Class names how you have implemented. (10 Marks)

## Task Two
* The student application assigns exam times and adjustments. A student can be registered with zero or more disabilities. Each disability might add on extra time or change if they are in separate rooms.
* You are provided with a file `src/main/resources/OOSE_202505171000.csv`. **DO NOT AMEND THIS FILE**. This should be loaded by `CreateExam.java`. `ExamReport.java` will then create a report of extra times and venues for the students.
* `CreateExam.java` currently does not read in disability and adjustment information. 
* Implement a solution in `CreateExam.java` with a taught design pattern to also read in student disabilities. (30 marks)
* Below are the disabilities:
    * ADHD - 0.25 Extra Time, Main Venue
    * Autism - 0.25 Extra Time, Separate Venue
    * Dyscalculia - 0.25 Extra Time, Main Venue
    * Dyslexia - 0.25 Extra Time, Main Venue
* If you have two disabilities the extra time is added together.
* If at least one disability requires a separate room, then the students will be given a separate room.
* Describe in the ReadMe at the top the design decision, your reasoning behind it in maximum 150 words and a short description with Class names how you have implemented. (10 Marks)

## Task Three
* New disabilities may be added. Choose a taught design pattern to avoid `CreateExam.java` having to be amended when this happens. (10 Marks)
* Describe in the ReadMe at the top the design decision, your reasoning behind it in maximum 150 words and a short description with Class names how you have implemented. (10 Marks)
