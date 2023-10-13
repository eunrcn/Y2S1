/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */

/**
 * Lesson Calendar.
 */
class LessonCalendar extends Calendar {
  private int start;
  private int end;
  
  public LessonCalendar(String event, int start, int end) {
    super(event);
    this.start = start;
    this.end = end;
  }
  
  @Override
  public void cancel() throws IllegalCancellationException {
    throw new IllegalCancellationException(this.getDescription());
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
    return super.getDescription() + " | " + this.start + " - " + this.end;
  }
}