package Esercitazioni.ArcaDiNoe;

import Esercitazioni.ArcaDiNoe.Animali.Animale;
import java.util.ArrayList;

public class Arca {

    private final ArrayList<Animale> animali;

    public Arca() {
        animali = new ArrayList<>();
    }

    public void salva(Animale a) {
        int count = 0;

        for (Animale x : animali) {
            if (x.getClass().equals(a.getClass())) {
                count++;
            }
        }

        if (count < 2) {
            animali.add(a);
        }
    }

    public int getNumeroAnimali() {
        return animali.size();
    }

    public String coro() {
        StringBuilder sb = new StringBuilder();

        for (Animale a : animali) {
            sb.append(a.verso()).append(" ");
        }

        return sb.toString().trim();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        for (Animale a : animali) {
            sb.append(a.toString()).append("\n");
        }

        return sb.toString();
    }
}
