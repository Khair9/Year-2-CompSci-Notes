# [High-Level vs. Low-Level Modules in Software Design](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/OOSE2/week4-6.md)

In software architecture, the terms **high-level** and **low-level modules** describe different layers of abstraction.

---

## 🔹 High-Level Modules

- Contain **business logic** or **application-specific rules**.
- Focus on **what** the software does.
- Usually control the overall flow of the application.
- Are more abstract and less concerned with implementation details.

### ✅ Example:

```java
public class PaymentProcessor {
    public void processPayment(double amount) {
        // Business logic like applying discounts, validating input, etc.
    }
}
```


```java
// Abstraction
public interface PaymentGateway {
    void charge(double amount);
}

// High-Level Module
public class PaymentProcessor {
    private final PaymentGateway gateway;

    public PaymentProcessor(PaymentGateway gateway) {
        this.gateway = gateway;
    }

    public void processPayment(double amount) {
        // Business logic
        gateway.charge(amount);
    }
}

// Low-Level Module
public class StripePaymentGateway implements PaymentGateway {
    @Override
    public void charge(double amount) {
        System.out.println("Charging $" + amount + " using Stripe");
    }
}
```
