package Esercitazioni.GestoreMele.Class;

import Esercitazioni.GestoreMele.Interface.Criterio;

public class CriterioPeso implements Criterio{

    @Override
    public boolean test(Mela mela) {
        return mela.getPeso() > 150;
    }
    
}



