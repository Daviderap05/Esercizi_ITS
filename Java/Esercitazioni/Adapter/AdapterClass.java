package Esercitazioni.Adapter;

// Soluzione Class
public class AdapterClass extends PaymentSystem implements PaymentProcessor {
    @Override
    public void pay(double amount) {
        amount *= 100;
        makePayment((int) amount);
    }
}
