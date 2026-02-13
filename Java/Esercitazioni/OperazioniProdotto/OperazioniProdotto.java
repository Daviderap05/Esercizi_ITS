package Esercitazioni.OperazioniProdotto;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@SuppressWarnings("FieldMayBeFinal")
class Prodotto {
    private int codice;
    private String descrizione;
    private String categoria;
    private int quantita;
    private boolean disponibilita;
    private double prezzo;
    private double sconto;

    public Prodotto(int codice, String descrizione, String categoria, int quantita, boolean disponibilita,
            double prezzo, double sconto) {
        this.codice = codice;
        this.descrizione = descrizione;
        this.categoria = categoria;
        this.quantita = quantita;
        this.disponibilita = disponibilita;
        this.prezzo = prezzo;
        this.sconto = sconto;
    }

    public int getCodice() {
        return this.codice;
    }

    public String getDescrizione() {
        return this.descrizione;
    }

    public String getCategoria() {
        return this.categoria;
    }

    public int getQuantita() {
        return this.quantita;
    }

    public boolean isDisponibilita() {
        return this.disponibilita;
    }

    public double getPrezzo() {
        return this.prezzo;
    }

    public double getSconto() {
        return this.sconto;
    }

    @Override
    public String toString() {
        return this.descrizione + " (" + this.prezzo + "€, Sconto: " + this.sconto + "%)";
    }
}

public class OperazioniProdotto {
    public static void main(String[] args) {

        // Assumiamo di avere la seguente lista di dati nel catalogo
        ArrayList<Prodotto> catalogo = new ArrayList<>();
        catalogo.add(new Prodotto(133, "latte", "alimentare", 100, true, 2.5, 0));
        catalogo.add(new Prodotto(134, "latte UHT", "alimentare", 0, false, 2.5, 0));
        catalogo.add(new Prodotto(113, "pomodori", "alimentare", 50, true, 1.5, 5));
        catalogo.add(new Prodotto(123, "libro", "media", 10, true, 10, 5));
        catalogo.add(new Prodotto(155, "maglietta", "abbigliamento", 20, true, 25, 10));
        catalogo.add(new Prodotto(184, "cd musicale", "media", 0, false, 12.5, 0));
        catalogo.add(new Prodotto(143, "smartphone", "elettronica", 80, true, 250, 10));
        catalogo.add(new Prodotto(144, "cuffie", "elettronica", 0, false, 250, 10));

        System.out.println("--- RISULTATI OPERAZIONI ---");

        // 1. Il numero di categorie
        long numeroCategorie = catalogo.stream()
                .map(Prodotto::getCategoria)
                .distinct()
                .count();
        System.out.println("1. Numero di categorie univoche: " + numeroCategorie);

        // 2. Le categorie ordinate in ordine alfabetico, senza elementi doppi
        List<String> categorieOrdinate = catalogo.stream()
                .map(Prodotto::getCategoria)
                .distinct()
                .sorted()
                .collect(Collectors.toList());
        System.out.println("2. Categorie ordinate alfabeticamente: " + categorieOrdinate);

        // 3. I nomi dei prodotti ordinati per prezzo crescente
        List<String> nomiPrezzoCrescente = catalogo.stream()
                .sorted(Comparator.comparingDouble(Prodotto::getPrezzo))
                .map(Prodotto::getDescrizione)
                .collect(Collectors.toList());
        System.out.println("3. Nomi prodotti per prezzo crescente: " + nomiPrezzoCrescente);

        // 4. I prodotti ordinati in base allo sconto
        List<Prodotto> ordinatiPerSconto = catalogo.stream()
                .sorted(Comparator.comparingDouble(Prodotto::getSconto))
                .collect(Collectors.toList());
        System.out.println("4. Prodotti ordinati per sconto crescente: " + ordinatiPerSconto);

        // 5. Il prodotto con lo sconto maggiore
        Optional<Prodotto> scontoMaggiore = catalogo.stream()
                .max(Comparator.comparingDouble(Prodotto::getSconto));
        System.out.println(
                "5. Prodotto con sconto maggiore: " + scontoMaggiore.map(Prodotto::getDescrizione).orElse("Nessuno"));

        // 6. La somma dei prezzi dei prodotti alimentari
        double sommaAlimentari = catalogo.stream()
                .filter(p -> p.getCategoria().equalsIgnoreCase("alimentare"))
                .mapToDouble(Prodotto::getPrezzo)
                .sum();
        System.out.println("6. Somma prezzi alimentari: " + sommaAlimentari + "€");

        // 7. Un Optional vuoto a seguito di una ricerca di prodotto per una categoria
        // inesistente (es. giocattoli)
        Optional<Prodotto> categoriaInesistente = catalogo.stream()
                .filter(p -> p.getCategoria().equalsIgnoreCase("giocattoli"))
                .findAny();
        System.out.println("7. Optional da categoria 'giocattoli' è vuoto? " + !categoriaInesistente.isPresent());

        // 8. Il prodotto con prezzo più alto nella categoria media
        Optional<Prodotto> caroMedia = catalogo.stream()
                .filter(p -> p.getCategoria().equalsIgnoreCase("media"))
                .max(Comparator.comparingDouble(Prodotto::getPrezzo));
        System.out.println(
                "8. Prodotto più costoso in 'media': " + caroMedia.map(Prodotto::getDescrizione).orElse("Nessuno"));

        // 9. I nomi dei prodotti non disponibili
        List<String> nonDisponibili = catalogo.stream()
                .filter(p -> !p.isDisponibilita())
                .map(Prodotto::getDescrizione)
                .collect(Collectors.toList());
        System.out.println("9. Nomi prodotti non disponibili: " + nonDisponibili);
    }
}