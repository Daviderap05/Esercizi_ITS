package Esercitazioni.ECommerce;

public class Prodotto {
    private static int contatore = 1;

    private final int id;
    private String desc;

    private double prezzoListino;
    private double prezzoCorrente;

    private int qOrdinata;

    @SuppressWarnings("OverridableMethodCallInConstructor")
    public Prodotto(String desc, double prezzoListino, int qOrdinata) {
        this.id = contatore++;
        this.setDesc(desc);
        this.setPrezzoListino(prezzoListino);
        this.setQOrdinata(qOrdinata);
    }

    @SuppressWarnings("OverridableMethodCallInConstructor")
    public Prodotto(String desc, double prezzoListino) {
        this.id = contatore++;
        this.setDesc(desc);
        this.setPrezzoListino(prezzoListino);
        this.setQOrdinata(1);
    }

    public int getId() {
        return this.id;
    }

    public String getDesc() {
        return this.desc;
    }

    public void setDesc(String desc) {
        if (desc == null || desc.isBlank()) {
            throw new IllegalArgumentException("Descrizione non valida.");
        }
        this.desc = desc;
    }

    public double getPrezzo() {
        return this.prezzoCorrente;
    }

    public double getPrezzoListino() {
        return this.prezzoListino;
    }

    public void setPrezzoListino(double prezzoListino) {
        if (prezzoListino < 0) {
            throw new IllegalArgumentException("Prezzo negativo non valido.");
        }
        this.prezzoListino = prezzoListino;
        ricalcolaPrezzoCorrente();
    }

    protected void setPrezzoCorrente(double prezzoCorrente) {
        this.prezzoCorrente = prezzoCorrente;
    }

    public int getQOrdinata() {
        return this.qOrdinata;
    }

    public void setQOrdinata(int qOrdinata) {
        if (qOrdinata < 0) {
            throw new IllegalArgumentException("Quantità ordinata non valida.");
        }

        this.qOrdinata = qOrdinata;
        ricalcolaPrezzoCorrente();
    }

    protected void ricalcolaPrezzoCorrente() {
        this.prezzoCorrente = this.prezzoListino;
    }

    @Override
    public String toString() {
        return "Prodotto{" +
                "id=" + this.id +
                ", desc='" + this.desc + '\'' +
                ", prezzoListino=" + this.prezzoListino +
                ", prezzoCorrente=" + this.prezzoCorrente +
                ", qOrdinata=" + this.qOrdinata +
                '}';
    }
}
