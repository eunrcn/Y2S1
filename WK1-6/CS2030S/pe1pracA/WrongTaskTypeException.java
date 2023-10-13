/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */
 
/**
 * Checked exception for the task.
 */
class WrongTaskTypeException extends Exception {
  public WrongTaskTypeException(int type) {
    super("Invalid task type in input: " + type);
  }
}