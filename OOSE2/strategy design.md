# Strategy Design (weeks 1/5):
**What:** The Strategy Pattern is a behavioral design pattern that allows you to define a family of algorithms, encapsulate them, and make them interchangeable at runtime.

**When to use:**
- When you have multiple algorithms for a specific task and want to switch between them dynamically.
- To remove complex conditional statements (if-else or switch-case).
- To follow the Open/Closed Principle (new strategies can be added without modifying existing code).

**Possible benefits to using Strategy Design:**
- flexibilty
- extensibility
- code cleanleness


## Example Implementation:

**step 1 make the strategy interface:**
``` java
// PaymentStrategy.java
public interface PaymentStrategy {
    void pay(double amount);
}
```

**Step 2: Implement Concrete Strategies**

```java
// CreditCardPayment.java
public class CreditCardPayment implements PaymentStrategy {
    private String cardNumber;

    public CreditCardPayment(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    @Override
    public void pay(double amount) {
        System.out.println("Paid $" + amount + " using Credit Card (" + cardNumber + ").");
    }
}
```
```java
// PayPalPayment.java
public class PayPalPayment implements PaymentStrategy {
    private String email;

    public PayPalPayment(String email) {
        this.email = email;
    }

    @Override
    public void pay(double amount) {
        System.out.println("Paid $" + amount + " using PayPal (" + email + ").");
    }
}
```
**Step 3: Create the Context Class**

```java
// PaymentContext.java
public class PaymentContext {
    private PaymentStrategy strategy;

    public PaymentContext(PaymentStrategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(PaymentStrategy strategy) {
        this.strategy = strategy;
    }

    public void processPayment(double amount) {
        strategy.pay(amount);
    }
}
```
**Step 4: Using the Strategy Pattern**

```java
// Main.java
public class Main {
    public static void main(String[] args) {
        // Using Credit Card Payment
        PaymentStrategy creditCard = new CreditCardPayment("1234-5678-9876-5432");
        PaymentContext context = new PaymentContext(creditCard);
        context.processPayment(100.0);

        // Switching to PayPal Payment
        PaymentStrategy paypal = new PayPalPayment("user@example.com");
        context.setStrategy(paypal);
        context.processPayment(200.0);
    }
}
```









