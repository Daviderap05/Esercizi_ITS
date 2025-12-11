package lezione6;

import java.util.Scanner;

public class esercizio4 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Inserisci una frase: ");
        String frase = s.nextLine();

        System.out.print("Inserisci un carattere (verrà preso il primo carattere): ");
        String inpuString = s.nextLine();
        char cht = inpuString.toLowerCase().charAt(0);

        int somma = 0;
        for (int i = 0; i < frase.length(); i++) {
            if (frase.toLowerCase().charAt(i) == cht) {
                somma++;
            }
        }

        int somma2 = 0;
        for (int i = 0; i < frase.length(); i++) {
            int pos = frase.toLowerCase().indexOf(cht, i);
            if (pos == i) {
                somma2++;
            }
        }

        System.out.println("\nIl numero di occorrenze 1 è: " + somma);
        System.out.println("Il numero di occorrenze 2 è: " + somma2);
        s.close();
    }
}
