/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * Encapsulate a list of event for today.
 */
class DayCalendar {
  private Array<Calendar> allCalendars; // Store all calendar.

  // The types of event.
  private static final int BIRTHDAY = 0;
  private static final int LESSON = 1;
  private static final int MEETING = 2;

  /**
   * A constructor that reads in the list from the standard input.
   **/
  public DayCalendar() {
    this(new Scanner(System.in));
  }

  /**
   * A constructor that reads in the list from the standard input.
   * @throws FileNotFoundException
   **/
  public DayCalendar(String filename) throws FileNotFoundException {
    this(new Scanner(new File(filename)));
  }

  /**
   * A constructor that reads in the list using the given scanner.
   * @param sc The Scanner to read from.
   **/
  private DayCalendar(Scanner sc) {
    loadEvents(sc);
  }

  /**
   * Load the events from the given scanner.
   * @param sc The scanner to load from.
   **/
  private void loadEvents(Scanner sc) {
    int numOfEvents = Integer.parseInt(sc.nextLine().trim());
    this.allCalendars = new Array<Calendar>(numOfEvents);

    int i = 0;
    while (sc.hasNext()) {
      String text = sc.nextLine().trim();
      String[] arguments = text.split(",");
      createEvent(i, arguments);
      i = i + 1;
    }
  }

  /**
   * Create Event i with the given arguments.
   * @param i The index of the task.
   * @param args The arguments read from the input.
   * @return false if the input contains a wrong type; true otherwise.
   **/
  private void createEvent(int i, String[] args) {
    int type = Integer.parseInt(args[0]);
    String description = args[1];

    if (type == DayCalendar.LESSON) {
      int startTime = Integer.parseInt(args[2]);
      int endTime = Integer.parseInt(args[3]);
      this.allCalendars.set(i, new LessonCalendar(description, startTime, endTime));
    } else if (type == DayCalendar.BIRTHDAY) {
      this.allCalendars.set(i, new BirthdayCalendar(description));
    } else if (type == DayCalendar.MEETING) {
      int startTime = Integer.parseInt(args[2]);
      int endTime = Integer.parseInt(args[3]);
      String meetWith = args[4];
      this.allCalendars.set(i, new MeetingCalendar(description, startTime, endTime, meetWith));
    }
  }

  /**
   * Print the description of all non-cancelled events.
   **/
  public void printEventDescriptions() {
    for (int i = 0; i < this.allCalendars.length(); i++) {
      if (this.allCalendars.get(i).isNotCancelled()) {
        System.out.println(i + " " + this.allCalendars.get(i).getDescription());
      }
    }
  }

  /**
   * Print the details of all non-cancelled events.
   **/
  public void printEventDetails() {
    for (int i = 0; i < this.allCalendars.length(); i++) {
      if (this.allCalendars.get(i).isNotCancelled()) {
        System.out.println(i + " " + this.allCalendars.get(i).getDetails());
      }
    }
  }

  /**
   * Calculate the total busy period (excluding cancelled events).
   * @return The busy period in hours.
   **/
  public int getBusyPeriod() {
    int sum = 0;
    for (int i = 0; i < this.allCalendars.length(); i++) {
      sum += this.allCalendars.get(i).busyPeriod();
    }
    return sum;
  }


  /**
   * Print all non-cancelled events that start on or after a given time.
   * @param time The time used to select the events to remind users about.
   **/
  public void remind(int time) {
    for (int i = 0; i < this.allCalendars.length(); i++) {
      if (this.allCalendars.get(i).needReminder(time)) {
        System.out.println(i + " " + this.allCalendars.get(i).getDetails());
      }
    }
  }

  /**
   * Cancel an event .
   * @param i The index of the event to cancel
   */
  public void cancelEvent(int i) {
    try {
      this.allCalendars.get(i).cancel();
    } catch (IllegalCancellationException e) {
      System.out.println(e.getMessage());
    }
  }
}
