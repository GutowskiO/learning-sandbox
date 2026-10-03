import java.util.ArrayList;

public class Stack {
    private ArrayList<String> stack;

    public Stack() {
        this.stack = new ArrayList<>();
    }

    public boolean isEmpty() {
        if (this.stack.isEmpty()) {
            return true;
        }

        return false;
    }

    public void add(String value) {
        this.stack.add(0, value);
    }

    public ArrayList<String> values() {
        return this.stack;
    }

    public String take() {
        String returned = this.stack.get(0);
        this.stack.remove(0);

        return returned;
    }
}
