package Lezioni.lezione3;

import java.util.Scanner;

public class esercizio6 {
    public static void main(String[] args) {
         Scanner s = new Scanner(System.in);

        System.out.print("Inserisci la dimensione dell'array: ");
        int n = s.nextInt();

        int[] A = new int[n];

        System.out.println("Inserisci gli elementi di A:");
        for (int i = 0; i < n; i++) {
            A[i] = s.nextInt();
        }

        for (int i = 0; i < A.length / 2; i++) {
            int temp = A[i];
            A[i] = A[A.length - 1 - i];
            A[A.length - 1 - i] = temp;
        }

        System.out.println("Array A copiato al contrario:");
        for (int k = 0; k < A.length; k++) {
            System.out.print(A[k] + " ");
        }
    }
}
