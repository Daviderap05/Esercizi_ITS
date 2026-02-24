@SuppressWarnings("OverridableMethodCallInConstructor")
public abstract class Articolo {

    // Contatore statico condiviso: tiene traccia del prossimo ID disponibile
    private static int contatore = 1;

    // ID immutabile: finale, non può essere cambiato dopo l'assegnazione
    private final int id;

    private String marca;
    private String modello;
    private double costo;
    private double prezzoVendita;

    public Articolo(String marca, String modello, double costo) {
        this.marca = marca;
        this.modello = modello;
        setCosto(costo);
        setPrezzoVendita(this.costo * 2);
        this.id = Articolo.contatore++;
    }

    public Articolo(String marca, String modello, double costo, double prezzoVendita) {
        this(marca, modello, costo);
        setPrezzoVendita(prezzoVendita);
    }

    public int getId() {
        return this.id;
    }

    public String getMarca() {
        return this.marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModello() {
        return this.modello;
    }

    public void setModello(String modello) {
        this.modello = modello;
    }

    public double getCosto() {
        return this.costo;
    }

    public void setCosto(double costo) {
        if (costo < 0) {
            throw new IllegalArgumentException("Errore costo negativo non inseribile.");
        }

        this.costo = costo;

        if (this.prezzoVendita < this.costo) {
            this.prezzoVendita = this.costo * 2;
        }
    }

    public double getPrezzoVendita() {
        return this.prezzoVendita;
    }

    public void setPrezzoVendita(double prezzoVendita) {
        if (prezzoVendita < this.costo) {
            throw new IllegalArgumentException("Prezzo di vendita troppo basso rispetto il costo del prodotto.");
        }

        this.prezzoVendita = prezzoVendita;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        sb.append("Articolo{");
        sb.append("id=").append(this.id);
        sb.append(", marca=").append(this.marca);
        sb.append(", modello=").append(this.modello);
        sb.append(", costo=").append(this.costo);
        sb.append(", prezzoVendita=").append(this.prezzoVendita);
        sb.append('}');

        return sb.toString();
    }
}