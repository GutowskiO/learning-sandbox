public class PaymentCard {
    private double balance;
    public PaymentCard(int balance) {
        this.balance = balance;
    }

    public String toString() {
        return "The card has a balance of " + this.balance + " euros";
    }
    public void eatAffordably() {
        if (this.balance >= 2.60) {
            this.balance -= 2.60;
        } else {
            System.out.println("Not enough funds on the card!");
        }
    }

    public void eatHeartily() {
        if (this.balance >= 4.60) {
            this.balance -= 4.60;
        } else {
            System.out.println("Not enough funds on the card!");
        }
    }
    public void addMoney(double amount) {
        if (amount < 0) {
            System.out.println("You can't top up your card with a negative value!");
            return;
        }

        double sum = this.balance + amount;

        if (sum > 150) {
            this.balance = 150.0;
        } else {
            this.balance = sum;
        }
    }
}