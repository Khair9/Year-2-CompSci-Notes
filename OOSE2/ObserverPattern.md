# [Observer Pattern (weeks 4/8)](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/OOSE2/Design%20Patterns.md)
### what:
The Observer Pattern is a behavioral design pattern that allows one object (the subject) to maintain a list of dependents (observers) that get automatically notified of any changes.
### when to use:
- When you need to notify multiple objects about state changes in another object.
- When a one-to-many relationship between objects is required.
- When implementing event-driven architectures (e.g., GUI listeners, pub-sub models, real-time updates).

### why use:
- Decoupling (Observers and subjects are independent, making it easy to modify or add new observers.)
- Scalability
- Real-Time Updates
  
## example implementation
Stock Price Update System, where multiple investors (observers) get notified when the stock price changes.


**Step 1: Define the Observer Interface:**
```java
// Observer.java
public interface Observer {
    void update(String stockName, double price);
}
```
**Step 2: Implement Concrete Observers**
```java
// Investor.java
public class Investor implements Observer {
    private String name;

    public Investor(String name) {
        this.name = name;
    }

    @Override
    public void update(String stockName, double price) {
        System.out.println(name + " received an update: " + stockName + " is now $" + price);
    }
}

```
**Step 3: Define Subject Investor:**
```java
// Subject.java
import java.util.ArrayList;
import java.util.List;

public interface Subject {
    void addObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers();
}
```

Step 4: Implement Concrete Subject (Stock)
```java
// Stock.java
import java.util.ArrayList;
import java.util.List;

public class Stock implements Subject {
    private String stockName;
    private double price;
    private List<Observer> observers;

    public Stock(String stockName, double price) {
        this.stockName = stockName;
        this.price = price;
        this.observers = new ArrayList<>();
    }

    @Override
    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(stockName, price);
        }
    }

    // Method to update the stock price and notify observers
    public void setPrice(double newPrice) {
        this.price = newPrice;
        System.out.println("\nStock " + stockName + " price updated to $" + price);
        notifyObservers();
    }
}

```
**Using the design pattern**
```java
// Main.java
public class Main {
    public static void main(String[] args) {
        // Create a stock
        Stock appleStock = new Stock("AAPL", 150.0);

        // Create investors (observers)
        Observer investor1 = new Investor("Alice");
        Observer investor2 = new Investor("Bob");

        // Subscribe investors to the stock updates
        appleStock.addObserver(investor1);
        appleStock.addObserver(investor2);

        // Change the stock price (observers will be notified)
        appleStock.setPrice(155.0);
        appleStock.setPrice(160.0);

        // Unsubscribe an investor
        appleStock.removeObserver(investor1);
        appleStock.setPrice(165.0); // Only Bob gets notified
    }
}
```

