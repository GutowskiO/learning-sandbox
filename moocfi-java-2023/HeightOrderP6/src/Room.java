import java.util.ArrayList;

public class Room {
    private ArrayList<Person> persons;
    public Room() {
        this.persons = new ArrayList<>();
    }

    public void add(Person person) {
        this.persons.add(person);
    }

    public boolean isEmpty() {
        if (this.persons.isEmpty()) {
            return true;
        }

        return false;
    }

    public ArrayList<Person> getPersons() {
        return this.persons;
    }

    public Person shortest() {
        if (this.persons.isEmpty()) {
            return null;
        }

        Person shortest = this.persons.get(0);
        for (Person compared: this.persons) {
            if (shortest.getHeight() > compared.getHeight()) {
                shortest = compared;
            }
        }

        return shortest;
    }

    public Person take() {
        Person shortest = shortest();
        this.persons.remove(shortest());
        return shortest;
    }
}
