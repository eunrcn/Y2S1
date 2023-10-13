/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */

/**
 * Abstract Call.
 */
abstract class Call {
  private int length;
  
  public Call(int length) {
    this.length = length;
  }
  
  abstract public String getNumbers();
  
  public String getCalls() {
    return this.getNumbers() + " | " + (this.isMissed() ? "[MISSED]" : this.length + " minutes");
  }
  
  public void callback(int length) throws IllegalCallException {
    this.length = (this.isMissed() ? length : this.length + length);
  }
  
  public boolean isMissed() {
    return this.length == -1;
  }
  
  abstract public boolean isMissedCall();
  
  public int getMinutes() {
    return this.isMissed() ? 0 : this.length;
  }
}