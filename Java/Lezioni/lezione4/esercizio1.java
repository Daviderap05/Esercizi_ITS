package Lezioni.lezione4;

import java.util.Scanner;

public class esercizio1 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Inserisci una frase: ");
        String frase = s.nextLine();

        Boolean ris = true;
        for (int i = 0; i < frase.length(); i++) {
            if (Character.isLetter(frase.charAt(i))) {
                ris = false;
                break;
            }
        }

        if (ris) {
            System.out.println("Testo numerico");
        } else {
            System.out.println("Testo non numerico");
        }

        s.close();
    }
}
