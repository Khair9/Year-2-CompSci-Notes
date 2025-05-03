import java.util.Scanner;
import java.util.Arrays;

public class MyClass {
    static boolean exit = false;

    public static void main(String args[]) {
        System.out.println("CALC STARTING UP\n#############################################################");

        Scanner scanner = new Scanner(System.in);
        String userInput = "";

        System.out.println("TYPE 'exit' TO QUIT:");
        System.out.println("FORMAT: <input a> <operation> <input b>");
        System.out.println("EXAMPLE: 1 + 1");
        System.out.println("OPERATIONS:");
        System.out.println("+");
        System.out.println("-");
        System.out.println("*");
        System.out.println("/");
        System.out.println("modulus = %");
        System.out.println("power = ^");
        System.out.println("#############################################################");

        while (!exit) {
            System.out.print("\nCALC: ");
            userInput = scanner.nextLine();

            if (userInput.equalsIgnoreCase("exit")) {
                exit = true;
                continue;
            }

            String[] processedUserInput = userInput.split(" ");
            if (processedUserInput.length != 3) {
                System.out.println("Invalid format. Use: <number> <operator> <number> (e.g., 5 * 2)");
                continue;
            }

            try {
                double num1 = Double.parseDouble(processedUserInput[0]);
                String operator = processedUserInput[1];
                double num2 = Double.parseDouble(processedUserInput[2]);
                double result;

                switch (operator) {
                    case "+":
                        result = calcAdd(num1, num2);
                        break;
                    case "-":
                        result = calcSub(num1, num2);
                        break;
                    case "*":
                        result = calcMul(num1, num2);
                        break;
                    case "/":
                        if (num2 == 0) {
                            System.out.println("Error: Cannot divide by zero.");
                            continue;
                        }
                        result = calcDiv(num1, num2);
                        break;
                    case "%":
                        result = calcMod(num1, num2);
                        break;
                    case "^":
                        result = calcPow(num1, num2);
                        break;
                    default:
                        System.out.println("Unsupported operator: " + operator);
                        continue;
                }

                System.out.println("Result: " + result);

            } catch (NumberFormatException e) {
                System.out.println("Invalid number format.");
            }
        }

        System.out.println("SHUTTING DOWN CALC");
        scanner.close();
    }

    public static double calcAdd(double a, double b) {
        return a + b;
    }

    public static double calcSub(double a, double b) {
        return a - b;
    }

    public static double calcMul(double a, double b) {
        return a * b;
    }

    public static double calcDiv(double a, double b) {
        return a / b;
    }

    public static double calcMod(double a, double b) {
        return a % b;
    }

    public static double calcPow(double a, double b) {
        return Math.pow(a, b);
    }
}
