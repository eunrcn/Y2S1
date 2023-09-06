public class Ternary {
    private int value;

    public Ternary() {
        value = 0;
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }

    public void incr() {
        value = (value + 1) % 3;
    }
}


