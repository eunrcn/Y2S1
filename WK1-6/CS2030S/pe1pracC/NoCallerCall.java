/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */

/**
 * No Caller Call.
 */
class NoCallerCall extends Call {
  public NoCallerCall(int length) {
    super(length);
  }
  
  @Override
  public String getNumbers() {
    return "No Caller ID";
  }
  
  @Override
  public void callback(int length) throws IllegalCallException {
    throw new IllegalCallException();
  }
  
  @Override
  public boolean isMissedCall() {
    return false;
  }
}