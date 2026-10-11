import java.util.Scanner;

public class LineByLine {
    public  static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] stuffToPrint = null;
        while (true) {
            String input = scanner.nextLine();
            if (input.equals("")) {
                break;
            } else {
                stuffToPrint = input.split(" ");
            }
            for (int i = 0; i < stuffToPrint.length; i++) {
                System.out.println(stuffToPrint[i]);
            }
        }
    }
}