package lezione3;

import java.util.Scanner;

public class esercizio7 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Inserisci la dimensione dell'array  A: ");
        int n_A = s.nextInt();

        int[] A = new int[n_A];

        System.out.println("Inserisci gli elementi di A:");
        for (int i = 0; i < n_A; i++) {
            A[i] = s.nextInt();
        }

        s.nextLine();
        System.out.print("Inserisci la dimensione dell'array  B: ");
        int n_B = s.nextInt();

        int[] B = new int[n_B];

        System.out.println("Inserisci gli elementi di B:");
        for (int i = 0; i < n_B; i++) {
            B[i] = s.nextInt();
        }

        for (int i = 0; i < n_A; i++) {
            for (int j = 0; j < n_B; j++) {
                if (A[i] == B[j]) {
                    System.out.println(A[i]);
                    break;
                }
            }
        }
    }
}