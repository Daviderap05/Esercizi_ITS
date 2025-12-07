package lezione2;

import java.util.Date;
import java.util.Scanner;

public class esercizio1 {
    public static void main(String[] args) {
        Date data_fine = new Date(0, 0, 0, 15, 30);
        Date data_corrente = new Date();
        Scanner s = new Scanner(System.in);

        int ore_f = data_fine.getHours();
        int min_f = data_fine.getMinutes();

        System.out.print("Inserire l'ora corrente: ");
        data_corrente.setHours(s.nextInt());

        System.out.print("Inserire i minuti correnti: ");
        data_corrente.setMinutes(s.nextInt());

        int ore_c = data_corrente.getHours();
        int min_c = data_corrente.getMinutes();

        if (ore_c == 18 && min_c == 00) {
            System.out.println("\nDRIIIIIIIIIINNNNNNNNNNN");
        } else if (ore_c > ore_f) {
            System.out.println("\nLa lezione è già finita");
        } else if (ore_c < 8) {
            System.out.println("\nLa lezione inizia alle 8:00");
        } else if (min_c > min_f) {
            System.out.println("\nRimangono " + ((ore_f - ore_c) - 1) + " ora/e - " + (60 - min_c + min_f) + " minuto/i.");
        } else {
            System.out.println("\nRimangono " + ((ore_f - ore_c)) + " ora/e - " + (min_f - min_c) + " minuto/i.");
        }

        s.close();
    }
}