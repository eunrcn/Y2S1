public class InvalidOperandException {
    private char c;

    public InvalidOperandException(char c) {
        this.c = c;
    }
    
    public String getMessage() {
        return "ERROR: Invalid operand for operator " + c;
    }
}
