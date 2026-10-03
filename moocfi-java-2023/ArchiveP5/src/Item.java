public class Item {
    private String indentifer;
    private String name;

    public Item(String indentifer, String name) {
        this.indentifer = indentifer;
        this.name = name;
    }

    public boolean equals(Object compared) {
        if (this == compared) {
            return true;
        }

        if (!(compared instanceof Item)) {
            return false;
        }
        Item comparedItem = (Item) compared;

        return this.indentifer.equals(comparedItem.indentifer);
    }

    @Override
    public String toString() {
        return this.indentifer + ": " + this.name;
    }
}
