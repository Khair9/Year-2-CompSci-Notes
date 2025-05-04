##### Weeks 1-3
------------------
# [Week 1](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/OOSE2/oose.md)
### Bugs
_A common term used to describe a flaw, mistake, or failure in a computer system that produces an incorrect or unexpected result or causes it to behave in unintended ways._

Everything we don’t like is a bug! 

#### Reasons for bugs
1. The software doesn't do something that the product specification says it should do.
1. The software does something that the product specification says it shouldn't do.
1. The software does something that the product specification doesn't mention.
1. The software doesn't do something that the product specification doesn't mention but should.
1. The software is difficult to understand, hard to use, slow, or—in the software tester's eyes—will be viewed by the end user as just plain not right. 

<img width="322" alt="image" src="https://github.com/user-attachments/assets/f90fcad6-d244-4719-a2f2-720b0c8ea8e4" />

#### Causes of bugs

##### Specification
- Unwritten or incomplete
- Ambiguous 
- Constantly changing
- Not communicated to the development team
##### Design 
- Inappropriate modelling
- Lack of modelling tools
- Time to market pressure
##### Code
Software complexity
Poor documentation 
Limited time
Programmer skills
##### Reliability
However, failures seem random, hence Bayesian (probabilistic) theories over time are applied
 - R(t) - the probability of software still functioning at a given point in time (t) 
 - Availability/up-time - what percentage of the time will a service be available (particularly useful in online services)
 - Mean time between failures (MTBF) - how long, on average, will you go before the system fails again
##### Debugging
<img width="332" alt="image" src="https://github.com/user-attachments/assets/7a17bc3f-3547-48be-b693-a767fdbb3b16" />

The debugger lets you decide if you want to:
 - Resume operation – run until the next breakpoint or until the program terminates
 - Step over – move past a line of code
 - Step in – execute the next line of code
 - Step out – leave method
 - Restart
 - Terminate the program

-----------------

# week 2
### development styles 
just a bunch crap about peer programming when its useful and stuff
- permiscus peer programming is like peer programming but your kind of consulting an expert in that field

------------------
# Did 3.1.2
- not much to say just development stuff
------------------
# Coupling
 - The degree of interdependence between software applications/modules/services e.g. deployable units
     - An application – the executable program for your team
     - A module – A file of code or a class
     - A service – A process available to the application, calling a database, sending a message, making an Application Programme Interface (API) call
## coupling types
### Content Coupling
One module, file or class uses code from another
 - TwentyOne and CardGame – Heavy content coupling
 - Sevens and CardGame – Heavy content coupling
 - Same package

Removed duplication – set up players once

### Common Coupling
Several modules, files or class have access to the same global data
 - Global data is data they anyone can access so is public
 - Public CardGame.players – this is global data
 - It is used by TwentyOne and Snap so they have Common Coupling

### External Coupling
Several modules, files or class have access to a externally imposed data format, communication protocol or device interface
 - An external data format for example a database table structure
 - Swift is used to transfer money around the world and have a specific format
 - An application built to sent SWIFT messages would have external coupling

### Control Coupling
One module, file or class to control the flow of another module, by passing information on what to do
 - If you had a separate module to determine if a person is bust
 - If a separate module determined the status of another module

### Stamp Coupling (data-structure coupling)
Several modules, files or class have access to the share a composite data structure
 - A composite data structure has more than one data types
 - playingCard.userHand() is just an integer so not a composite data structure
 - A deck is a list of Cards so a composite data structure



### Data Coupling
Data coupling occurs when modules, files or classes share data through parameters
 - Passing an integer to a function to calculate the square root
 - TwentyOne and CardGame have data coupling since TwentyOne call CardGame methods with parameters
 - You are tied to the method parameters
### how strong are data coupling types
<img width="923" alt="image" src="https://github.com/user-attachments/assets/4832acd9-7b9e-41ec-9602-6f1fc9e494d7" />


### Cohesion
 - The degree to which deployable units belong together, perform similar technical or business functions
 - A deployable unit, an executable program or process to run
   
##### Example of cohesion:
 - Moodle 
    - Stores students in a configuration file
    - Displays course materials available in the library
       - Database look up – High Coupling
       - Call a rest web service to check – Low Coupling
       - Link to the library catalogue – Very Low Coupling, manual

 ### Coupling & Cohesion – Why Avoid It
 - Impact of High Coupling
     - Coordination effort of changes
     - Delay (time to market) for new business functionality
     - Additional testing and environment setup
     - Additional risk of impact
     - Lack of visibility

``` markdown
 ### Coupling & Cohesion – Why Do It
 - Library Catalogue Check - Implement
     - Database look up – High Coupling
     - Stored Procedure in Library Book Catalogue
     - Call stored Procedure from Moodle
```

### Cohesion
 - Refers to how closely related and focused the responsibilities of a single module/class are.
 - High cohesion means a module does one thing well.
 - Promotes readability, maintainability, and reusability.
 - Easier to debug and test because functionality is localized.
 - Enhances code organization and clarity.

### Coupling
 - Refers to how much one module depends on others.
 - Low coupling means modules are independent.
 - Reduces ripple effects from changes in other modules.
 - Increases modularity and makes the system easier to understand.
 - Improves flexibility and allows for easier updates and scaling.

### Why It Matters
 - Systems with high cohesion and low coupling are:
 - Easier to maintain and evolve.
 - More robust and fault-tolerant.
 - Simpler to test and debug.
 - Better structured for team development and scalability.
    
### Temporal Coupling
 - Definition: When two or more operations in a module must be executed in a specific order.
 - Example: A method that initializes resources must be called before another method that uses them.
 - Problem: If the sequence is violated, the system may break or behave incorrectly.
 - Solution: Refactor the code to enforce the order automatically or encapsulate dependencies.

### Subclass Coupling
 - Definition: Occurs when a subclass is tightly dependent on the implementation details of its parent class.
 - Problem: If the parent class changes, the subclass may break, violating the Liskov Substitution Principle.
 - Sign of Fragility: The subclass relies on specific behaviors or internal mechanisms of the superclass.
 - Solution: Favor composition over inheritance when appropriate, or ensure the superclass has a stable and well-defined interface.

#### What is Composition?
 - Composition means a class contains and uses instances of other classes, rather than inheriting from them.
 - It follows the principle: "has-a" relationship instead of "is-a".
 - Promotes looser coupling because you're not tied to the internal behavior of a superclass.
 - More flexible — you can change the composed class without affecting the consumer class much.




      
