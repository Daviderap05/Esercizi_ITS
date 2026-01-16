package Lezioni.lezione3;

import java.util.Scanner;

public class esercizio4 {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int somma = 0;
        int somma_p = 0;
        int somma_d = 0;

        System.out.print("Inserisci la dimensione dell'array: ");
        int n = s.nextInt();

        int[] A = new int[n];

        System.out.println("Inserisci gli elementi di A:");
        for (int i = 0; i < n; i++) {
            A[i] = s.nextInt();
        }

        for (int i = 0; i < A.length; i++) {
            somma += A[i];
        }

        for (int i = 0; i < A.length; i += 2) {
            somma_p += A[i];
        }
        
        for (int i = 1; i < A.length; i += 2) {
            somma_d += A[i];
        }

        System.out.println("Somma totale: " + somma);
        System.out.println("Somma pari: " + somma_p);
        System.out.println("Somma dispari: " + somma_d);
        System.out.println("Media: " + somma/A.length);
    }
}
