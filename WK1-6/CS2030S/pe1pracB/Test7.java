class Test7 {
  public static void main(String[] args) {
    DayCalendar cal = new DayCalendar();
    cal.cancelEvent(2);
    System.out.println(cal.getBusyPeriod());
  }
}
