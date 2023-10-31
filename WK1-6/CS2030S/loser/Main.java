package loser;

public class Main {
    public static void main(String[] args) {
        // Code snippet 0
        A a = A.of(1); // Create an instance of A with value 1
        String result = a.toString(); // Call the toString method on the instance
        System.out.println("Code snippet 0: " + result);

        // Code snippet 1
        String result1 = A.of(1).flatMap(x -> A.of(x)).toString();
        System.out.println("Code snippet 1: " + result1);

        // Code snippet 2
        String result2 = A.of(10).incrA(10).toString();
        System.out.println("Code snippet 2: " + result2);

        // Code snippet 3
        String result3 = A.of(10).incrA(10).flatMap(x -> A.of(x)).toString();
        System.out.println("Code snippet 3: " + result3);

        // Code snippet 4
        String result4 = A.of(1).flatMap(x -> A.of(x).flatMap(y -> A.of(y).sqrA(y))).toString();
        System.out.println("Code snippet 4: " + result4);

        // Code snippet 5
        String result5 = A.of(1)
            .flatMap(x -> A.of(x).flatMap(y -> A.of(y).sqrA(y)))
            .toString();
        System.out.println("Code snippet 5: " + result5);
    }
}
