import java.util.Scanner;

public class TextUI {
    private SimpleDictionary dictionary;
    private Scanner scanner;

    public TextUI(Scanner scanner, SimpleDictionary dictionary) {
        this.scanner = scanner;
        this.dictionary = dictionary;
    }

    public void start() {
        while (true) {
            System.out.print("Command: ");
            String input = scanner.nextLine();

            if (input.equals("end")) {
                System.out.println("Bye bye!");
                break;
            } else if (input.equals("add")) {
                System.out.print("Word: ");
                String word = scanner.nextLine();

                System.out.print("Translation: ");
                String translation = scanner.nextLine();

                dictionary.add(word, translation);
            } else if (input.equals("search")) {
                System.out.print("To be translated: ");
                String toTranslate = scanner.nextLine();

                if (dictionary.translate(toTranslate) == null) {
                    System.out.println("Word " + toTranslate + " was not found.");
                } else {
                    System.out.println(dictionary.translate(toTranslate));
                }
            } else {
                System.out.println("Unknown Command");
            }
        }
    }
}
