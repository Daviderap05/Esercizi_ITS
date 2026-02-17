package Esercitazioni.Corridori;

import java.util.ArrayList;

public class Corridore implements Runnable {

    private static final ArrayList<Corridore> classifica = new ArrayList<>();

    private final int GIRI = 5;
    private String nome;

    public Corridore(String nome) {
        this.nome = nome;
    }

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getGIRI() {
        return this.GIRI;
    }

    @Override
    @SuppressWarnings({ "MathRandomCastToInt", "CallToPrintStackTrace", "BusyWait" })
    public void run() {
        for (int i = 0; i < this.GIRI; i++) {
            System.out.println(Thread.currentThread().getName() + " ha completato la tappa: " + (i + 1));
            try {
                Thread.sleep((int) (Math.random() * 601) + 200);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        // Gestione della posizione con variabile statica/lista
        synchronized (Corridore.classifica) {
            classifica.add(this);
            int posizione = classifica.size();
            System.out.println(this.nome + " è arrivato/a in " + posizione + "° posizione.");
        }
    }

    public static Corridore getVincitore() {
        synchronized (Corridore.classifica) {
            return classifica.isEmpty() ? null : classifica.get(0);
        }
    }
}
