import java.util.Scanner;

public class UserInterface {

    private JokeManager jokeManager;
    private Scanner scanner;

    public UserInterface(JokeManager jokeManager, Scanner scanner) {
        this.jokeManager = jokeManager;
        this.scanner = scanner;
    }

    public void start() {
        while (true) {
            System.out.println("Commands:\n" +
                    "1 - add a joke\n" +
                    "2 - draw a joke\n" +
                    "3 - list jokes\n" +
                    "X - stop");

            String input = scanner.nextLine();

            if (input.equals("X")) {
                break;
            }

            if (input.equals("1")) {
                System.out.println("Write the joke to be added: ");
                String joke = scanner.nextLine();

                this.jokeManager.addJoke(joke);
            }

            if (input.equals("2")) {
                System.out.println(this.jokeManager.drawJokes());
            }

            if (input.equals("3")) {
                System.out.println("Printing the jokes.");
                this.jokeManager.printJokes();
            }
        }
    }
}
