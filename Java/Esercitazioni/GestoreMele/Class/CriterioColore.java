package Esercitazioni.GestoreMele.Class;

import Esercitazioni.GestoreMele.Interface.Criterio;

public class CriterioColore implements Criterio{
    @Override
    public boolean test(Mela mela) {
        return mela.getColore().equals("verde");
    }
}
