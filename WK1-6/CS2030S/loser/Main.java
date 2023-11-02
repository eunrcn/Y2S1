package loser;

public class Main {
    public static void main(String[] args) {
        A a = A.of(1)
            .flatMap(x -> incrA(x).flatMap(y -> sqrA(y)));

        String result = a.toString();
        System.out.println("Result: " + result);
    }

    public static A incrA(int x) {
        return new A(x + 1, x);
    }

    public static A sqrA(int x) {
        return new A(x * x, x);
    }
}
