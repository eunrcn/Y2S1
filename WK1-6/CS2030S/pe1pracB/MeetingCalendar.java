/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */

/**
 * Meeting Calendar.
 */
class MeetingCalendar extends Calendar {
  private int start;
  private int end;
  private String person;
  
  public MeetingCalendar(String event, int start, int end, String person) {
    super(event);
    this.start = start;
    this.end = end;
    this.person = person;
  }
  
  @Override
  public boolean needReminder(int hour) {
    return super.needReminder(hour) && hour <= this.start;
  }
  
  @Override
  public int busyPeriod() {
    return this.isNotCancelled() ? this.end - this.start : 0;
  }
  
  @Override
  public String getDetails() {
    return super.getDescription() + " | " + this.start + " - " + this.end + " | Meet with " + this.person;
  }
}