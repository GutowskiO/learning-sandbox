
public class HealthStation {
    private int numberOfWeighnings;

    public int weigh(Person person) {
        numberOfWeighnings++;
        return person.getWeight();
    }
    public void feed(Person person) {
        person.setWeight(person.getWeight() + 1);
    }
    public int weighings() {
        return this.numberOfWeighnings;
    }
}
