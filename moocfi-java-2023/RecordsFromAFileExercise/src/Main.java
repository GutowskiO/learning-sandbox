
import java.nio.file.Paths;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        System.out.println("Name of the file:");
        String file = reader.nextLine();

        try (Scanner scanner = new Scanner(Paths.get(file))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] seperation = line.split(",");

                System.out.println(seperation[0] + ", age: " + seperation[1] + " years");
            }
        } catch (Exception e) {
            System.out.println("Error " + e.getMessage());
        }
    }
}