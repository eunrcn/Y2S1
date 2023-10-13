/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */

/**
 * Birthday Calendar.
 */
class BirthdayCalendar extends Calendar {
  public BirthdayCalendar(String event) {
    super(event);
  }
  
  @Override
  public void cancel() throws IllegalCancellationException {
    throw new IllegalCancellationException(this.getDescription());
  }
  
  @Override
  public String getDescription() {
    return "Birthday (" + super.getDescription() + ")";
  }
  
  @Override
  public boolean needReminder(int hour) {
    return false;
  }
  
  @Override
  public int busyPeriod() {
    return 0;
  }
  
  @Override
  public String getDetails() {
    return this.getDescription();
  }
}