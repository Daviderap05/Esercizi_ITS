package com.its.music.music;

import org.springframework.stereotype.Component;

@Component
public class Guitar implements Instrument {

    @Override
    public void play() {
        System.out.println("SI'm playing the guitar!");
    }
}
