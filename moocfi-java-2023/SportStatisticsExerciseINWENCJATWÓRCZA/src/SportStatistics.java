
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Scanner;

public class SportStatistics {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);

        System.out.println("File:");
        String file = reader.nextLine();

        System.out.println("Team:");
        String whatTeam = reader.nextLine();

        Team ENCE = new Team("ENCE");
        Team Vitality = new Team("Vitality");
        Team FURIA = new Team("FURIA");
        Team NRG = new Team("NRG");
        Team Prospects = new Team("Prospects");
        Team Heroic = new Team("Heroic");
        Team SK = new Team("SK");

        HashMap<String, Team> mapOfTeams = new HashMap<>();

        mapOfTeams.put("ENCE", ENCE);
        mapOfTeams.put("Vitality", Vitality);
        mapOfTeams.put("FURIA", FURIA);
        mapOfTeams.put("NRG", NRG);
        mapOfTeams.put("Prospects", Prospects);
        mapOfTeams.put("Heroic", Heroic);
        mapOfTeams.put("SK", SK);

        try (Scanner readFile = new Scanner(Paths.get(file))) {
            while (readFile.hasNextLine()) {
                String line = readFile.nextLine();

                String[] splitted = line.split(",");

                String team1 = splitted[0];
                String team2 = splitted[1];
                int score1 = Integer.valueOf(splitted[2]);
                int score2 = Integer.valueOf(splitted[3]);

                if (score1 > score2) {
                    mapOfTeams.get(team1).addGames();
                    mapOfTeams.get(team1).addWins();
                    mapOfTeams.get(team2).addLosses();
                    mapOfTeams.get(team2).addGames();
                } else {
                    mapOfTeams.get(team1).addGames();
                    mapOfTeams.get(team2).addWins();
                    mapOfTeams.get(team1).addLosses();
                    mapOfTeams.get(team2).addGames();
                }
            }
        } catch (Exception e) {
            System.out.println("Error " + e.getMessage());
        }
        System.out.println("Games: " + mapOfTeams.get(whatTeam).getGames());
        System.out.println("Wins: " + mapOfTeams.get(whatTeam).getWins());
        System.out.println("Losses: " + mapOfTeams.get(whatTeam).getLosses());
    }
}
