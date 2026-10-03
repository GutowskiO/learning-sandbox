public class Container {

    private int amount;

    public Container() {
        this.amount = 0;
    }

    public void add(int amount) {
        int afterAddition = this.amount + amount;

        if (afterAddition > 100) {
            this.amount = 100;
            return;
        }

        this.amount = afterAddition;
    }

    public void remove(int amount) {
       int afterSubstraction = this.amount - amount;

        if (afterSubstraction < 0) {
            this.amount = 0;
            return;
        }

        this.amount -= amount;
    }

    public int contains() {
        return this.amount;
    }

    public Container moveToAnother(int amount, Container movedTo) {
        if (this.amount >= amount) {
            this.remove(amount);
            movedTo.add(amount);
        } else {
            movedTo.add(this.amount);
            this.amount = 0;
        }

        return movedTo;
    }

    @Override
    public String toString() {
        return this.amount + "/100";
    }
}
