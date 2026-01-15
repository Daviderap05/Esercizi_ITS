package Esercitazioni.BankAccount;

public class SavingAccount extends ContoCorrente {

    private final double interessi;
    private int max_prelievi;

    public SavingAccount(String intestatario, int numero, double interessi, int max_prelievi) {
        super(intestatario, numero);
        this.interessi = interessi;
        this.max_prelievi = max_prelievi;
    }

    public SavingAccount(String intestatario, int numero, double depositoIniziale, double interessi, int max_prelievi) {
        super(intestatario, numero, depositoIniziale);
        this.interessi = interessi;
        this.max_prelievi = max_prelievi;
    }

    @Override
    public Movimento doMovement(Movimento mioMovimento) {

        if (mioMovimento.getTipo_ope() == TipoMovimento.prelievo) {
            if (this.max_prelievi <= 0) {
                throw new IllegalArgumentException("Operazioni terminate");
            }

            Movimento res = super.doMovement(mioMovimento);
            this.max_prelievi--;
            System.out.println("Prelievi rimasti: " + this.max_prelievi);
            return res;

        } else {

            return super.doMovement(mioMovimento);
        }
    }

    public double interessiCalcolati() {
        if (this.getSaldo() == 0 || this.interessi == 0) {
            throw new IllegalArgumentException("Saldo e/o interessi 0");
        }

        double interesse = this.getSaldo() * this.interessi / 100.0;
        super.doMovement(new Movimento(TipoMovimento.deposito, interesse));
        return interesse;
    }

    public double getInteressi() {
        return this.interessi;
    }

    public int getMax_prelievi() {
        return this.max_prelievi;
    }

    @Override
    public String toString() {
        return "SavingAccount [intestatario=" + this.getIntestatario() + ", numero=" + this.getNumero() + ", saldo="
                + this.getSaldo() + ", interessi=" + this.getInteressi() + ", max_prelievi=" + this.getMax_prelievi()
                + "]";
    }
}
