
import java.nio.file.Paths;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        int counter = 0;

        System.out.println("File?");
        String file = reader.nextLine();

        System.out.println("Lower bound?");
        int lowerBound = Integer.valueOf(reader.nextLine());

        System.out.println("Upper bound?");
        int upperBound = Integer.valueOf(reader.nextLine());

        try (Scanner scanner = new Scanner(Paths.get(file))) {
            while (scanner.hasNextLine()) {
                int number = Integer.valueOf(scanner.nextLine());
                if (number >= lowerBound && number <= upperBound) {
                    counter++;
                }
            }
        } catch (Exception e) {
            System.out.println("Error " + e.getMessage());
        }
        System.out.println("Numbers: " + counter);
    }
}

