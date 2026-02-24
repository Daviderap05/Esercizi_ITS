@SuppressWarnings("OverridableMethodCallInConstructor")
public class Penna extends Articolo {

    private String colore;

    public Penna(String marca, String modello, String colore, double costo) {
        super(marca, modello, costo);
        setColore(colore);
    }

    public Penna(String marca, String modello, String colore, double costo, double prezzoVendita) {
        super(marca, modello, costo, prezzoVendita);
        setColore(colore);
    }

    public String getColore() {
        return this.colore;
    }

    public void setColore(String colore) {
        if (colore == null || colore.isBlank()) {
            throw new IllegalArgumentException("Colore non valido (non può essere vuoto).");
        }
        this.colore = colore.trim();
    }

    @Override
    public String toString() {
        return "Penna{" +
                "colore='" + this.colore + '\'' +
                "} " + super.toString();
    }
}