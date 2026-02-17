package Lezioni.lezione6;

public class Main {
    @SuppressWarnings("CallToPrintStackTrace")

    public static void main(String[] args) {
        System.out.println(Thread.currentThread());

        Counter c1 = new Counter("pippo", 20);
        c1.setPriority(10);
        c1.start();

        Counter c2 = new Counter("pluto", 20);
        c2.start();

        CountDown cd = new CountDown("minni", 50);
        Thread t = new Thread(cd, cd.getNome());
        t.start();

        // dopo che finiscono il lavoro stampa la frase
        try {
            c1.join();
            c2.join();
            t.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Fine lavoro del main");
    }
}
