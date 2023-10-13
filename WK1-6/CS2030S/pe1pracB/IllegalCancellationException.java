/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * Checked exception for the task.
 */
class IllegalCancellationException extends Exception {
  public IllegalCancellationException(String event) {
    super("Unable to cancel event: " + event);
  }
}