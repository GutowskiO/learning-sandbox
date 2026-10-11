public class Team {
    private String name;
    private int games;
    private int wins;
    private int losses;
    public Team(String name) {
        this.name = name;
        this.games = 0;
        this.wins = 0;
        this.losses = 0;
    }
    public int getGames() {
        return this.games;
    }
    public int getWins() {
        return this.wins;
    }
    public int getLosses() {
        return this.losses;
    }
    public void addGames() {
        this.games++;
    }
    public void addWins() {
        this.wins++;
    }
    public void addLosses() {
        this.losses++;
    }

    @Override
    public String toString() {
        return "Games: "+ this.games;
    }
}
