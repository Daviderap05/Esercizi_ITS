package com.its.music;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

import com.its.music.music.Player;

@SpringBootApplication
public class MusicApplication {
	public static void main(String[] args) {
		ApplicationContext context = SpringApplication.run(MusicApplication.class, args);

		Player p = context.getBean(Player.class);
		p.playInstrument();
	}
}
