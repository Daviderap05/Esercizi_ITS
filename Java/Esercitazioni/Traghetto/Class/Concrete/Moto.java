package Class.Concrete;

import Class.Astratte.Veicolo;

public class Moto extends Veicolo {

    public Moto(String targa) {
        super(targa);
    }

    @Override
    public double calcolaTariffa() {
        if (passeggeri.size() < 1 || passeggeri.size() > 2)
            throw new IllegalStateException("Numero passeggeri moto non valido");

        return 3.5 + costoPasseggeri();
    }
}
