import java.util.Scanner;

public class DayOfYearCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Accept year, month, and day as input
        System.out.print("Enter year: ");
        int year = scanner.nextInt();

        System.out.print("Enter month: ");
        int month = scanner.nextInt();

        System.out.print("Enter day: ");
        int day = scanner.nextInt();

        // Array storing the number of days for each month in a non-leap year
        int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        // Check if the year is a leap year
        boolean isLeapYear = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);

        // Calculate the day of the year
        int dayOfYear = 0;

        // Sum the days of the months preceding the current month
        for (int i = 0; i < month - 1; i++) {
            dayOfYear += daysInMonth[i];
        }

        // Add the current day
        dayOfYear += day;

        // If leap year and month is greater than 2, add 1 to the total
        if (isLeapYear && month > 2) {
            dayOfYear += 1;
        }

        // Output the result
        System.out.println("Day of year: " + dayOfYear);

        scanner.close();
    }
}
