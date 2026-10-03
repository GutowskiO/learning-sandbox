
public class YourFirstAccount {

    public static void main(String[] args) {
        Account Account = new Account("Somebody's account", 100);
        Account.deposit(20);
        System.out.println(Account.saldo());
    }
}
