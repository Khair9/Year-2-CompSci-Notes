# [Faxtory Design](https://github.com/Khair9/Year-2-CompSci-Notes/blob/main/OOSE2/Design%20Patterns.md)
**What:**
The Factory Pattern is a creational design pattern that provides an interface for creating objects without specifying their exact class. It encapsulates object creation, making the code more flexible and maintainable.


**When:**
- When you need to create objects without exposing the instantiation logic to the client.
- When you have a common interface and multiple concrete implementations.
- When object creation involves complex logic, and you want to keep it separate from business logic.

**Why:**
- **Encapsulation of Object Creation:** The client does not need to know class instantiation details.
- **Loose Coupling:** The client depends only on the factory and the interface, not concrete classes.
- **Code Maintainability:** New shapes can be added without modifying the existing client code.
- **Simplifies Object Creation Logic:** Complex instantiation logic is centralized in the factory.

## Example factory design implementation:
**Step 1: Define the Product Interface**
```java
// Shape.java
public interface Shape {
    void draw();
}
```
**Step 2: Implement Concrete Products**

```java
// Circle.java
public class Circle implements Shape {
    @Override
    public void draw() {
        System.out.println("Drawing a Circle");
    }
}

```

```java
// Rectangle.java
public class Rectangle implements Shape {
    @Override
    public void draw() {
        System.out.println("Drawing a Rectangle");
    }
}

```

```java
// Square.java
public class Square implements Shape {
    @Override
    public void draw() {
        System.out.println("Drawing a Square");
    }
}

```
**Step 3: Create the Factory Class**

```java
// ShapeFactory.java
public class ShapeFactory {
    // Factory method to create objects
    public static Shape getShape(String shapeType) {
        if (shapeType == null) {
            return null;
        }
        switch (shapeType.toLowerCase()) {
            case "circle":
                return new Circle();
            case "rectangle":
                return new Rectangle();
            case "square":
                return new Square();
            default:
                throw new IllegalArgumentException("Unknown shape type: " + shapeType);
        }
    }
}
```

```java
// Main.java
public class Main {
    public static void main(String[] args) {
        // Create a Circle
        Shape circle = ShapeFactory.getShape("circle");
        circle.draw();

        // Create a Rectangle
        Shape rectangle = ShapeFactory.getShape("rectangle");
        rectangle.draw();

        // Create a Square
        Shape square = ShapeFactory.getShape("square");
        square.draw();
    }
}
```



