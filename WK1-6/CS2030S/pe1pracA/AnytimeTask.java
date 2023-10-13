/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */
 
/**
 * Any time Task.
 */
class AnytimeTask extends Task {
  public AnytimeTask(String task) {
    super(task);
  }
  
  @Override
  public String getDetails() {
    return super.getDetails();
  }
  
  @Override
  public boolean needReminder() {
    return false;
  }
}