package Lezioni.lezione3;

import java.util.Scanner;

public class esercizio1 {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Inserisci la dimensione dell'array: ");
        int n = s.nextInt();

        int[] A = new int[n];
        int[] B = new int[n];

        System.out.println("Inserisci gli elementi di A:");
        for (int i = 0; i < n; i++) {
            A[i] = s.nextInt();
        }

        for (int i = 0; i < n; i++) {
            B[i] = A[i];
        }

        System.out.println("Array B copiato da A:");
        for (int i = 0; i < n; i++) {
            System.out.print(B[i] + " ");
        }
    }
}
