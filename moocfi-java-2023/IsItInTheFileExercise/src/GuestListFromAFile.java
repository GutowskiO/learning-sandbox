
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

public class GuestListFromAFile {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<>();

        System.out.println("Name of the file:");
        String file = reader.nextLine();

        System.out.println("Search for:");
        String search = reader.nextLine();

        try (Scanner scanner = new Scanner(Paths.get(file))) {
            while (scanner.hasNextLine()) {
                list.add(scanner.nextLine());
            }
        } catch (Exception e) {
            System.out.println("Reading the file " + file + " failed");
        }

        if (list.contains(search)) {
            System.out.println("Found!");
        } else {
            System.out.println("Not found.");
        }
    }
}