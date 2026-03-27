package com.observer;

import java.util.ArrayList;
import java.util.List;

public class TimerTest implements TimerSubject, Runnable {
    private final List<TestObserver> observers;
    private final int secondiAssegnati;

    public TimerTest(int secondiAssegnati) {
        this.observers = new ArrayList<>();
        this.secondiAssegnati = secondiAssegnati;
    }

    @Override
    public void addObserver(TestObserver o) {
        observers.add(o);
    }

    @Override
    public void removeObserver(TestObserver o) {
        observers.remove(o);
    }

    @Override
    public void notifyObservers() {
        for (TestObserver o : observers) {
            o.tempoScaduto();
        }
    }

    @Override
    public void run() {
        System.out.println("[TIMER] Il test è iniziato! Tempo a disposizione: " + secondiAssegnati + " secondi.");
        try {
            Thread.sleep(secondiAssegnati * 1000L);
        } catch (InterruptedException e) {
            System.err.println("Timer interrotto.");
        }
        
        System.out.println("\n[TIMER] DRIIIN! Tempo scaduto! Consegna dei compiti in corso...\n");
        notifyObservers();
    }
}
