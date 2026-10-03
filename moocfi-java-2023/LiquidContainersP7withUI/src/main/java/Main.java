import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Container first = new Container();
        Container second = new Container();

        UserInterface ui = new UserInterface(scanner, first, second);
        ui.start();

    }

}
