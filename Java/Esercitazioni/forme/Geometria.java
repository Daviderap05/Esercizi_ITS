package Esercitazioni.Forme;

import java.util.Scanner;

public class Geometria {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String ris;
        String forma;
        Cerchio cerchio;
        Rettangolo rettangolo;

        while (true) {

            cerchio = null;
            rettangolo = null;

            do {
                System.out.print("Inserire la forma geometrica (c/r): ");
                forma = s.next().toLowerCase();

                if (!forma.equals("c") && !forma.equals("r")) {
                    System.err.println("Attenzione inserire solo C o R\n");
                }

            } while (!forma.equals("c") && !forma.equals("r"));

            switch (forma) {
                case "c" -> {
                    while (true) {
                        int r;
                        try {
                            System.out.print("Inserire il raggio: ");
                            r = s.nextInt();
                        } catch (Exception e) {
                            System.err.println("Errore il raggio deve essere un numero intero positivo\n");
                            s.nextLine();
                            continue;
                        }

                        if (r > 0) {
                            cerchio = new Cerchio(r);
                            break;
                        } else {
                            System.err.println("Errore il raggio deve essere positivo\n");
                        }
                    }
                }

                case "r" -> {
                    int base;
                    int altezza;

                    while (true) {
                        try {
                            System.out.print("Inserire la base: ");
                            base = s.nextInt();
                        } catch (Exception e) {
                            System.err.println("Errore la base deve essere un numero intero positivo\n");
                            s.nextLine();
                            continue;
                        }

                        if (base > 0) {
                            break;
                        } else {
                            System.err.println("Errore la base deve essere positiva\n");
                        }
                    }

                    while (true) {
                        try {
                            System.out.print("Inserire l'altezza: ");
                            altezza = s.nextInt();
                        } catch (Exception e) {
                            System.err.println("Errore l'altezza deve essere un numero intero positivo\n");
                            s.nextLine();
                            continue;
                        }

                        if (altezza > 0) {
                            rettangolo = new Rettangolo(base, altezza);
                            break;
                        } else {
                            System.err.println("Errore l'altezza deve essere positiva\n");
                        }
                    }
                }
            }

            do {
                System.out.print("Calcolo Area o Perimetro (a/p): ");
                ris = s.next().toLowerCase();

                if (!ris.equals("a") && !ris.equals("p")) {
                    System.err.println("Attenzione inserire solo A o P\n");
                }

            } while (!ris.equals("a") && !ris.equals("p"));

            double risultato;
            switch (ris) {
                case "a" -> {
                    if (forma.equals("c")) {
                        risultato = cerchio.calcolaArea();
                        System.out.println("Il risultato dell'area è: " + risultato);
                    } else {
                        risultato = rettangolo.calcolaArea();
                        System.out.println("Il risultato dell'area è: " + risultato);
                    }
                }

                case "p" -> {
                    if (forma.equals("c")) {
                        risultato = cerchio.calcolaPerimetro();
                        System.out.println("Il risultato del perimetro è: " + risultato);
                    } else {
                        risultato = rettangolo.calcolaPerimetro();
                        System.out.println("Il risultato del perimetro è: " + risultato);
                    }
                }
            }

            do {
                System.out.print("\nVuoi ricominciare (s/n): ");
                ris = s.next().toLowerCase();

                if (!ris.equals("s") && !ris.equals("n")) {
                    System.err.println("Attenzione inserire solo 's' o 'n'");
                }

            } while (!ris.equals("s") && !ris.equals("n"));

            if (ris.equals("n")) {
                System.out.println("Arrivederci");
                s.close();
                break;
            } else {
                System.out.println("Ricominciamo :)\n\n");
            }
        }
    }
}