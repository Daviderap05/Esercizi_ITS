package com.observer;

import java.util.Random;

public class Allievo implements TestObserver, Runnable {
    private String nome;
    private int domandeRisposte;
    private volatile boolean tempoFinito; 
    
    // Aggiungiamo un riferimento al Thread che sta eseguendo questo allievo
    private Thread threadCorrente; 

    public Allievo(String nome) {
        this.nome = nome;
        this.domandeRisposte = 0;
        this.tempoFinito = false;
    }

    @Override
    public void tempoScaduto() {
        this.tempoFinito = true;
        
        // Se il thread è in esecuzione (magari in sleep), lo interrompiamo SUBITO
        if (threadCorrente != null) {
            threadCorrente.interrupt(); 
        }
    }

    @SuppressWarnings("BusyWait")
    @Override
    public void run() {
        // Salviamo il riferimento al thread che sta eseguendo il metodo run()
        this.threadCorrente = Thread.currentThread(); 
        
        System.out.println("[ALLIEVO] " + nome + " sta eseguendo il test...");
        Random random = new Random();
        
        while (!tempoFinito) {
            try {
                int tempoRisposta = 500 + random.nextInt(1000);
                
                // Lo studente "pensa"
                Thread.sleep(tempoRisposta);
                
                // Se arriva qui senza essere interrotto, ha completato la domanda
                domandeRisposte++;
                
            } catch (InterruptedException e) {
                // Questa eccezione viene lanciata se il Timer chiama tempoScaduto()
                // ed esegue l'interrupt() proprio mentre l'allievo è in sleep.
                // Usciamo immediatamente dal ciclo!
                System.out.println("[!] " + nome + " è stato fermato mentre pensava a una domanda!");
                break; 
            }
        }
        
        System.out.println("-> L'allievo " + nome + " annuncia di aver risposto a " + domandeRisposte + " domande.");
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
}
