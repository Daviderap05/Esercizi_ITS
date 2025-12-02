package lezione2;

import java.util.Random;
import java.util.Scanner;

public class esercizio3 {
    public static void main(String[] args) {
        
        Random rand = new Random();
        Scanner s = new Scanner(System.in);

        int ris_c;
        String ris;

        System.out.println("\n\nMorra Cinese\n");

        do {

            ris_c = rand.nextInt(0, 3);

            System.out.println("0  --> Sasso");
            System.out.println("1  --> Carta");
            System.out.println("2  --> Forbice\n");

            System.out.print("Fai il tuo gioco: ");
            int ris_g = s.nextInt();

            switch (ris_g) {

                case 0 -> {
                    if (ris_c == ris_g) {
                        System.out.println("Pareggio\n");
                    } else if (ris_c == 1) {
                        System.out.println("Sconfitta\n");
                    } else {
                        System.out.println("Vittoria\n");
                    }
                }

                case 1 -> {
                    if (ris_c == ris_g) {
                        System.out.println("Pareggio\n");
                    } else if (ris_c == 0) {
                        System.out.println("Vittoria\n");
                    } else {
                        System.out.println("Sconfitta\n");
                    }
                }

                case 2 -> {
                    if (ris_c == ris_g) {
                        System.out.println("Pareggio\n");
                    } else if (ris_c == 0) {
                        System.out.println("Sconfitta\n");
                    } else {
                        System.out.println("Vittoria\n");
                    }
                }

                default -> System.out.println("Giocata non valida riprova!\n");

            }

            while (true) {
                System.out.print("\nVuoi giocare ancora (s/n): ");
                ris = s.next().toLowerCase();

                if (!ris.equals("n") || !ris.equals("s")) {
                    System.err.println("Errore... scelta non valida Riprova!");
                } else {
                    break;
                }
            }

        } while (!ris.equals("n"));
    }
}
