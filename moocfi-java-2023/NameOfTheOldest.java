import java.util.Scanner;

public class NameOfTheOldest {
    public  static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int oldest = 0;
        String nameOfTheOldest = null;

        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            }
            String[] arrayOfStrings = input.split(",");
            int current = Integer.valueOf(arrayOfStrings[1]);

            if (current > oldest) {
                oldest = current;
                nameOfTheOldest = arrayOfStrings[0];
            }
        }
        System.out.println(nameOfTheOldest);
    }
}