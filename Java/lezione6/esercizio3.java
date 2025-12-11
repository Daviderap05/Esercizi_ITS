package lezione6;

import java.util.Scanner;

public class esercizio3 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Inserisci una parola: ");
        String s = in.nextLine().toLowerCase();

        Boolean ris = true;
        for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) {
                ris = false;
                break;
            }
        }

        if (ris) {
            System.out.println("Palindromo");
        } else {
            System.out.println("Non palindromo");
        }

        in.close();
    }
}
