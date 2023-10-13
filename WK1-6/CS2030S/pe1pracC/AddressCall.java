/**
 * CS2030S AY22/23 Sem 2 PE1
 * @author: STUDENT ID
 * */

/**
 * Address Call.
 */
class AddressCall extends Call {
  private int phone;
  private String name;
  
  public AddressCall(int length, int phone, String name) {
    super(length);
    this.phone = phone;
    this.name = name;
  }
  
  @Override
  public String getNumbers() {
    return "" + this.phone;
  }
  
  @Override
  public boolean isMissedCall() {
    return this.isMissed();
  }
  
  @Override
  public String getCalls() {
    return super.getCalls() + " | " + this.name;
  }
}