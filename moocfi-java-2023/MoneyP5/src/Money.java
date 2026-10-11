
public class Money {

    private final int euros;
    private final int cents;

    public Money(int euros, int cents) {

        if (cents > 99) {
            euros = euros + cents / 100;
            cents = cents % 100;
        }

        this.euros = euros;
        this.cents = cents;
    }

    public int euros() {
        return this.euros;
    }

    public int cents() {
        return this.cents;
    }

    public Money plus(Money addition) {
        Money newMoney = new Money(this.euros + addition.euros, this.cents + addition.cents);

        return newMoney;
    }

    public Money minus(Money decreaser) {
        double currentMoney = this.euros * 100 + this.cents;
        double minusMoney = decreaser.euros * 100 + decreaser.cents;

        double distinction = currentMoney - minusMoney;

        if (distinction < 0) {
            return new Money(0, 0);
        }

        double almostFinalEuros = this.euros - decreaser.euros;
        double almostFinalCents = this.cents - decreaser.cents;

        if (almostFinalCents < 0) {
            int finalEuros = (int) (almostFinalEuros - 2);
            int finalCents = (int) (100 - almostFinalCents);

            return new Money(finalEuros, finalCents);
        }

        return new Money((int) almostFinalEuros, (int) almostFinalEuros);
    }

    public boolean lessThan(Money compared) {
        if (this.euros > compared.euros) {
            return false;
        } else if (this.euros == compared.euros) {
            if (this.cents > compared.cents) {
                return false;
            }
        }

        return true;
    }

    public String toString() {
        String zero = "";
        if (this.cents < 10) {
            zero = "0";
        }

        return this.euros + "." + zero + this.cents + "e";
    }

}
