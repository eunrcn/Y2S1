class Test3 {
  public static void main(String[] args) {
    CallHistory cal = new CallHistory();
    cal.callback(1, 24);
    cal.callback(3, 7);
    cal.printAllCalls();
  }
}
