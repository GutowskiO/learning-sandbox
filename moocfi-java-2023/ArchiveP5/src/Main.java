
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Item> items = new ArrayList<>();

        while (true) {
            System.out.println("Identifier? (empty will stop)");
            String temporaryIndentifer = scanner.nextLine();

            if (temporaryIndentifer.isEmpty()) {
                break;
            }

            System.out.println("Name? (empty will stop)");
            String temporaryName = scanner.nextLine();

            if (temporaryName.isEmpty()) {
                break;
            }

            Item temporaryItem = new Item(temporaryIndentifer, temporaryName);
            if (!(items.contains(temporaryItem))) {
                items.add(temporaryItem);
            }
        }
        System.out.println("==Items==");
        for (Item item: items) {
            System.out.println(item);
        }

    }
}
