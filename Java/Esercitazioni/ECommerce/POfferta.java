package Esercitazioni.ECommerce;

public class POfferta extends Prodotto {

    private int quantitaMin;
    private int sconto; // 0..100

    @SuppressWarnings("OverridableMethodCallInConstructor")
    public POfferta(String desc, double prezzoListino, int quantitaMin, int sconto, int qOrdinata) {
        super(desc, prezzoListino, qOrdinata);
        this.setQuantitaMin(quantitaMin);
        this.setSconto(sconto);
    }

    @SuppressWarnings("OverridableMethodCallInConstructor")
    public POfferta(String desc, double prezzoListino, int quantitaMin, int sconto) {
        super(desc, prezzoListino);
        this.setQuantitaMin(quantitaMin);
        this.setSconto(sconto);
    }

    public int getQuantitaMin() {
        return this.quantitaMin;
    }

    public void setQuantitaMin(int quantitaMin) {
        if (quantitaMin < 1) {
            throw new IllegalArgumentException("Quantità minima deve essere >= 1.");
        }
        this.quantitaMin = quantitaMin;
        ricalcolaPrezzoCorrente();
    }

    public int getSconto() {
        return this.sconto;
    }

    public void setSconto(int sconto) {
        if (sconto < 0 || sconto > 100) {
            throw new IllegalArgumentException("Sconto valido solo tra 0 e 100%.");
        }
        this.sconto = sconto;
        ricalcolaPrezzoCorrente();
    }

    @Override
    protected void ricalcolaPrezzoCorrente() {
        double base = getPrezzoListino();

        if (getQOrdinata() >= this.quantitaMin) {
            setPrezzoCorrente(base * (1.0 - (this.sconto / 100.0)));
        } else {
            setPrezzoCorrente(base);
        }
    }
}