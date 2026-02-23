import java.util.Date;

public class Imp {
    private String nome;
    private double salario;
    private Date dataAssunzione;

    public Imp(Date dataAssunzione, String nome, double salario) {
        this.dataAssunzione = dataAssunzione;
        this.nome = nome.toLowerCase();
        this.salario = salario;
    }

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome.toLowerCase();
    }

    public double getSalario() {
        return this.salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public Date getDataAssunzione() {
        return this.dataAssunzione;
    }

    public void setDataAssunzione(Date dataAssunzione) {
        this.dataAssunzione = dataAssunzione;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Impiegato{");
        sb.append("Nome=").append(this.nome.toUpperCase());
        sb.append(", Salario=").append(this.salario);
        sb.append(", Data assunzione=").append(this.dataAssunzione);
        sb.append('}');
        return sb.toString();
    }


}
