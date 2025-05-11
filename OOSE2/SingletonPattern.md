# [Singleton Pattern](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/OOSE2/Design%20Patterns.md)
**What:**
The Singleton Pattern is a creational design pattern that ensures a class has only one instance and provides a global access point to that instance.

**When to Use the Singleton Pattern:**
- When only one instance of a class should exist (e.g., a database connection, configuration manager, logging service).
- When an object should be accessible globally throughout an application.
- To control shared resources, preventing multiple instantiations.

**Why Use the Singleton Pattern?**
- **Ensures a Single Instance**: Prevents multiple instances of a class.
- **Global Access Point**: Easily accessible throughout an application.
- **Efficient Resource Management**: Controls shared resources like database connections, caches, etc.
- **Thread-Safety Considerations**: Can be adapted for concurrent applications.

<Br>
<Br>
<Br>

  **Step 1: Implement the Singleton Class**
```java
    // Logger.java
    public class Logger {
        private static Logger instance;
    
        // Private constructor prevents instantiation
        private Logger() {}
    
        // Public method to provide a single instance (Lazy Initialization)
        public static Logger getInstance() {
            if (instance == null) {
                instance = new Logger();
            }
            return instance;
        }
    
        public void log(String message) {
            System.out.println("[LOG]: " + message);
        }
   }
```
**Step 2: Using the Singleton Pattern:**
```java
// Main.java
public class Main {
    public static void main(String[] args) {
        // Get the Singleton instance
        Logger logger1 = Logger.getInstance();
        logger1.log("First log message");

        // Get another instance (same object)
        Logger logger2 = Logger.getInstance();
        logger2.log("Second log message");

        // Check if both instances are the same
        System.out.println("Are logger1 and logger2 the same? " + (logger1 == logger2));
    }
}
```
**Thread Safe Singleton:**
```java
// Thread-Safe Logger (Singleton)
public class Logger {
    private static volatile Logger instance; // volatile ensures visibility across threads

    private Logger() {}

    public static Logger getInstance() {
        if (instance == null) { // First check
            synchronized (Logger.class) {
                if (instance == null) { // Second check
                    instance = new Logger();
                }
            }
        }
        return instance;
    }

    public void log(String message) {
        System.out.println("[LOG]: " + message);
    }
}
```
