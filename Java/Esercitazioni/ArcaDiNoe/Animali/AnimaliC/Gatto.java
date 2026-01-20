package Esercitazioni.ArcaDiNoe.Animali.AnimaliC;

import Esercitazioni.ArcaDiNoe.Animali.AnimaliA.AnimaleTerrestre;

public class Gatto extends AnimaleTerrestre {

    @Override
    public String verso() {
        return "Miao";
    }

    @Override
    public String toString() {
        return "Sono un Gatto, " + categoria() + ", verso: " + verso();
    }
}
