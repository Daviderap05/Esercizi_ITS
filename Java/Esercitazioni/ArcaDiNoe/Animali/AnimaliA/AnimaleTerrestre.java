package Esercitazioni.ArcaDiNoe.Animali.AnimaliA;

import Esercitazioni.ArcaDiNoe.Animali.Animale;

public abstract class AnimaleTerrestre implements Animale {

    @Override
    public String categoria() {
        return "Animale terrestre";
    }

    @Override
    public String toString() {
        return categoria() + " - " + this.getClass().getSimpleName() + " - " + verso();
    }
}
