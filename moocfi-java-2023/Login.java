import java.util.Scanner;

public class Login {
    public  static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter username: ");
        String username = scanner.nextLine();

        System.out.print("Enter password: ");
        String password = scanner.nextLine();

        String firstUser = "alex";
        String firstPass = "sunshine";
        String secondUser = "emma";
        String secondPass = "haskell";

        if (username.equals(firstUser) && password.equals(firstPass) || username.equals(secondUser) && password.equals(secondPass)) {
            System.out.println("You have successfully logged in!");
        } else {
            System.out.println("Incorrect username or password!");
        }
    }
}