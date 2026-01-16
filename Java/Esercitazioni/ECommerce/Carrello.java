package Esercitazioni.ECommerce;

import java.util.ArrayList;

public class Carrello {
    private final ArrayList<Prodotto> carrello;

    public Carrello() {
        this.carrello = new ArrayList<>();
    }

    public void add(Prodotto p) {
        if (p == null) {
            throw new IllegalArgumentException("Prodotto nullo");
        }

        if (carrello.contains(p)) {
            p.setQOrdinata(p.getQOrdinata() + 1);
        } else {
            carrello.add(p);
        }
    }

    public void delete(Prodotto p) {
        if (p == null) {
            throw new IllegalArgumentException("Prodotto nullo");
        }

        if (!carrello.contains(p)) {
            throw new IllegalArgumentException("Il prodotto non è nel carrello");
        }

        if (p.getQOrdinata() > 1) {
            p.setQOrdinata(p.getQOrdinata() - 1);
        } else {
            carrello.remove(p);
        }
    }

    public int totaleProdotti() {
        int tot = 0;
        for (Prodotto p : this.carrello) {
            tot += p.getQOrdinata();
        }
        return tot;
    }

    public double totaleDaPagare() {
        double tot = 0.0;
        for (Prodotto p : this.carrello) {
            tot += p.getPrezzo() * p.getQOrdinata();
        }
        return tot;
    }

    public void stampaCarrello() {
        System.out.println("=== CARRELLO ===");

        if (carrello.isEmpty()) {
            System.out.println("(vuoto)");
            return;
        }

        for (Prodotto p : this.carrello) {
            System.out.println("- " + p.getDesc()
                + " | q=" + p.getQOrdinata()
                + " | prezzo unit=" + String.format("%.2f", p.getPrezzo())
                + " | subtot=" + String.format("%.2f", p.getPrezzo() * p.getQOrdinata()));
        }

        System.out.println("----------------");
        System.out.println("Totale prodotti: " + totaleProdotti());
        System.out.println("Totale da pagare: " + String.format("%.2f", totaleDaPagare()));
    }
}
