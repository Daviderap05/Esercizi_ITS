package Esercitazioni.ArcaDiNoe.Animali.AnimaliC;

import Esercitazioni.ArcaDiNoe.Animali.AnimaliA.AnimaleVolatile;

public class Airone extends AnimaleVolatile {

    @Override
    public String verso() {
        return "Craaa";
    }

    @Override
    public String toString() {
        return "Sono un Airone, " + categoria() + ", verso: " + verso();
    }
}
