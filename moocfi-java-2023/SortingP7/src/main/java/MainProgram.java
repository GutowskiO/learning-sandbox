import java.util.Arrays;

public class MainProgram {

    public static void main(String[] args) {
        int[] numbers = {8, 3, 7, 9, 1, 2, 4};
        MainProgram.sort(numbers);
    }

    public static int smallest(int[] array) {
        int smallest = array[0];

        for (int number: array) {
            if (smallest > number) {
                smallest = number;
            }
        }

        return smallest;
    }

    public static int indexOfSmallest(int[] array) {
        int i = 0;

        for (int number: array) {
            if (number == smallest(array)) {
                return i;
            }

            i++;
        }

        return -1;
    }

    public static int indexOfSmallestFrom(int[] array, int i) {

        int j = i;
        int smallest = array[i];

        for (i = i; i < array.length; i++) {
            if (smallest > array[i]) {
                smallest = array[i];
            }
        }

        for (j = j; j < array.length; j++) {

            if (array[j] == smallest) {
                return j;
            }
        }

        return -1;
    }

    public static void swap(int[] array, int index1, int index2) {
        int index2value = array[index1];

        array[index1] = array[index2];
        array[index2] = index2value;
    }


    public static void sort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.println(Arrays.toString(array));
            swap(array, i, indexOfSmallestFrom(array, i));
        }
    }
}
