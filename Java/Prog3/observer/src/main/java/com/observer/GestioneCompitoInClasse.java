package com.observer;

public class GestioneCompitoInClasse {
    public static void main(String[] args) {
        TimerTest timer = new TimerTest(5);
        
        Allievo a1 = new Allievo("Marco");
        Allievo a2 = new Allievo("Giulia");
        Allievo a3 = new Allievo("Andrea");
        
        timer.addObserver(a1);
        timer.addObserver(a2);
        timer.addObserver(a3);
        
        Thread threadA1 = new Thread(a1);
        Thread threadA2 = new Thread(a2);
        Thread threadA3 = new Thread(a3);
        Thread threadTimer = new Thread(timer);
        
        threadA1.start();
        threadA2.start();
        threadA3.start();
        threadTimer.start();
    }
}
