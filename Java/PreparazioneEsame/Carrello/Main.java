public class Main {

    public static void main(String[] args) {

        // =========================
        // CLIENTI
        // =========================

        Cliente privato = new Privato("Mario Rossi", 500);
        Cliente azienda = new Azienda("Tech SRL", 1000);

        // =========================
        // MAGAZZINO
        // =========================

        Magazzino magazzino = new Magazzino();

        Articolo penna1 = new Penna("Bic", "Cristal", "Blu", 0.5);
        Articolo penna2 = new Penna("Bic", "Gel", "Nera", 1.0);
        Articolo gomma1 = new Gomma("Staedtler", "Soft", 5, "Rettangolare", 0.8);
        Articolo gomma2 = new Gomma("Faber", "Pro", 6, "Quadrata", 1.2);

        magazzino.addArticolo(penna1);
        magazzino.addArticolo(penna2);
        magazzino.addArticolo(gomma1);
        magazzino.addArticolo(gomma2);

        magazzino.stampaArticoli();

        // =========================
        // RICERCHE
        // =========================

        System.out.println("Ricerca per marca Bic:");
        magazzino.cercaPerMarca("Bic").forEach(System.out::println);

        System.out.println("\nRicerca modello contiene 'Pro':");
        magazzino.cercaPerModello("Pro").forEach(System.out::println);

        // =========================
        // ORDINAMENTI
        // =========================

        System.out.println("\nOrdinati per prezzo crescente:");
        magazzino.ordinatiPerPrezzoCrescente().forEach(System.out::println);

        // =========================
        // ORDINE PRIVATO (con moltiplicatore)
        // =========================

        Ordine ordinePrivato = new Ordine(privato);
        ordinePrivato.aggiungiArticolo(penna1);
        ordinePrivato.aggiungiArticolo(gomma1);

        System.out.println("\nTotale ordine privato: " + ordinePrivato.totaleOrdine());

        ordinePrivato.chiusuraOrdine();

        System.out.println("Saldo cliente privato dopo acquisto: " + privato.getConto());

        // Scarico articoli dal magazzino
        magazzino.scaricaPerId(penna1.getId());
        magazzino.scaricaPerId(gomma1.getId());

        // =========================
        // ORDINE AZIENDA (senza moltiplicatore)
        // =========================

        Ordine ordineAzienda = new Ordine(azienda);
        ordineAzienda.aggiungiArticolo(penna2);
        ordineAzienda.aggiungiArticolo(gomma2);

        System.out.println("\nTotale ordine azienda: " + ordineAzienda.totaleOrdine());

        ordineAzienda.chiusuraOrdine();

        System.out.println("Saldo azienda dopo acquisto: " + azienda.getConto());

        magazzino.scaricaPerId(penna2.getId());
        magazzino.scaricaPerId(gomma2.getId());

        // =========================
        // MAGAZZINO FINALE
        // =========================

        System.out.println("\nMagazzino finale:");
        magazzino.stampaArticoli();
    }
}