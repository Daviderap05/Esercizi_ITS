package com.its.music.music;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class Player {
    
    @Autowired
    private Instrument instrument;

    public Player() {
    }

    public void playInstrument() {
        this.instrument.play();
    }
}
