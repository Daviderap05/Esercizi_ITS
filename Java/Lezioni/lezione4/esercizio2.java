package Lezioni.lezione4;

import java.util.Scanner;

public class esercizio2 {
    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);

        System.out.print("Inserisci una data: ");
        String data = s.nextLine();

        String giorno = data.substring(0, 2);
        String anno = data.substring(6);

        String mese = data.substring(3, 5);
        int mese_i = Integer.parseInt(mese);

        String mese_s = "";
        switch (mese_i) {
            case 1 -> {
                mese_s = "Gennaio";
            }
            case 2 -> {
                mese_s = "Febbraio";
            }
            case 3 -> {
                mese_s = "Marzo";
            }
            case 4 -> {
                mese_s = "Aprile";
            }
            case 5 -> {
                mese_s = "Maggio";
            }
            case 6 -> {
                mese_s = "Giugno";
            }
            case 7 -> {
                mese_s = "Luglio";
            }
            case 8 -> {
                mese_s = "Agosto";
            }
            case 9 -> {
                mese_s = "Settembre";
            }
            case 10 -> {
                mese_s = "Ottobre";
            }
            case 11 -> {
                mese_s = "Novembre";
            }
            case 12 -> {
                mese_s = "Dicembre";
            }
        }
        
        System.out.println(giorno + " " + mese_s + " " + anno);
        s.close();
    }
}
