class Test6 {
  public static void main(String[] args) {
    CallHistory hist = new CallHistory();
    hist.callback(5, 3);
    hist.printMissedCalls();
  }
}
