package Lezioni.lezione5;

public class esercizio1 {
    public static void main(String[] args) {

        esercizio1 es = new esercizio1();
        boolean palindroma = es.isPalindronma("osso");

        System.out.println("La parola è palindroma? " + palindroma);

        int occ = es.contaOccorrenze("Lorem ipsum Lorem ipsum ollelle", "o");

        System.out.println("La parola è palindroma? " + palindroma);
        System.out.println("Quante volte c'è la o? " + occ);

    }

    public boolean isPalindronma(String str1) {
        String str2 = "";

        for (int i = str1.length() - 1; i >= 0; i--) {
            str2 += str1.charAt(i);
        }

        return str2.equals(str1);
    }

    public int contaOccorrenze(String str, String token) {
        int occorrenze = 0;

        for (int i = 0; i <= str.length() - token.length(); i++) {
            String tmp = str.substring(i, i + token.length());
            if (tmp.equals(token)) {
                occorrenze++;
            }
        }

        return occorrenze;
    }
}
