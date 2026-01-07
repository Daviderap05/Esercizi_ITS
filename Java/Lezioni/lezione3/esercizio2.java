package Lezioni.lezione3;

import java.util.Scanner;

public class esercizio2 {
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

        int cont = 0;
        for (int i = A.length - 1; i >= 0; i--) {
            B[cont] = A[i];
            cont++;
        }
        
        System.out.println("Array B copiato, al contrario, da A:");
        for (int i = 0; i < n; i++) {
            System.out.print(B[i] + " ");
        }
    }
}