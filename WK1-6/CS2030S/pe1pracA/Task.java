/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */
 
/**
 * Abstract Task.
 */
abstract class Task {
  private String task;
  private boolean isCompleted;
  
  public Task(String task) {
    this.task = task;
    this.isCompleted = false;
  }
  
  public void complete() {
    this.isCompleted = true;
  }
  
  public boolean needReminder() {
    return !this.isCompleted;
  }
  
  public String getDetails() {
    return "[" + (this.isCompleted ? "X" : " ") + "] " + this.toString();
  }
  
  public int getRewards(int num) {
    // Only Task knows if a task is completed or not.
    // So we propagate the num upwards from the subclasses.
    // Then we decide here if it is 0 or not.
    return this.isCompleted ? num : 0;
  }
  
  public boolean isDueToday() {
    return false;
  }
  
  public String remind() {
    return "\"" + this.task + "\"";
  }
  
  @Override
  public String toString() {
    return this.task;
  }
}