package loser;

class A {
  private final int value;
  private final int cumulative;

  public A(int value, int cumulative) {
    this.value = value;
    this.cumulative = cumulative;
  }

  public static A of(int value) {
    return new A(value, 0);
  }

  public A flatMap(Transformer<? super Integer, ? extends A> transformer) {
    A updated = transformer.transform(this.value);
    return new A(updated.value, updated.cumulative + this.cumulative);
  }

  public String toString() {
    return this.value + " " + this.cumulative;
  }

  A incrA(int x) {
    return new A(x + 1, x);
  }

  A sqrA(int x) {
    return new A(x * x, x);
  }
}
