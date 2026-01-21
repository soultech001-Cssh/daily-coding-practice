import java.util.Scanner;

/**
 * Lucas Rabbit Counter - Calculates the Lucas Sequence
 * Similar to Fibonacci but with starting values 1 and 3.
 */
public class LucasRabbitCounter {

    public static void main(String[] args) {
        System.out.println("Please enter the month number: ");

        try (Scanner scanner = new Scanner(System.in)) {
            int month = scanner.nextInt();
            int result = calculateLucasNumber(month);
            System.out.println("\nThe total number of rabbits in month " + month + " is: " + result + "\n");
        } catch (Exception e) {
            System.out.println(" -- Calculation Error --");
        } finally {
            System.out.println(" -- Complete --");
        }
    }

    /**
     * Calculates the Lucas number for the given position.
     *
     * @param month the position in the Lucas sequence
     * @return the Lucas number at that position
     */
    private static int calculateLucasNumber(int month) {
        if (month == 1) {
            return 1;
        }
        if (month == 2) {
            return 3;
        }
        return calculateLucasNumber(month - 1) + calculateLucasNumber(month - 2);
    }
}
