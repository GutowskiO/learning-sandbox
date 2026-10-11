import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Main {

    public static void main(String[] args) {
        // insert test code here
        int[] array = {3, 1, 5, 99, 3, 12};
        ArrayList<Integer> list = new ArrayList<>();

        list.add(5);
        list.add(2);
        list.add(10);
        System.out.println(list);
        sortIntegers(list);
        System.out.println(list);

        System.out.println(Arrays.toString(array));
        sort(array);
        System.out.println(Arrays.toString(array));
    }

    public static void sort(int[] array) {
        Arrays.sort(array);
    }

    public static void sort(String[] array) {
        Arrays.sort(array);
    }

    public static void sortIntegers(ArrayList<Integer> list) {
        Collections.sort(list);
    }

    public static void sortStrings (ArrayList<String> list) {
        Collections.sort(list);
    }

}
