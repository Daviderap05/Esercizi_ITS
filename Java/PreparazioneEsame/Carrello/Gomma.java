@SuppressWarnings("OverridableMethodCallInConstructor")

public class Gomma extends Articolo {

    private int dimensione;
    private String forma;

    public Gomma(String marca, String modello, int dimensione, String forma, double costo) {
        super(marca, modello, costo);
        setDimensione(dimensione);
        setForma(forma);
    }

    public Gomma(String marca, String modello, int dimensione, String forma, double costo, double prezzoVendita) {
        super(marca, modello, costo, prezzoVendita);
        setDimensione(dimensione);
        setForma(forma);
    }

    public int getDimensione() {
        return this.dimensione;
    }

    public void setDimensione(int dimensione) {
        if (dimensione <= 0) {
            throw new IllegalArgumentException("Dimensione non valida (deve essere > 0).");
        }
        this.dimensione = dimensione;
    }

    public String getForma() {
        return this.forma;
    }

    public void setForma(String forma) {
        if (forma == null || forma.isBlank()) {
            throw new IllegalArgumentException("Forma non valida (non può essere vuota).");
        }
        this.forma = forma.trim();
    }

    @Override
    public String toString() {
        return "Gomma{" +
                "dimensione=" + this.dimensione +
                ", forma='" + this.forma + '\'' +
                "} " + super.toString();
    }
}