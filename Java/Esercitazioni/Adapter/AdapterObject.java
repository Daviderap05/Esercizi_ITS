package Esercitazioni.Adapter;

//Soluzione Object
public class AdapterObject implements PaymentProcessor {

    public PaymentSystem paymentSystem;

    public AdapterObject(PaymentSystem paymentSystem) {
        this.paymentSystem = paymentSystem;
    }

    @Override
    public void pay(double amount) {
        amount *= 100;
        paymentSystem.makePayment((int) amount);
    }
}