package Esercitazioni.ArcaDiNoe.Animali.AnimaliA;

import Esercitazioni.ArcaDiNoe.Animali.Animale;

public abstract class AnimaleVolatile implements Animale {

    @Override
    public String categoria() {
        return "Animale volatile";
    }

    @Override
    public String toString() {
        return categoria() + " - " + this.getClass().getSimpleName() + " - " + verso();
    }
}
