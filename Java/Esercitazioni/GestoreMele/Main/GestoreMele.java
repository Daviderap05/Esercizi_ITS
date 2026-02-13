package Esercitazioni.GestoreMele.Main;

import Esercitazioni.GestoreMele.Class.CriterioColore;
import Esercitazioni.GestoreMele.Class.Mela;
import Esercitazioni.GestoreMele.Interface.Criterio;
import java.util.ArrayList;
import java.util.List;

public class GestoreMele {

    public static void main(String[] args) {
        // Creo una lista di mele
        ArrayList<Mela> cassetta = new ArrayList<>();
        cassetta.add(new Mela("rossa", 100));
        cassetta.add(new Mela("verde", 150));
        cassetta.add(new Mela("gialla", 200));
        cassetta.add(new Mela("rossa", 80));
        cassetta.add(new Mela("verde", 900));
        cassetta.add(new Mela("gialla", 100));

        // filtro x colore
        List<Mela> risultato = filtraPerColore(cassetta);
        System.out.println("Solo le mele verdi: ");
        for (Mela mela : risultato) {
            System.out.println(mela);
        }

        System.out.println();

        // filtro x colore (Lambda)
        risultato = filtraMele(cassetta, mela -> mela.getColore().equals("rossa") && mela.getPeso() == 100);
        System.out.println("Solo le mele rosse che pesano 100 (con Lambda): ");
        for (Mela mela : risultato) {
            System.out.println(mela);
        }

        System.out.println();

        // filtro x colore(Criterio)
        System.out.println("Solo le mele verdi (filtrata con Criterio): ");
        risultato = filtraMele(cassetta, new CriterioColore());
        for (Mela mela : risultato) {
            System.out.println(mela);
        }

        System.out.println();

        // filtro x peso
        risultato = filtraPerPeso(cassetta);
        System.out.println("Solo le mele con peso maggiore di 150: ");
        for (Mela mela : risultato) {
            System.out.println(mela);
        }

    }

    public static List<Mela> filtraPerColore(List<Mela> cassetta) {

        ArrayList<Mela> listaFiltrata = new ArrayList<>();

        for (Mela mela : cassetta) {

            if (mela.getColore().equals("verde")) {
                listaFiltrata.add(mela);
            }

        }
        return listaFiltrata;
    }

    public static List<Mela> filtraPerPeso(List<Mela> cassetta) {

        ArrayList<Mela> listaFiltrata = new ArrayList<>();

        for (Mela mela : cassetta) {

            if (mela.getPeso() > 150) {
                listaFiltrata.add(mela);
            }

        }
        return listaFiltrata;
    }

    public static List<Mela> filtraMele(List<Mela> cassetta, Criterio criterio) {

        ArrayList<Mela> filtrata = new ArrayList<>();

        for (Mela mela : cassetta) {

            if (criterio.test(mela) == true)
                filtrata.add(mela);
        }

        return filtrata;
    }

}