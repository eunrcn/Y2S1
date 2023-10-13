/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */
 
/**
 * Deadline Task.
 */
class DeadlineTask extends Task {
  private int deadline;
  
  public DeadlineTask(String task, int deadline) {
    super(task);
    this.deadline = deadline;
  }
  
  @Override
  public String getDetails() {
    return super.getDetails() + " | Due in " + this.deadline + " days";
  }
  
  @Override
  public int getRewards(int num) {
    return super.getRewards(this.deadline);
  }
  
  @Override
  public boolean isDueToday() {
    return deadline == 0;
  }
  
  @Override
  public String remind() {
    return "The task " + super.remind() + " is due in " + this.deadline + " days";
  }
}