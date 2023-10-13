class Test5 {
  public static void main(String[] args) {
    CallHistory hist = new CallHistory();
    hist.callback(1, 24);
    hist.printMissedCalls();
  }
}
