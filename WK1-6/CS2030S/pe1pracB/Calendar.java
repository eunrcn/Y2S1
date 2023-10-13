/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * Abstract Calendar.
 */
abstract class Calendar {
  private String event;
  private boolean isCancelled;
  
  public Calendar(String event) {
    this.event = event;
    this.isCancelled = false;
  }
  
  public void cancel() throws IllegalCancellationException {
    this.isCancelled = true;
  }
  
  public boolean isNotCancelled() {
    return !this.isCancelled;
  }
  
  public boolean needReminder(int hour) {
    return !this.isCancelled;
  }
  
  public String getDescription() {
    return this.toString();
  }
  
  abstract public String getDetails();
  abstract public int busyPeriod();
  
  @Override
  public String toString() {
    return this.event;
  }
}