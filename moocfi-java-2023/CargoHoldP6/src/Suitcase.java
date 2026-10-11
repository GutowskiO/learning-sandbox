import java.util.ArrayList;

public class Suitcase {
    private int maxWeight;
    private ArrayList<Item> items;

    public Suitcase(int maxWeight) {
        this.maxWeight = maxWeight;
        this.items = new ArrayList<>();
    }

    public void addItem(Item item) {
        if (totalWeight() + item.getWeight() > maxWeight) {
            return;
        }

        this.items.add(item);
    }

    public void printItems() {
        for (Item item: this.items) {
            System.out.println(item);
        }
    }

    public int totalWeight() {
        int totalWeight = 0;
        for (Item item: this.items) {
            totalWeight += item.getWeight();
        }

        return totalWeight;
    }

    public Item heaviestItem() {
        if (this.items.isEmpty()) {
            return null;
        }

        Item heaviestItem = this.items.get(0);
        for (Item compared: this.items) {
            if (compared.getWeight() > heaviestItem.getWeight()) {
                heaviestItem = compared;
            }
        }

        return heaviestItem;
    }

    @Override
    public String toString() {
        if (this.items.size() == 0) {
            return "no items (" + totalWeight() + "kg)";
        }

        return this.items.size() +  " items (" + totalWeight() + "kg)";
    }
}
