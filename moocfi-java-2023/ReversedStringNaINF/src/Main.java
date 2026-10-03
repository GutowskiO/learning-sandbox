
import java.nio.file.Paths;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        System.out.print("Give the name of the file/Podaj nazwe pliku: ");
        String name = reader.nextLine();

        System.out.println(reversedString(contentOfFile(name)));
    }

    private static String reversedString(String str) {
        StringBuilder reversed = new StringBuilder();

        for (int i = str.length() -1; i >= 0; i--) {
            reversed.append(str.charAt(i));
        }

        return reversed.toString();
    }

    private static String contentOfFile (String fileName) {
        StringBuilder content = new StringBuilder();

        try (Scanner fileReader = new Scanner(Paths.get(fileName))) {

            while (fileReader.hasNextLine()) {
                content.append(fileReader.nextLine());
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        return content.toString();
    }
}
