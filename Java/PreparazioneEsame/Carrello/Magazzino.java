import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Magazzino {

    private final TreeSet<Articolo> magazzino;

    public Magazzino() {
        this.magazzino = new TreeSet<>((a, b) -> Integer.compare(a.getId(), b.getId()));
    }

    public Set<Articolo> getMagazzino() {
        return Collections.unmodifiableSet(this.magazzino);
    }

    public void stampaArticoli() {
        System.out.println("\n--- MAGAZZINO ---");

        for (Articolo a : this.magazzino) {
            System.out.println(a);
        }

        System.out.println("-----------------\n");
    }

    public boolean addArticolo(Articolo a) {
        if (a == null)
            throw new IllegalArgumentException("Articolo nullo.");

        boolean ok = magazzino.add(a);
        System.out.println(ok ? "Articolo aggiunto correttamente" : "Articolo già presente (stesso id).");

        return ok;
    }

    public double sommaCosti() {
        double somma = 0;
        for (Articolo a : this.magazzino) {
            somma += a.getCosto();
        }

        return somma;
    }

    public double sommaPrezzi() {
        double somma = 0;
        for (Articolo a : this.magazzino) {
            somma += a.getPrezzoVendita();
        }

        return somma;
    }

    public List<Articolo> cercaPerMarca(String marca) {
        if (marca == null)
            throw new IllegalArgumentException("Marca nulla.");

        return magazzino.stream()
                .filter(a -> a.getMarca() != null &&
                        a.getMarca().equalsIgnoreCase(marca))
                .toList();
    }

    public List<Articolo> cercaPerModello(String testo) {
        if (testo == null)
            throw new IllegalArgumentException("Testo nullo.");

        String key = testo.toLowerCase();

        return magazzino.stream()
                .filter(a -> a.getModello() != null &&
                        a.getModello().toLowerCase().contains(key))
                .toList();
    }

    public boolean scaricaPerId(int id) {
        return magazzino.removeIf(a -> a.getId() == id);
    }

    public List<Articolo> ordinatiPerPrezzoCrescente() {
        return magazzino.stream()
                .sorted(Comparator.comparingDouble(Articolo::getPrezzoVendita))
                .toList();
    }

    public List<Articolo> ordinatiPerMarca() {
        return magazzino.stream()
                .sorted(Comparator.comparing(Articolo::getMarca,
                        String.CASE_INSENSITIVE_ORDER))
                .toList();
    }

    public List<Articolo> ordinatiPerCosto() {
        return magazzino.stream()
                .sorted(Comparator.comparing(Articolo::getCosto))
                .toList();
    }
}