# [Adapter Pattern](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/OOSE2/Design%20Patterns.md)
**what:**
The Adapter Pattern is a structural design pattern that allows incompatible interfaces to work together by acting as a bridge between them. It enables an interface of an existing class to be used as another interface without modifying its source code.
**when:**
- When you need to convert an interface of an existing class into another interface that the client expects.
- When you want to reuse an existing class but its interface does not match the requirements.
- When you are working with third-party libraries and you cannot modify their source code.
## Example Implementation of adapter pattern
**Step 1: Define the Target Interface**

This is the expected interface that the client (your charger) needs.
```java
// EuropeanSocket.java (Target Interface)
public interface EuropeanSocket {
    void plugIn();
}

```
**Step 2: Define the Adaptee (Incompatible Class)**

This is the incompatible class that needs to be adapted.
```java
// USPlug.java (Adaptee)
public class USPlug {
    public void insertIntoUSSocket() {
        System.out.println("US plug inserted into US socket (110V).");
    }
}

```
**Step 3: Create the Adapter**

The adapter allows the USPlug to work with a EuropeanSocket.
```java
// PowerAdapter.java (Adapter)
public class PowerAdapter implements EuropeanSocket {
    private USPlug usPlug;

    public PowerAdapter(USPlug usPlug) {
        this.usPlug = usPlug;
    }

    @Override
    public void plugIn() {
        System.out.println("Adapter converts European socket (220V) to US socket (110V).");
        usPlug.insertIntoUSSocket();
    }
}

```
**Step 4: Implement the Client (Using the Adapter)**

The client is your phone charger, which expects a European socket but gets adapted.
```java
// Main.java (Client)
public class Main {
    public static void main(String[] args) {
        USPlug usPlug = new USPlug();  // The plug that doesn’t fit
        EuropeanSocket adapter = new PowerAdapter(usPlug); // Adapter makes it compatible

        // Now we can use the US plug in a European socket
        adapter.plugIn();
    }
}
```

```
Adapter converts European socket (220V) to US socket (110V).
US plug inserted into US socket (110V).

```
