package loser;

@FunctionalInterface
public interface Transformer<U, T> {
  T transform(U u);
}
