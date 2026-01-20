package Esercitazioni.ArcaDiNoe.Animali.AnimaliC;

import Esercitazioni.ArcaDiNoe.Animali.AnimaliA.AnimaleVolatile;

public class Canarino extends AnimaleVolatile {

    @Override
    public String verso() {
        return "Cip cip";
    }

    @Override
    public String toString() {
        return "Sono un Canarino, " + categoria() + ", verso: " + verso();
    }
}