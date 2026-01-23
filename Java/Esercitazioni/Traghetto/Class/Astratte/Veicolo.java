package Class.Astratte;

import Interface.Tariffabile;
import java.util.ArrayList;

public abstract class Veicolo implements Tariffabile {

    protected String targa;
    protected ArrayList<Persona> passeggeri;

    public Veicolo(String targa) {
        this.targa = targa;
        this.passeggeri = new ArrayList<>();
    }

    public void aggiungiPasseggero(Persona p) {
        if (p == null)
            throw new IllegalArgumentException("Passeggero nullo");
        passeggeri.add(p);
    }

    protected double costoPasseggeri() {
        return passeggeri.size() * 2.5;
    }
}
