public class Customer {
    private BankAccount account;

    Customer() {
        this.account = new BankAccount(0);
    }

    public void deposit(double amount) {
        this.account.deposit(amount);
    }

    public boolean withdraw(double amount) {
        return this.account.withdraw(amount);
    }

    public static void main(String[] args) {
        // Create a Customer
        Customer customer = new Customer();

        // Deposit and withdraw operations
        customer.deposit(100);
        System.out.println("Balance after deposit: " + customer.account.getBalance());

        if (customer.withdraw(50)) {
            System.out.println("Withdrawal successful. Balance: " + customer.account.getBalance());
        } else {
            System.out.println("Withdrawal failed. Insufficient balance.");
        }
    }
}