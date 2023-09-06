public class Main {
    public static void main(String[] args) {
        Ternary t = new Ternary();
        System.out.println(t.toString());
        System.out.println(t);  // Output: 0
        
        t.incr();
        System.out.println(t);  // Output: 1
        
        t.incr();
        System.out.println(t);  // Output: 2
        
        t.incr();
        System.out.println(t);  // Output: 0
    }
}