public class MultiplicationOperation<T extends Number> extends Operation<T> {

    public MultiplicationOperation(Operand<T> expression1, Operand<T> expression2) {
        super(expression1, expression2);
    }

    public T eval() {
        T value1 = expression1.eval();
        T value2 = expression2.eval();
        if (value1 instanceof Integer && value2 instanceof Integer) {
            //multiply
            return (T) Integer.valueOf()
        }
        throw new InvalidOperandException('*');
    }
    
}
