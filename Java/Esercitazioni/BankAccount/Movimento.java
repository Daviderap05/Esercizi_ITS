package Esercitazioni.BankAccount;

import java.time.LocalDate;

public class Movimento {
    private final TipoMovimento tipo_ope;
    private final LocalDate istante;
    private double importo;

    public Movimento(TipoMovimento tipo_ope, double importo) {
        this.tipo_ope = tipo_ope;
        this.istante = LocalDate.now();
        if (importo > 0) {
            this.importo = importo;
        } else {
            throw new IllegalArgumentException("L'importo deve essere positivo.");
        }
    }

    public TipoMovimento getTipo_ope() {
        return this.tipo_ope;
    }

    public LocalDate getIstante() {
        return this.istante;
    }

    public double getImporto() {
        return this.importo;
    }

    @Override
    public String toString() {
        return "Movimento [tipo_ope=" + this.tipo_ope + ", istante=" + this.istante + ", importo=" + this.importo + "]";
    }
}