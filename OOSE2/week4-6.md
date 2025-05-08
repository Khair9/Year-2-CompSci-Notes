# [4.1.1 uml diagrams](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/OOSE2/oose.md)
Class diagrams in Java are a Blueprint or Model of the system that you are building
 - They can help you map out the design of a system
 - They can help you understand what you have built
 - They can give a visual map of the system when well organises

We use Unified Modelling Language to produce our diagrams
 - Class notation and entity relationships are the key elements to understand

### Class notation
![image](https://github.com/user-attachments/assets/5a725ee0-4226-4fda-8aed-ec04ba672695)
Attributes: The data that the class stores
 - Type tells you if it is a String, integer, Boolean, etc.
 - A “+” means it is Public,
 - a “-” means Private
 - A “#” means Protected
 - Default values tell you what the variable is initialised to

Operations: the methods within the class 
 - In addition to the same +/- notation, their input parameters and return type (if any) are specific 
### UML
alot of stuff already done before
##### Realization
Realization in UML (Dotted Line with Hollow Arrow)
In UML class diagrams, a dotted line with a hollow triangle arrow represents a realization relationship.

 - **What It Means:** A realization means that one class or component implements the specification defined by another — typically used with interfaces or abstract classes.
 - **When Is It Used?**
 - **A class implements an interface.** A concrete subclass implements the abstract methods of an abstract class (if inheritance is not shown as generalization).

 - Key Concepts:
   - Interface
      - Defines only method signatures, not actual code.

      - Cannot be instantiated.

      - Example: interface Drawable with method draw().

- Abstract Class
   - May define some methods with implementation, and others without.
       - Cannot be instantiated.
       - Used as a partial blueprint.

-  Concrete Class  
    - Implements all methods from interfaces/abstract classes.
    - Can be instantiated.
 
![image](https://github.com/user-attachments/assets/31a837ac-bc80-4d12-91fe-fc70588376d4)

##### Aggregation
Key Features:
 - It's a weaker form of composition.
 - Represented by a hollow diamond at the “whole” (container) end of the line
 - Implies a "has-a" relationship.
   
Example:
 - A Team has multiple Players.
 - Players can exist without a Team (e.g., be free agents).
   
```
Team ◇───── Player
```
![image](https://github.com/user-attachments/assets/ab06f5c1-0155-46f4-af36-710ac425fb54)


# 4.1.2 observer design pattern 
already done in the design pattern folders

# 4.1.3 mocking
### what is local unit testing
cal unit testing refers to the practice of running unit tests on your local development machine (as opposed to running them in a shared environment like a CI/CD pipeline or staging server).

- Unit Testing
  - Tests individual components or functions of code in isolation.
  - Ensures that each "unit" of logic behaves as expected.

- Local Testing
   - Performed on your own machine (laptop/desktop).
   - Usually done before pushing code to version control.
- continous integration
   - At regular intervals or on commit run unit test
   - Your change may affect another method, class or package
   - Speed of tests
   - Early feedback on your change

### Doubling
 -  A **test double** is a general term for any object that replaces a real component in a test to control behavior or observe interactions.
 - what to double:
    - Read or write to a file
    - Read or write to a database
    - Calls to a web service
    - Calls to another application
    - Calls to an external library
   
#### mocking **why**
   - Speed up continuous integration testing
   - Faster and earlier feedback
   - Remove dependencies on input and output
   - Remove dependencies on external applications that could be down or slow
   - Code of the application does not need to change
#### mocking spy v mock
Both can be used to mock methods or fields. The difference is that in mock, you are creating a complete mock or fake object while in spy, there is the real object and you just spying or stubbing specific methods of it.

#### mocking - challenges
 - **Code coverage** – How much code is exercised
 - **Case coverage** – How many use cases are covered by the test suite
 - Null test, yet validation layer prevents
- 100% code coverage does not guarantee 100% case coverage


### [A mocking script](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/OOSE2/mocking.java)

-----------------------

# Week 5
##  5.1.1
the decorator design pattern done in a seperate file

## 5.1.2 Refactoring

**Refactoring** is a disciplined technique for restructuring an existing body of code, altering its internal structure without changing its external behavior.

### Clean code 
|positives|
|---------|
|Easier to start and continue|
Easier to follow
Better for team onboarding
Most time spent enhancing code, adding new features
Avoid duplication, if you understand it you will use it

#### S.O.L.I.D.
 - Single Responsibility Principle (SRP)
    - A class/method should have one and only one reason to change, meaning that a class should have only one job.
 - Open-Closed Principle (OCP)
    - You should be able to add new functionality without altering existing code.
 - Liskov Substitution Principle (LSP)
    - Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.
 - Interface Segregation Principle (ISP)
    - Clients should not be forced to depend on interfaces they do not use.
    - Prefer small, specific interfaces over large, general ones.
    - Leads to more modular and flexible code.
 - [Dependency Inversion Principle (DIP)](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/OOSE2/explaination456.md)
    - High-level modules should not depend on low-level modules. Both should depend on abstractions.
    - Reduces coupling between software modules.
    - Use dependency injection to pass in dependencies rather than hardcoding them.

#### Domain Name (the names of stuff i think, the lecture isnt very clear here)
- Make the implicit explicit
- Cultivate a shared language
- Learning never stops
- Explore multiple models
- Focus on concrete scenarios
- Design is evolutionary

#### DRY
dont repeat yourself

#### touch it once
- Don’t leave comments to return
- You might not go back
- You will have a learning curve to get back up to speed



### Refactoring
#### Style guides
- Naming conventions camelCase, PascalCase, snake_case
- Size of methods and classes
- Consistency
- assertEquals assertSame
- Easier to read consistent code

  #### refactoring process
  <img src="https://github.com/user-attachments/assets/c5544e1c-9c7b-4764-9844-13d890a40f47" alt="ljandocjnoad" width="500" >


  
#### smells
- Duplicate Code
- Long method or class
- Variables and parameters
- Shotgun surgery
- Parallel inheritance hierarchies
- Switch statements or if
- Refused bequest
- Alternative classes with different interfaces
- Middle man
- Inappropriate intimacy
- Data class
#### types of refactoring
- Fixing Method
- Moving Functionality
- Organising Data
- Simplifying method
- Simplifying conditions
- Reorganise classes

#### rules of refactoring
- Your methods and functions should do one thing
- No duplication, problems have to be fixed several times
- Consistency of style
- Later tend to be never
- Don’t always comment
- Remove commented out code, version control has a history

  
--------------------

# Week 6
this was reading week with guest lecturers

--------------------

# Week 7
## 7.1.2 Design Principles
no new info just crap about planning

## 7.2.1 singleton design pattern
done elsewhere
----------------------
# Week 8
## 8.1.1 state design pattern
## 8.1.2 iterator and composite design pattern

-----------------------
# Week 9
## 9.1.1 factory design pattern
## 9.1.2 requirements gathering
### Scope
The scope establishes the high level description of the system you are building
 - Setting boundaries
 - Business Benefits
 - Stakeholders
### Forming requirements
Build on your scoping and identify decision makers first – who decides on what you do?
 - Identify the stakeholders
 - Who has the knowledge
 - Tie back development and testing to requirements
### Prototype
 - Prototypes are not iterations of the software, the material used to build them is not well engineered, secure, or reliable and must not creep into your final software deployment (allowing this is a major source of bugs)
**We can try to build prototypes when:**
- The requirements are unknown or unclear
- The technology is unknown
- It is a new team
- Need early knowledge and early feedback
##### Prototypes can be:
- Low fidelity/non-functional: A drawing of a user interface
- Low fidelity/functional: A powerpoint slideshow with buttons built in to regions of the slide
- Hi-fidelity/non-functional: A webpage showing a proposed UI 
- Hi-fidelity/functional: An early version of the software with no persistence between sessions

### Questions
- Likert Scale
- Categorical
- True/False
- Closed question
- Open Ended

(this is what a likert scale is)

![image](https://github.com/user-attachments/assets/54a92707-655a-4a68-8838-91a979851731)

#### survey

A set list of questions,

benefits including:| Drawbacks:
------------------|------------
Easy to compare with other participants|No follow-up for lack of detail
Consistency | No interview/less accountability
Large scale
If they are not open questions, can look at statistics
If that helps!

#### Structured Interview 
benefits|Drawbacks
------|------
Consistency in the responses|No follow-ups to compensate for lack of detail in the questions
Allows for easy comparison with other participants|It’s boring!
Means the Interviewer does no need to be skilled

#### Un-Structured Interview
pretty obvious benefits and drawback cba to note

#### Semi-Structured Interview
A list of set questions or a topic guide with areas you want tot ouch on with follow-up unscripted questions that depend on answers with the advantages that they:
  

#### Group Meetings – Focus Group
Focus groups are small group discussion sessions with 2 facilitators (1 to lead discussion and 1 to take notes/look for follow up opportunities and 3-8 stakeholders

#### user stories

---------------------------
# week 10
## 10.1.1 adaptar design pattern
done in the design pattern file

## 10.1.2 Navigating Codebases
### Enviroments
- **Local development environment** – Local to your computer to develop and test
- **Development** – describes and area to test features, less stable
- **System Integration Test (SIT)** - describes as the area to test features work together and integrate with other applications 
- **User Acceptance Test (UAT)** - describes as the area that user of the application test the system
- **Performance Test** - describes as the area performance tests are performed to mimic production and at peak levels
- **Scratch/Stage** – A test environment prior to production.
- **Live or Production** - describes as the area the application runs and is used by the end users and integrates with other applications
![image](https://github.com/user-attachments/assets/4adb663c-a466-448c-9698-dcaac89a9610)
![image](https://github.com/user-attachments/assets/8e8da2e7-b580-4df4-9117-76777c025486)
### What makes a good code commit:
- The change links to one requirement, item of work
- The change is self contained and can work on its own
- The change is not too large to be difficult to review
- A change is not so small as to require other small changes
- The change can go across several files and classes, but if significant for a file or class maybe better on it own
- The change assess impact on the rest of the codebase
- Consider older versions of applications go live later e.g. rest services
<Br>
All branched changes must be merged back to the next branch and or master


















