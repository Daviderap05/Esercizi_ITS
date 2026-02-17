package Esercitazioni.Corridori;

public class Main {
    @SuppressWarnings("CallToPrintStackTrace")
    public static void main(String[] args) {
        Corridore c1 = new Corridore("pippo");
        Corridore c2 = new Corridore("pluto");
        Corridore c3 = new Corridore("minni");

        Thread t1 = new Thread(c1, c1.getNome());
        Thread t2 = new Thread(c2, c2.getNome());
        Thread t3 = new Thread(c3, c3.getNome());

        System.out.println("Gara iniziata");

        t1.start();
        t2.start();
        t3.start();

        try {
            t1.join();
            t2.join();
            t3.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        Corridore vincitore = Corridore.getVincitore();
        
        if (vincitore != null) {
            System.out.println("Il vincitore è: " + vincitore.getNome());
        } else {
            System.out.println("Nessun vincitore determinato.");
        }

        System.out.println("Fine corsa");
    }
}
