class Operand {
    private final Object x;

    public Operand(Object x) {
        this.x = x;
    }
    
    public Object eval() {
        return x;
    }
}