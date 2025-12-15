package lezione7;

import java.util.ArrayList;

public class RubricaMain {
    public static void main(String[] args) {

        // creo alcuni contatti
        Contatto c1 = new Contatto("Mario", "Rossi", "123456789");
        Contatto c2 = new Contatto("Luigi", "Verdi", "987654321");
        Contatto c3 = new Contatto("Anna", "Bianchi", "555555555");

        // creo una lista iniziale
        ArrayList<Contatto> lista = new ArrayList<>();
        lista.add(c1);
        lista.add(c2);

        // creo la rubrica
        Rubrica rubrica = new Rubrica(lista);

        // aggiungo un contatto
        rubrica.addContact(c3);

        // stampo numero contatti
        System.out.println("Numero contatti: " + rubrica.countContact());
        System.out.println("Posti liberi: " + rubrica.countFreeContact());

        // mostro un contatto per posizione
        Contatto c = rubrica.showContact(1);
        if (c != null) {
            System.out.println("Contatto in posizione 1: " + c.getNome());
        }

        // ricerca per nome
        Contatto ricercaNome = rubrica.findContactByName("Anna");
        if (ricercaNome != null) {
            System.out.println("Trovato per nome: " + ricercaNome.getNome());
        }

        // ricerca per numero
        Contatto ricercaNumero = rubrica.findContactByNumber("123456789");
        if (ricercaNumero != null) {
            System.out.println("Trovato per numero: " + ricercaNumero.getNome());
        }
    }
}
