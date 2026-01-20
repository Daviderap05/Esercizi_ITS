package Esercitazioni.ArcaDiNoe.Animali.AnimaliC;

import Esercitazioni.ArcaDiNoe.Animali.AnimaliA.AnimaleTerrestre;

public class Cane extends AnimaleTerrestre {

    @Override
    public String verso() {
        return "Bau bau";
    }

    @Override
    public String toString() {
        return "Sono un Cane, " + categoria() + ", verso: " + verso();
    }
}
