package Esercitazioni.Tamagotchi;

public class Tamagotchi_test {

    // metodo di supporto per stampare lo stato
    private static void stampa(Tamagotchi t) {
        System.out.println(
                "Nome: " + t.getNome() +
                        ", Specie: " + t.getSpecie() +
                        ", Peso: " + t.getPeso() +
                        ", Altezza: " + t.getAltezza() +
                        ", Energia: " + t.getEnergia());
    }

    public static void main(String[] args) {

        Tamagotchi t1 = new Tamagotchi("Fido", "Gatto");
        Tamagotchi t2 = new Tamagotchi("Bob", "Pappagallo"); // specie non valida
        Tamagotchi t3 = new Tamagotchi("Alice"); // default cane

        // STATO INIZIALE
        System.out.println("=== STATO INIZIALE ===");
        stampa(t1);
        stampa(t2);
        stampa(t3);

        // TEST mangia
        System.out.println("\n=== FIDO MANGIA ===");
        System.out.println("mangia(): " + t1.mangia());
        stampa(t1);

        // TEST dorme
        System.out.println("\n=== FIDO DORME ===");
        System.out.println("dorme(): " + t1.dorme());
        stampa(t1);

        // TEST gioca
        System.out.println("\n=== FIDO GIOCA ===");
        System.out.println("gioca(): " + t1.gioca());
        stampa(t1);

        // TEST limite energia
        System.out.println("\n=== TEST LIMITE ENERGIA ===");
        for (int i = 0; i < 10; i++) {
            t1.mangia();
        }
        stampa(t1);
        System.out.println("Prova a mangiare ancora: " + t1.mangia());
    }
}
