package Esercitazioni.PrenotazioneVoli;

public class Assegnatore {
    private int postiDisponibili = 20;

    public synchronized void assegnaPosti(String cliente, int numPosti) throws PostiNonDispException {
        if (numPosti <= this.postiDisponibili) {
            this.postiDisponibili -= numPosti;
            System.out.println("Prenotazione confermata per " + cliente + ": " + numPosti + " posti assegnati.");
            System.out.println("Posti totali rimanenti: " + this.postiDisponibili);
        } else {
            throw new PostiNonDispException("Posti insufficienti per la richiesta di " + cliente);
        }
    }

    public synchronized int getTotalePosti() {
        return this.postiDisponibili;
    }
}
