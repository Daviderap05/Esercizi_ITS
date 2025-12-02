package lezione2;

import java.util.Random;
import java.util.Scanner;

public class esercizio2 {
    public static void main(String[] args) {
        Random rand = new Random();
        Scanner s = new Scanner(System.in);
        int n = rand.nextInt(1, 11);
        int cont = 1;
        int num = 0;

        System.out.println("Indovina il numero (1 - 10)\n\n");
        
        while (n != num) {
            System.out.print(cont + "°" + " tentativo: ");
            num = s.nextInt();

            if (num == n) {
                System.out.println("\nComplimenti hai indovinato in " + cont + " tentativi/o");
                break;
            } else if (num < n) {
                System.out.println("Numero troppo piccolo\n");
            } else {
                System.out.println("Numero troppo grande\n");
            }

            cont++;

        }
    }
}
