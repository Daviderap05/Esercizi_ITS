package Esercitazioni.Adapter;

public class Main {
    public static void main(String[] args) {
        // Esempio Class Object
        PaymentSystem paymentSystem = new PaymentSystem();
        AdapterObject adapterObject = new AdapterObject(paymentSystem);

        adapterObject.pay(20.50);

        // Esempio Class Adapter
        AdapterClass paymentProcessor = new AdapterClass();
        paymentProcessor.pay(15.75);
    }
}
