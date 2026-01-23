package Main;

import Class.Astratte.Biglietteria;
import Class.Astratte.CodaVuotaException;
import Class.Astratte.Persona;
import Class.Concrete.Auto;
import Class.Concrete.Tir;
import Interface.Tariffabile;

public class Main {
    public static void main(String[] args) throws Exception {

        Biglietteria b = new Biglietteria();

        Persona p1 = new Persona("Mario", "Rossi");

        Auto a = new Auto("AB123CD", Auto.Tipo.STANDARD);
        a.aggiungiPasseggero(new Persona("Luigi", "Verdi"));
        a.aggiungiPasseggero(new Persona("Anna", "Bianchi"));

        Tir t = new Tir("TR999ZZ", 10);
        t.aggiungiPasseggero(new Persona("Paolo", "Neri"));

        b.aggiungiInCoda(p1);
        b.aggiungiInCoda(a);
        b.aggiungiInCoda(t);

        while (true) {
            try {
                Tariffabile x = b.riceviPagamento();
                System.out.println("Pagato: " + x.calcolaTariffa());
            } catch (CodaVuotaException e) {
                break;
            }
        }

        System.out.println("Totale cassa: " + b.getCassa());
    }
}
