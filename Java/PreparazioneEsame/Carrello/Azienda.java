public class Azienda extends Cliente {

    public Azienda(String nome) {
        super(nome, 0);
    }

    public Azienda(String nome, double conto) {
        super(nome, conto);
    }

    @Override
    public double getMoltiplicatoreOrdine() {
        return 1.1;
    }
}