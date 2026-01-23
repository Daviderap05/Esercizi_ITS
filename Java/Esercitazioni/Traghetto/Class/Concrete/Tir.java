package Class.Concrete;

import Class.Astratte.Veicolo;

public class Tir extends Veicolo {

    private double tonnellate;

    public Tir(String targa, double tonnellate) {
        super(targa);
        if (tonnellate < 0)
            throw new IllegalArgumentException("Tonnellate negative");
        this.tonnellate = tonnellate;
    }

    @Override
    public double calcolaTariffa() {
        if (passeggeri.size() < 1 || passeggeri.size() > 3)
            throw new IllegalStateException("Numero passeggeri tir non valido");

        double base = 12.5;
        double costoMerce = tonnellate * 0.5;

        return base + costoMerce + costoPasseggeri();
    }
}
