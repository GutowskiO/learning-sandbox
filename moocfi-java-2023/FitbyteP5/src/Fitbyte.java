
public class Fitbyte {
    private double maxHR;
    private int age;
    private int restingHR;
    public Fitbyte(int age, int restingHR) {
        this.age = age;
        this.restingHR = restingHR;
        this.maxHR = 206.3 - (0.711 * age);
    }
    public double targetHR(double percentageOfMaximum) {
        return (maxHR - restingHR) * (percentageOfMaximum) + restingHR;
    }
}