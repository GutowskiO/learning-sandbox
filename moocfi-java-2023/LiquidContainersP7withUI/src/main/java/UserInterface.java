import java.util.Scanner;

public class UserInterface {

    private Scanner scanner;
    private Container first;
    private Container second;

    public UserInterface(Scanner scanner, Container first, Container second) {
        this.scanner = scanner;
        this.first = first;
        this.second = second;
    }

    public void start() {

        while (true) {
            System.out.println("First: " + first);
            System.out.println("Second: " + second);

            String input = scanner.nextLine();

            if (input.equals("quit")) {
                break;
            }

            String[] parts = input.split(" ");
            int amount = Integer.valueOf(parts[1]);

            switch (parts[0]) {
                case "add" -> this.first.add(amount);
                case "remove" -> this.second.remove(amount);
                case "move" -> this.second = this.first.moveToAnother(amount, this.second);
            }
        }
    }
}
