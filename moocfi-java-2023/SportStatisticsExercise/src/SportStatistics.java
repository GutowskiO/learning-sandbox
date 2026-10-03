
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

public class SportStatistics {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        System.out.println("File?");
        String file = reader.nextLine();

        System.out.println("What team?");
        String whatTeam = reader.nextLine();

        int targetTeamWins = 0;
        int targetTeamLosses = 0;
        int targetGames = 0;

        try (Scanner fileReader = new Scanner(Paths.get(file))) {
            while (fileReader.hasNextLine()) {
                String line = fileReader.nextLine();
                String[] splitted = line.split(",");

                String team1 = splitted[0];
                String team2 = splitted[1];
                int score1 = Integer.valueOf(splitted[2]);
                int score2 = Integer.valueOf(splitted[3]);

                if (team1.equals(whatTeam)) {
                    if (score1 > score2) {
                        targetGames++;
                        targetTeamWins++;
                    } else {
                        targetGames++;
                        targetTeamLosses++;
                    }
                } else if (team2.equals(whatTeam)) {
                    if (score2 > score1) {
                        targetGames++;
                        targetTeamWins++;
                    } else {
                        targetGames++;
                        targetTeamLosses++;
                    }
                }
            }
        } catch (Exception e) {
            System.out.println("Error " + e.getMessage());
        }
        System.out.println("Games: " + targetGames + "\nWins: " + targetTeamWins + "\nLosses: " + targetTeamLosses);
    }

}
