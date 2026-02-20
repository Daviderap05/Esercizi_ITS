package Esercitazioni.Telefono;

import java.util.ArrayList;

public class RubricaMain {
    public static void main(String[] args) {

        Contatto c1 = new Contatto("Mario", "Rossi", "123456789");
        Contatto c2 = new Contatto("Luigi", "Verdi", "987654321");
        Contatto c3 = new Contatto("Anna", "Bianchi", "555555555");

        ArrayList<Contatto> lista = new ArrayList<>();
        lista.add(c1);
        lista.add(c2);

        Rubrica rubrica = new Rubrica(lista);

        rubrica.addContact(c3);

        System.out.println("Numero contatti: " + rubrica.countContact());
        System.out.println("Posti liberi: " + rubrica.countFreeContact());

        Contatto c = rubrica.showContact(1);
        if (c != null) {
            System.out.println("Contatto in posizione 1: " + c.getNome());
        }

        Contatto ricercaNome = rubrica.findContactByName("Anna");
        if (ricercaNome != null) {
            System.out.println("Trovato per nome: " + ricercaNome.getNome());
        }

        Contatto ricercaNumero = rubrica.findContactByNumber("123456789");
        if (ricercaNumero != null) {
            System.out.println("Trovato per numero: " + ricercaNumero.getNome());
        }
    }
}
