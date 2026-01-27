package Class.Astratte;

import Class.Error.CodaVuotaException;
import Interface.Tariffabile;
import java.util.LinkedList;
import java.util.Queue;

public class Biglietteria {

    private double cassa;
    private final Queue<Tariffabile> coda;

    public Biglietteria() {
        this.cassa = 0;
        this.coda = new LinkedList<>();
    }

    public void aggiungiInCoda(Tariffabile t) {
        if (t == null)
            throw new IllegalArgumentException("Oggetto nullo");
        coda.add(t);
    }

    public Tariffabile riceviPagamento() throws CodaVuotaException {
        if (coda.isEmpty())
            throw new CodaVuotaException("Coda vuota");

        Tariffabile t = coda.poll();
        this.cassa += t.calcolaTariffa();
        return t;
    }

    public double getCassa() {
        return this.cassa;
    }
}
