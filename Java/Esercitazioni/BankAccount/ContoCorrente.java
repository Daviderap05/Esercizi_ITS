package Esercitazioni.BankAccount;

import java.util.ArrayList;

public class ContoCorrente {
    private String intestatario;
    private int numero;
    private double saldo;
    private ArrayList<Movimento> movimenti;

    public ContoCorrente(String intestatario, int numero) {
        this.intestatario = intestatario;
        this.numero = numero;
        this.saldo = 0;
        this.movimenti = new ArrayList<>();
    }

    // è dovuto al fatto che doMovement è sovrascrivibile
    @SuppressWarnings("OverridableMethodCallInConstructor")
    public ContoCorrente(String intestatario, int numero, double depositoIniziale) {
        this(intestatario, numero);
        if (depositoIniziale <= 0) {
            throw new IllegalArgumentException("Deposito iniziale negativo o 0.");
        }
        if (depositoIniziale > 0) {
            doMovement(new Movimento(TipoMovimento.deposito, depositoIniziale));
        }
    }

    public Movimento doMovement(Movimento mioMovimento) {
        if (mioMovimento.getTipo_ope() == TipoMovimento.prelievo) {
            if (mioMovimento.getImporto() > this.saldo) {
                throw new IllegalArgumentException("Saldo insufficiente.");
            }
            this.saldo -= mioMovimento.getImporto();
        } else {
            this.saldo += mioMovimento.getImporto();
        }

        this.movimenti.add(mioMovimento);
        return mioMovimento;
    }

    public boolean checkBalance() {
        double calcolato = 0.0;

        for (Movimento m : this.movimenti) {
            if (m.getTipo_ope() == TipoMovimento.prelievo)
                calcolato -= m.getImporto();
            else
                calcolato += m.getImporto();
        }

        double epsilon = 1e-6;
        return Math.abs(calcolato - this.saldo) < epsilon;
    }

    public double getSaldo() {
        return this.saldo;
    }

    public String getIntestatario() {
        return this.intestatario;
    }

    public int getNumero() {
        return this.numero;
    }

    // stampa dati conto
    @Override
    public String toString() {
        return "bankAccount [intestatario=" + this.getIntestatario() + ", numero=" + this.getNumero() + ", saldo="
                + this.getSaldo() + "]";
    }

    // stampa solo movimenti
    public String stampaMovimenti() {
        StringBuilder sb = new StringBuilder();
        for (Movimento m : this.movimenti) {
            sb.append(m).append("\n");
        }
        return sb.toString();
    }

    public ArrayList<Movimento> getMovimenti() {
        return this.movimenti;
    }
}