import java.util.ArrayList;

public class TodoList {
    private ArrayList<String> list;

    public TodoList() {
        this.list = new ArrayList<>();
    }

    public void add(String string) {
        list.add(string);
    }

    public void remove(int index) {
        list.remove(index - 1);
    }

    public void print() {
        int counter = 1;
        for (String print: list) {
            System.out.println(counter + ". " + print);
            counter++;
        }
    }
}
