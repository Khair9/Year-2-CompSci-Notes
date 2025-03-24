# [Decorator Pattern](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/OOSE2/Design%20Patterns.md)

**What:**
The Decorator Pattern is a structural design pattern that allows behavior to be added to individual objects, dynamically, without modifying the code of the original class.

**When to Use the Decorator Pattern**
- When you want to extend the behavior of an object at runtime without modifying its structure.
- When subclassing leads to too many classes (instead of creating multiple subclasses, decorators can be stacked dynamically).
- When following the Open/Closed Principle (open for extension, closed for modification).

**Why Decorator pattern**
 - Flexibility
 - Avoids Subclass Explosion: Instead of creating multiple subclasses for combinations (e.g., CoffeeWithMilkAndSugar), decorators allow dynamic stacking.
 - Follows Open/Closed Principle: New features (decorators) can be added without modifying the existing code.

## Example Implementation in Java
**Step 1: Define the Component Interface**
```java
// Coffee.java
public interface Coffee {
    double getCost();
    String getDescription();
}
```
**Step 2: Implement the Concrete Component**
```java
// SimpleCoffee.java
public class SimpleCoffee implements Coffee {
    @Override
    public double getCost() {
        return 5.0; // Base cost
    }

    @Override
    public String getDescription() {
        return "Simple Coffee";
    }
}
```
**Step 3: Create an Abstract Decorator**
```java
// CoffeeDecorator.java
public abstract class CoffeeDecorator implements Coffee {
    protected Coffee decoratedCoffee;

    public CoffeeDecorator(Coffee coffee) {
        this.decoratedCoffee = coffee;
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost();
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription();
    }
}

```
**Step 4: Implement Concrete Decorators**
(note the extends operator on the second line)
```java
// MilkDecorator.java
public class MilkDecorator extends CoffeeDecorator {
    public MilkDecorator(Coffee coffee) {
        super(coffee);
    }

    @Override
    public double getCost() {
        return super.getCost() + 1.5; // Adding milk cost
    }

    @Override
    public String getDescription() {
        return super.getDescription() + ", Milk";
    }
}
```

```java
// SugarDecorator.java
public class SugarDecorator extends CoffeeDecorator {
    public SugarDecorator(Coffee coffee) {
        super(coffee);
    }

    @Override
    public double getCost() {
        return super.getCost() + 0.5; // Adding sugar cost
    }

    @Override
    public String getDescription() {
        return super.getDescription() + ", Sugar";
    }
}
```
**Using Implementation:**
``` java
// Main.java
public class Main {
    public static void main(String[] args) {
        // Base Coffee
        Coffee coffee = new SimpleCoffee();
        System.out.println(coffee.getDescription() + " -> Cost: $" + coffee.getCost());

        // Adding Milk
        coffee = new MilkDecorator(coffee);
        System.out.println(coffee.getDescription() + " -> Cost: $" + coffee.getCost());

        // Adding Sugar
        coffee = new SugarDecorator(coffee);
        System.out.println(coffee.getDescription() + " -> Cost: $" + coffee.getCost());

        // Adding another layer of Sugar
        coffee = new SugarDecorator(coffee);
        System.out.println(coffee.getDescription() + " -> Cost: $" + coffee.getCost());
    }
}
```
**outputs**
```pgsql
Simple Coffee -> Cost: $5.0
Simple Coffee, Milk -> Cost: $6.5
Simple Coffee, Milk, Sugar -> Cost: $7.0
Simple Coffee, Milk, Sugar, Sugar -> Cost: $7.5


```
