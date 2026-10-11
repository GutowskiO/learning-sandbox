public class PaymentTerminal {
    private double money;  // amount of cash
    private int affordableMeals; // number of sold affordable meals
    private int heartyMeals;  // number of sold hearty meals

    public PaymentTerminal() {
        this.money = 1000;
    }

    public double eatAffordably(double payment) {
        if (payment < 2.50) {
            return payment;
        }

        this.affordableMeals++;
        this.money += 2.50;
        return payment - 2.50;
    }

    public double eatHeartily(double payment) {
        if (payment <  4.30) {
            return payment;
        }

        this.heartyMeals++;
        this.money += 4.30;
        return payment -  4.30;
    }

    public boolean eatAffordably(PaymentCard card) {
        if (card.balance() < 2.5) {
            return false;
        }

        affordableMeals++;
        card.takeMoney(2.5);
        return true;
    }

    public boolean eatHeartily(PaymentCard card) {
        if (card.balance() < 4.3) {
            return false;
        }

        heartyMeals++;
        card.takeMoney(4.3);
        return true;
    }

    public void addMoneyToCard(PaymentCard card, double sum) {
        card.addMoney(sum);
        this.money += sum;
    }

    public String toString() {
        return "money: " + money + ", number of sold afforable meals: " + affordableMeals + ", number of sold hearty meals: " + heartyMeals;
    }
}
