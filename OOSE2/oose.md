# [OOSE](https://github.com/Khair9/Year-2-CompSci-Notes/tree/main)

[past papers](https://gla.sharepoint.com/sites/COMPSCI2008OOSE2023-24/Class%20Materials/Forms/AllItems.aspx?id=%2Fsites%2FCOMPSCI2008OOSE2023-24%2FClass%20Materials%2FPast%20Exams&p=true&ga=1)

[Design Patterns](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/OOSE2/Design%20Patterns.md)

[Weeks 1-3](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/OOSE2/weeks%201to3.md)

[Week 4-10](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/OOSE2/week4-6.md)

[UML/Class Diagrams](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/OOSE2/uml.md)

[calc](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/OOSE2/calc.java)

----------------------------

## from review of past papers

### Database Interaction and Performance / Data Persistence Strategies
At its core, this topic is about how software applications store and manage data so that it's not lost when the application closes, and how to do this efficiently.
1. Data Persistence:
     - Imagine you're using an application (like a game, a banking app, or a social media platform). When you enter information, make changes, or create something new, you expect that data to still be there the next time you open the app.
     - Persistence is the act of saving this data in a durable location (meaning it survives even if the power goes out or the app restarts). This is most commonly a database, but it could also be files on a disk.
2. Database Interaction:
   - This refers to how your software application "talks" to the database. This communication involves actions like: Writing, Read, Deleting, Querying
3. Strategies for Saving Data:
   - When an application needs to save multiple pieces of data (like the "one thousand investments per share" mentioned in the question), it has choices about how to send this data to the database.
   - Approach 1: Saving Each Item Individually (One by One)
       - **How it works:** For each investment fund value calculated, the application immediately sends a command to the database to save that single value. If there are 1000 fund values, this means 1000 separate save operations.
       - Benefits:
             - Simplicity (sometimes): For a small number of items, this can be straightforward to implement.
             - Immediate feedback: You know right away if a specific item was saved successfully or if there was an error for that particular item.
       - Challenges:
             - Performance Overhead: Each save operation involves establishing a connection (or using an existing one), sending the data, the database processing it, and sending a confirmation back. Doing this thousands of times can be slow.
              - Network Traffic: Lots of small back-and-forth messages between the application and the database.
             - Database Load: The database has to handle many individual requests, which can strain its resources.
  -  Approach 2: Saving Items in Bulk (Bulk Commit / Batching)
        -  **How it works:** The application gathers multiple investment fund values (e.g., all 1000, or perhaps in chunks of 100) and then sends them to the database in a single, larger save operation.
        -  Benefits:
              - Improved Performance: Significantly faster for large volumes of data because the overhead of connecting, sending, and processing is incurred fewer times.
             - Reduced Network Traffic: One larger message is often more efficient than many small ones.
             - Reduced Database Load: The database can process a batch of data more efficiently than many individual pieces. This "saves time and CPU" for both the application and the database server.   
        - Challenges:
             - Error Handling: If one item in a batch fails to save, you need a strategy to handle it. Does the whole batch fail? Do you try to save the others? This can be more complex.
             - Memory Usage: The application might need to hold more data in memory before sending the batch.
             - Delayed Feedback: You might not get immediate confirmation for each individual item until the whole batch is processed.
             -

------------------------- 
### Extensibility
Extensibility is a software design principle that refers to the ease with which a system or component can be expanded or enhanced to accommodate future growth or changes—such as adding new features or modifying existing behavior—without having to rewrite existing code.

##### In Java (and OOP in general), extensibility often involves:
 - **Inheritance:** Subclasses can extend and override parent class behavior.
 - **Interfaces and Abstract Classes:** Allow multiple implementations and easy plug-in of new behavior.
 - **Composition over Inheritance:** Combining objects to extend behavior without modifying original code.
 - **Design Patterns:** Like Strategy, Decorator, and Observer, which support flexible and extendable systems.

