package Lezioni.lezione3;

public class esercizio3 {
    public static void main(String[] args) {
        int[] A = new int[10];

        for (int i = 0; i < A.length / 2; i++) {
            A[i] = i;
        }
        
        for (int i = 0; i < A.length / 2; i++) {
            System.out.print(A[i] + " ");
        }
        
        System.out.println("");
        
        for (int i = (A.length / 2); i < A.length; i++) {
            A[i] = i;
        }

        for (int i = 0; i < A.length; i++) {
            System.out.print(A[i] + " ");
        }
    }
}
