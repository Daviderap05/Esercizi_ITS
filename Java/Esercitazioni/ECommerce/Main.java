package Esercitazioni.ECommerce;

public class Main {
    public static void main(String[] args) {
        Carrello carrello = new Carrello();

        // Prodotto normale
        Prodotto pane = new Prodotto("Pane", 1.20);

        // Prodotto in offerta: sconto 20% se quantità >= 3
        Prodotto pasta = new POfferta("Pasta", 2.00, 3, 20);

        // --- AGGIUNTE ---
        carrello.add(pane);
        carrello.add(pane); // quantità pane = 2

        carrello.add(pasta); // q = 1
        carrello.add(pasta); // q = 2
        carrello.add(pasta); // q = 3 → scatta lo sconto

        System.out.println("\nDopo aggiunte:");
        carrello.stampaCarrello();

        // --- RIMOZIONE ---
        carrello.delete(pasta); // q = 2 → sconto tolto automaticamente

        System.out.println("\nDopo rimozione di una pasta:");
        carrello.stampaCarrello();

        // --- ALTRA RIMOZIONE ---
        carrello.delete(pane); // pane da 2 → 1

        System.out.println("\nDopo rimozione di un pane:");
        carrello.stampaCarrello();
    }
}