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









