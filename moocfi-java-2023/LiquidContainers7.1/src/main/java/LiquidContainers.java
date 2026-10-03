
import java.util.Scanner;
import java.util.ArrayList;

public class LiquidContainers {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int firstContainer = 0;
        int secondContainer = 0;

        while (true) {
            System.out.println("First: "+ firstContainer + "/100");
            System.out.println("Second: "+ secondContainer + "/100");
            String input = scan.nextLine();
            String[] parts = input.split(" ");
            if (parts.length == 1) {
                if (parts[0].equals("quit")) {
                    break;
                }
            } else {
                String command = parts[0];
                int amount = Integer.valueOf(parts[1]);
                switch (command) {
                    case "add":
                        if (firstContainer + amount <= 100 && amount >= 0) {
                            firstContainer += amount;
                        } else {
                            firstContainer = 100;
                        }
                        break;
                    case "move":
                        if (firstContainer - amount >= 0 && amount >= 0) {
                            if (secondContainer + amount <= 100) {
                                if (amount <= firstContainer) {
                                    firstContainer -= amount;
                                    secondContainer += amount;
                                } else {
                                    firstContainer = 0;
                                    secondContainer += amount;
                                }
                            } else {
                                firstContainer -= amount;
                                secondContainer = 100;
                            }
                        } else {
                            secondContainer += firstContainer;
                            firstContainer = 0;

                        }      
                        break;
                    case "remove":
                        if (secondContainer - amount >= 0 && secondContainer - amount <= 100) {
                            secondContainer -= amount;
                        } else {
                            secondContainer = 0;
                        }    
                }    
            }         
        }
    }
}