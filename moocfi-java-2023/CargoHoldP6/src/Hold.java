import java.util.ArrayList;

public class Hold {
    private int maxWeight;
    private int totalWeight;
    private ArrayList<Suitcase> luggages;

    public Hold(int maxWeight) {
        this.maxWeight = maxWeight;
        this.totalWeight = 0;
        this.luggages = new ArrayList<>();
    }

    public void addSuitcase(Suitcase suitcase) {
        if (this.totalWeight + suitcase.totalWeight() > maxWeight) {
            return;
        }

        this.totalWeight += suitcase.totalWeight();
        this.luggages.add(suitcase);
    }

    public void printItems() {
        for (Suitcase suitcase: this.luggages) {
            suitcase.printItems();
        }
    }

    @Override
    public String toString() {
        return luggages.size() + " suitcases (" + this.totalWeight + "kg)";
    }
}
