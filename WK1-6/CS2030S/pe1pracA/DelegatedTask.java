/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */
 
/**
 * Delegated Task.
 */
class DelegatedTask extends Task {
  private int deadline;
  private String assignee;
  
  public DelegatedTask(String task, int deadline, String assignee) {
    super(task);
    this.deadline = deadline;
    this.assignee = assignee;
  }
  
  @Override
  public String getDetails() {
    return super.getDetails() + " | Due in " + this.deadline + " days | Assigned to " + this.assignee;
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
    return "Sending a reminder to complete " + super.remind() + " to " + this.assignee;
  }
}