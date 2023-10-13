class Test7 {
  public static void main(String[] args) {
    CallHistory cal = new CallHistory();
    cal.callback(1, 24);
    cal.callback(3, 7);
    System.out.println(cal.getMinutesOnCall());
  }
}
