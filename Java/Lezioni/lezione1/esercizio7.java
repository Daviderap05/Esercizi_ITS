package Lezioni.lezione1;

import java.util.Scanner;

public class esercizio7 {
    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Inserisci il giorno: ");
        int g = s.nextInt();

        System.out.print("Inserisci il mese: ");
        int m = s.nextInt();

        if (g > 31 || g < 1 || m > 12 || m < 1) {
            System.err.println("\nValori giorno/mese non coerenti");
            s.close();
            return;
        } else if ((g > 28 && m == 2) || (g == 31 && m == 4) || (g == 31 && m == 6) || (g == 31 && m == 9)
                || (g == 31 && m == 11)) {
            System.err.println("Valori giorno/mese non coerenti");
            s.close();
            return;
        }

        int[] giorniMese = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        int giorniTrascorsi = (g - 1);

        for (int i = 0; i < m - 1; i++) {
            giorniTrascorsi += giorniMese[i];
        }

        System.out.println("\nDall’inizio dell’anno sono trascorsi " + giorniTrascorsi + " giorni.");
        s.close();
    }
}
