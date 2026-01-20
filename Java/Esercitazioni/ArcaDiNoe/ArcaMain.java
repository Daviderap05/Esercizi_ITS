package Esercitazioni.ArcaDiNoe;

import Esercitazioni.ArcaDiNoe.Animali.AnimaliC.Airone;
import Esercitazioni.ArcaDiNoe.Animali.AnimaliC.Canarino;
import Esercitazioni.ArcaDiNoe.Animali.AnimaliC.Cane;
import Esercitazioni.ArcaDiNoe.Animali.AnimaliC.Gatto;

public class ArcaMain {
    public static void main(String[] args) {

        Arca arca = new Arca();

        // Terrestri
        arca.salva(new Cane());
        arca.salva(new Cane());
        arca.salva(new Cane()); // NON entra: max 2 per specie

        arca.salva(new Gatto());
        arca.salva(new Gatto());
        arca.salva(new Gatto()); // NON entra

        // Volatili
        arca.salva(new Canarino());
        arca.salva(new Airone());
        arca.salva(new Airone());
        arca.salva(new Airone()); // NON entra

        System.out.println("Numero animali salvati: " + arca.getNumeroAnimali());
        System.out.println("Coro: " + arca.coro());
        System.out.println("\n--- Lista animali ---");
        System.out.println(arca.toString());
    }
}