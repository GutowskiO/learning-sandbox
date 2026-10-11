import java.util.Scanner;

public class PersonalDetails {
    public  static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] arrayOfStrings = {};
        int longest = 0;
        int sumOfTheYears = 0;
        int counter = 0;
        String nameLongest = null;

        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            arrayOfStrings = input.split(",");
            int current = arrayOfStrings[0].length();

            sumOfTheYears = sumOfTheYears + Integer.valueOf(arrayOfStrings[1]);
            counter++;

            if (current > longest) {
                longest = current;
                nameLongest = arrayOfStrings[0];
            }
        }

        if (!(arrayOfStrings.length == 0)) {
            System.out.println("Longest name: " + nameLongest);
            double average = 1.0 * sumOfTheYears / counter;
            System.out.println("Average of the birth years: " + average);
        } else {
            System.out.println("No input!");
        }

    }
}