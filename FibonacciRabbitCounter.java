import java.util.Scanner;

public class FibonacciRabbitCounter {

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Please input the month number: ");
            int monthNumber = scanner.nextInt();

            System.out.println("\nThe total number of rabbits in month " + monthNumber
                    + " is: " + calculateFibonacci(monthNumber) + "\n");
        } catch (Exception e) {
            System.out.println(" -- Calculation Error --");
        } finally {
            System.out.println(" -- Done --");
        }
    }

    private static int calculateFibonacci(int n) {
        if (n == 1 || n == 2) {
            return 1;
        } else {
            return calculateFibonacci(n - 1) + calculateFibonacci(n - 2);
        }
    }
}
