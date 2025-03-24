# [state design](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/OOSE2/Design%20Patterns.md)
**What:**
The State Pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes. The object will appear to change its class dynamically.

**When:**
- When an object's behavior varies based on its state (e.g., vending machines, TCP connections, traffic lights).
- When using if-else or switch statements to manage state transitions leads to complex code.
- When you want to encapsulate state-specific behaviors into separate classes.

<Br>

## Example state design implementation:
**Step 1: Define the State Interface**
```java
// State.java
public interface State {
    void handleRequest();
}
```
**Step 2: Implement Concrete States**

(draft state)
```java
// DraftState.java
public class DraftState implements State {
    @Override
    public void handleRequest() {
        System.out.println("Document is in Draft. Can be edited.");
    }
}
```
(moderation state)
```java
// ModerationState.java
public class ModerationState implements State {
    @Override
    public void handleRequest() {
        System.out.println("Document is under Moderation. Awaiting approval.");
    }
}
```
(published state)
```java
// PublishedState.java
public class PublishedState implements State {
    @Override
    public void handleRequest() {
        System.out.println("Document is Published. Read-only mode.");
    }
}
```

**Step 3: Create the Context Class (Document)**
```java
// Document.java
public class Document {
    private State state;

    public Document() {
        this.state = new DraftState(); // Initial state
    }

    public void setState(State state) {
        this.state = state;
    }

    public void process() {
        state.handleRequest();
    }
}

```

**Step 4: Using the State Pattern**
```java
// Main.java
public class Main {
    public static void main(String[] args) {
        Document document = new Document();

        // Initial state: Draft
        document.process();

        // Change to Moderation state
        document.setState(new ModerationState());
        document.process();

        // Change to Published state
        document.setState(new PublishedState());
        document.process();
    }
}
```

