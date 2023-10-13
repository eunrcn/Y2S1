/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */

/**
 * Checked exception for the task.
 */
class IllegalCallException extends Exception {
  public IllegalCallException() {
    super("Unable to call back: No Caller ID");
  }
}