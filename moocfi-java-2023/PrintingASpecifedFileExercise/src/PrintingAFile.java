
import java.nio.file.Paths;
import java.util.Scanner;

public class PrintingAFile {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        System.out.println("Which file should have its contents printed?");
        String printed = reader.nextLine();

        try (Scanner scanner = new Scanner(Paths.get(printed))) {

            while (scanner.hasNextLine()) {
                String oneRow = scanner.nextLine();
                System.out.println(oneRow);
            }
        } catch (Exception e) {
            System.out.println("Error " + e.getMessage());
        }
    }
}
