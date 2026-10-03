import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        // implement here your program that uses the TelevisionProgram class

        ArrayList<TelevisionProgram> programs = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Name: ");
            String name = scanner.nextLine();

            if (name.isEmpty()) {
                break;
            }

            System.out.print("Duration: ");
            int duration = Integer.valueOf(scanner.nextLine());

            programs.add(new TelevisionProgram(name,duration));
        }

        System.out.print("Programs maximum duration? ");
        int maxduration = Integer.valueOf(scanner.nextLine());

        for (int i = 0; i < programs.size() -1; i++) {
            if (programs.get(i).getDuration() <= maxduration) { // można to zrobić za pomocą int container: programs w for loopie
                System.out.println(programs.get(i));
            }
        }
    }
}
