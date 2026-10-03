import java.util.Scanner;

public class AVClub {
    public  static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] arrayOfStrings = null;
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            } else {
                arrayOfStrings = input.split(" ");
            }
            for (int i = 0; i < arrayOfStrings.length; i++) {
                if (arrayOfStrings[i].contains("av")) {
                    System.out.println(arrayOfStrings[i]);
                }
            }
        }
    }
}