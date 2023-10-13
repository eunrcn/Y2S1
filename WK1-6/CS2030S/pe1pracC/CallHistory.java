/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * Encapsulate a list of phone call history.
 */
class CallHistory {
  private Array<Call> allCalls;

  // The types of calls
  private static final int NO_CALLER_ID = 0;
  private static final int UNKNOWN_CALLER = 1;
  private static final int CONTACT = 2;

  /**
   * A constructor that reads in the list from the standard input.
   **/
  public CallHistory() {
    this(new Scanner(System.in));
  }

  /**
   * A constructor that reads in the list from the standard input.
   * @throws FileNotFoundException
   **/
  public CallHistory(String filename) throws FileNotFoundException {
    this(new Scanner(new File(filename)));
  }

  /**
   * A constructor that reads in the list using the given scanner.
   * @param sc The Scanner to read from.
   **/
  private CallHistory(Scanner sc) {
    this.loadCalls(sc);
  }

  /**
   * Load the calls from the given scanner.
   * @param sc The scanner to load from.
   **/
  private void loadCalls(Scanner sc) {
    int numOfCalls = Integer.parseInt(sc.nextLine().trim());
    this.allCalls = new Array<Call>(numOfCalls);

    int i = 0;
    while (sc.hasNext()) {
      String text = sc.nextLine().trim();
      String[] arguments = text.split(",");
      this.createCall(i, arguments);
      i = i + 1;
    }
  }

  /**
   * Create Call i with the given arguments.
   * @param i The index of the task.
   * @param args The arguments read from the input.
   * @return false if the input contains a wrong type; true otherwise.
   **/
  private void createCall(int i, String[] args) { 
    int type = Integer.parseInt(args[0]);
    int length = Integer.parseInt(args[1]);

    if (type == CallHistory.NO_CALLER_ID) {
      this.allCalls.set(i, new NoCallerCall(length));
    } else if (type == CallHistory.UNKNOWN_CALLER) {
      int number = Integer.parseInt(args[2]);
      this.allCalls.set(i, new CallerCall(length, number));
    } else if (type == CallHistory.CONTACT) {
      int number = Integer.parseInt(args[2]);
      String name = args[3];
      this.allCalls.set(i, new AddressCall(length, number, name));
    }
  }

  /**
   * Print the phone number of all calls.
   **/
  public void printNumbers() {
    for (int i = 0; i < this.allCalls.length(); i++) {
      System.out.println(i + " " + this.allCalls.get(i).getNumbers());
    }
  }

  /**
   * Print the details of all calls.
   **/
  public void printAllCalls() {
    for (int i = 0; i < this.allCalls.length(); i++) {
      System.out.println(i + " " + this.allCalls.get(i).getCalls());
    }
  }

  /**
   * Calculate the total time on call.
   * @return The total time on call in minutes.
   **/
  public int getMinutesOnCall() {
    int sum = 0;
    for (int i = 0; i < this.allCalls.length(); i++) {
      sum += this.allCalls.get(i).getMinutes();
    }
    return sum;
  }

  /**
   * Print all missed calls from known contacts.
   **/
  public void printMissedCalls() {
    for (int i = 0; i < this.allCalls.length(); i++) {
      if (this.allCalls.get(i).isMissedCall()) {
        System.out.println(i + " " + this.allCalls.get(i).getCalls());
      }
    }
  }

  /**
   * Make a returned call to Call i that lasts a given time.
   * @param i The index of the Call to return.
   * @param length The length of the call in minutes.
   **/
  public void callback(int i, int length) {
    try {
      this.allCalls.get(i).callback(length);
    } catch (IllegalCallException e) {
      System.out.println(e.getMessage());
    }
  }
}
