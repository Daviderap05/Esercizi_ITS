public abstract class Cliente {

    private String nome;
    private double conto;

    public Cliente(String nome, double conto) {
        this.nome = nome;
        
        if (conto < 0)
            throw new IllegalArgumentException("Errore conto negativo.");
        this.conto = conto;
    }

    public Cliente(String nome) {
        this(nome, 0);
    }

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getConto() {
        return this.conto;
    }

    public void setConto(double conto) {
        if (conto < 0)
            throw new IllegalArgumentException("Errore conto negativo.");

        this.conto = conto;
    }

    public abstract double getMoltiplicatoreOrdine();
}