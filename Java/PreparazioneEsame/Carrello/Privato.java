public class Privato extends Cliente{

    public Privato(String nome) {
        super(nome, 0);
    }

    public Privato(String nome, double conto) {
        super(nome, conto);
    }

    @Override
    public double getMoltiplicatoreOrdine() {
        return 1.0;
    }
}