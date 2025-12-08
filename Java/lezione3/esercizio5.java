package lezione3;

import java.util.Scanner;

public class esercizio5 {
    public static void main(String[] args) {
         Scanner s = new Scanner(System.in);

        System.out.print("Inserisci la dimensione dell'array: ");
        int n = s.nextInt();

        int[] A = new int[n];

        System.out.println("Inserisci gli elementi di A:");
        for (int i = 0; i < n; i++) {
            A[i] = s.nextInt();
        }

        int i = 0;
        for (int j = A.length-1; j >= A.length / 2; j--) {
            System.out.print(A[i] + "" + A[j]);
            i++;
        } 
    }
}