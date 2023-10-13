/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * Encapsulate a list of TODO tasks.
 */
class TaskList {
  private Array<Task> allTasks; // Store the task.

  // The types of tasks
  private static final int ANYTIME = 0;
  private static final int DEADLINE = 1;
  private static final int ASSIGNABLE = 2;

  /**
   * A constructor that reads in the list from the standard input.
   **/
  public TaskList() {
    this(new Scanner(System.in));
  }

  /**
   * A constructor that reads in the list from the standard input.
   * @throws FileNotFoundException
   **/
  public TaskList(String filename) throws FileNotFoundException {
    this(new Scanner(new File(filename)));
  }

  /**
   * A constructor that reads in the list using the given scanner.
   * If the input contains an invalid type, print an error message.
   * @param sc The Scanner to read from.
   **/
  private TaskList(Scanner sc) {
    this.loadTasks(sc);
  }

  /**
   * Load the tasks from the given scanner.
   * @param sc The scanner to load from.
   * @return false if the input contains a wrong type; true otherwise.
   **/
  private void loadTasks(Scanner sc) {
    int numOfTasks = Integer.parseInt(sc.nextLine().trim());
    this.allTasks = new Array<Task>(numOfTasks);

    int i = 0;
    try {
      while (sc.hasNext()) {
        String text = sc.nextLine().trim();
        String[] arguments = text.split(",");
        this.createTask(i, arguments);
        i = i + 1;
      }
    } catch(WrongTaskTypeException e) {
      System.out.println(e.getMessage());
    } finally {
      sc.close();
    }
  }

  /**
   * Create Task i with the given arguments.
   * @param i The index of the task.
   * @param args The arguments read from the input.
   * @return false if the input contains a wrong type; true otherwise.
   **/
  private void createTask(int i, String[] args) throws WrongTaskTypeException {
    int type = Integer.parseInt(args[0]);
    String description = args[1];

    if (type == TaskList.ANYTIME) {
      this.allTasks.set(i, new AnytimeTask(description));
    } else if (type == TaskList.DEADLINE) {
      int dueInDays = Integer.parseInt(args[2]);
      this.allTasks.set(i, new DeadlineTask(description, dueInDays));
    } else if (type == TaskList.ASSIGNABLE) {
      int dueInDays = Integer.parseInt(args[2]);
      String assignees = args[3];
      this.allTasks.set(i, new DelegatedTask(description, dueInDays, assignees));
    } else {
      throw new WrongTaskTypeException(type);
    }
  }

  /**
   * Print the description of all tasks.
   **/
  public void printTaskDescriptions() {
    for (int i = 0; i < this.allTasks.length(); i++) {
      String description = this.allTasks.get(i).toString();
      System.out.println(i + " " + description);
    }
  }

  /**
   * Print the details of all tasks.
   **/
  public void printTaskDetails() {
    for (int i = 0; i < this.allTasks.length(); i++) {
      System.out.println(i + " " + this.allTasks.get(i).getDetails());
    }
  }

  /**
   * Calculate the total reward points earned.
   * @return The reward points.
   **/
  public int getRewardPoints() {
    int sum = 0;
    for (int i = 0; i < this.allTasks.length(); i++) {
      sum += this.allTasks.get(i).getRewards(0);
    }
    return sum;
  }

  /**
   * Print all the tasks that are due today.
   **/
  public void printDueToday() {
    for (int i = 0; i < this.allTasks.length(); i++) {
      if (this.allTasks.get(i).isDueToday()) {
        System.out.println(i + " " + this.allTasks.get(i).getDetails());
      }
    }
  }

  /**
   * Remind users about all incomplete tasks with deadline.
   */
  public void remindAll() {
    for (int i = 0; i < this.allTasks.length(); i++) {
      if (this.allTasks.get(i).needReminder()) {
        System.out.println(this.allTasks.get(i).remind());
      }
    }
  }

  /**
   * Mark a task as complete.
   * @param i The index of the task to complete.
   */
  public void completeTask(int i) {
    this.allTasks.get(i).complete();
  }
}
