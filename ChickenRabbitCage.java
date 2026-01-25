import java.util.Scanner;

/**
 * Chicken and Rabbit Cage Problem Solver
 *
 * Classic math problem: Given the total number of heads and feet in a cage
 * containing only chickens (2 feet each) and rabbits (4 feet each),
 * calculate how many of each animal there are.
 *
 * Mathematical formula:
 * - Let H = total heads, F = total feet
 * - Let C = chickens, R = rabbits
 * - C + R = H (each animal has one head)
 * - 2C + 4R = F (chickens have 2 feet, rabbits have 4)
 * - Solving: R = (F - 2H) / 2, C = H - R
 */
public class ChickenRabbitCage {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter total number of heads: ");
        int totalHeads = scanner.nextInt();

        System.out.print("Enter total number of feet: ");
        int totalFeet = scanner.nextInt();

        scanner.close();

        // Validation: Check for non-negative inputs
        if (totalHeads < 0) {
            System.out.println("Error: Total heads cannot be negative.");
            return;
        }

        if (totalFeet < 0) {
            System.out.println("Error: Total feet cannot be negative.");
            return;
        }

        // Validation: Total feet must be even (chickens have 2, rabbits have 4)
        if (totalFeet % 2 != 0) {
            System.out.println("Error: Total feet must be an even number.");
            return;
        }

        // Calculate number of rabbits: R = (Feet - 2 * Heads) / 2
        int rabbits = (totalFeet - 2 * totalHeads) / 2;

        // Calculate number of chickens: C = Heads - R
        int chickens = totalHeads - rabbits;

        // Validation: Check that calculated values are not negative
        if (rabbits < 0) {
            System.out.println("Error: Invalid input - too few feet for the given number of heads.");
            return;
        }

        if (chickens < 0) {
            System.out.println("Error: Invalid input - too many feet for the given number of heads.");
            return;
        }

        // Validation: Verify the solution is correct (sanity check)
        int calculatedFeet = (chickens * 2) + (rabbits * 4);
        if (calculatedFeet != totalFeet) {
            System.out.println("Error: No valid solution exists for the given inputs.");
            return;
        }

        // Output the results
        System.out.println("Number of chickens: " + chickens);
        System.out.println("Number of rabbits: " + rabbits);
    }
}
