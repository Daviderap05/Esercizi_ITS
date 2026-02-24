import java.util.ArrayList;
import java.util.Collections;
import java.util.Date;
import java.util.List;

public class Ordine {

    // Contatore statico condiviso: tiene traccia del prossimo ID disponibile
    private static int contatore = 1;

    // ID immutabile: finale, non può essere cambiato dopo l'assegnazione
    private final int numero;

    private final Date data;
    private final Cliente cliente;
    private final ArrayList<Articolo> carrello;

    public Ordine(Cliente cliente) {
        if (cliente == null) {
            throw new IllegalArgumentException("Cliente non valido.");
        }

        this.cliente = cliente;
        this.carrello = new ArrayList<>();
        this.data = new Date();
        this.numero = Ordine.contatore++;
    }

    public int getNumero() {
        return this.numero;
    }

    public Date getData() {
        return new Date(data.getTime());
    }

    public Cliente getCliente() {
        return this.cliente;
    }

    public List<Articolo> getCarrello() {
        return Collections.unmodifiableList(this.carrello);
    }

    public void aggiungiArticolo(Articolo articolo) {
        if (articolo == null) {
            throw new IllegalArgumentException("Articolo nullo.");
        }

        carrello.add(articolo);
    }

    public double totaleOrdine() {
        double totale = 0;
        for (Articolo a : this.carrello) {
            totale += a.getPrezzoVendita();
        }

        return totale * this.cliente.getMoltiplicatoreOrdine();
    }

    public void chiusuraOrdine() {
        double totale = totaleOrdine();
        double conto = this.cliente.getConto();

        if (conto < totale)
            throw new IllegalStateException("Saldo insufficiente.");

        this.cliente.setConto(conto - totale);
    }
    
    public void svuotaCarrello() {
        carrello.clear();
    }
}