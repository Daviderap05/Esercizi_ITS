package com.observer;

public interface TimerSubject {
    void addObserver(TestObserver o);
    void removeObserver(TestObserver o);
    void notifyObservers();
}
