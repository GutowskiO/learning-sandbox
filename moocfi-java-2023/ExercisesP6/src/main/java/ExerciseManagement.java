import java.util.ArrayList;

public class ExerciseManagement {

    private ArrayList<Exercise> exercises;

    public ExerciseManagement() {
        this.exercises = new ArrayList<>();
    }

    public ArrayList<String> exerciseList() {
        ArrayList<String> list = new ArrayList<>();

        for (Exercise exercise: this.exercises) {
            list.add(exercise.getName());
        }

        return list;
    }

    public void add(String added) {
        this.exercises.add(new Exercise(added));
    }

    public void markAsCompleted(String completed) {
        for (Exercise ex: this.exercises) {
            if (completed.equals(ex.getName())) {
                ex.setCompleted(true);
            }
        }
    }

    public boolean isCompleted(String exercise) {
        for (Exercise ex: this.exercises) {
            if (exercise.equals(ex.getName())) {
                return ex.isCompleted();
            }
        }

        return false;
    }
}
