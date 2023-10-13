/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */

/**
 * Caller Call.
 */
class CallerCall extends Call {
  private int phone;
  
  public CallerCall(int length, int phone) {
    super(length);
    this.phone = phone;
  }
  
  @Override
  public String getNumbers() {
    return "" + this.phone;
  }
  
  @Override
  public boolean isMissedCall() {
    return false;
  }
}