package Class.Concrete;

import Class.Astratte.Veicolo;

public class Auto extends Veicolo {

    public enum Tipo {
        MINI, STANDARD, SUV
    }

    private final Tipo tipo;

    public Auto(String targa, Tipo tipo) {
        super(targa);
        this.tipo = tipo;
    }

    @Override
    public double calcolaTariffa() {
        if (passeggeri.size() < 1 || passeggeri.size() > 5)
            throw new IllegalStateException("Numero passeggeri auto non valido");

        double base;
        switch (tipo) {
            case MINI -> base = 4;
            case STANDARD -> base = 5;
            case SUV -> base = 8.5;
            default -> base = 0;
        }

        return base + costoPasseggeri();
    }
}
