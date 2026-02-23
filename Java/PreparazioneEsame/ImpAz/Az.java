import java.util.ArrayList;
import java.util.Date;

public class Az {
    private String nome;
    private int capitaleSociale;

    @SuppressWarnings("FieldMayBeFinal")
    private ArrayList<Imp> listaImpiegati = new ArrayList<>();

    public Az(String nome, int capitaleSociale) {
        this.nome = nome;
        this.capitaleSociale = capitaleSociale;
    }

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public ArrayList<Imp> getListaImpiegati() {
        return this.listaImpiegati;
    }

    public void assume(Imp imp) {
        this.listaImpiegati.add(imp);
    }

    public int getNumeroImpiegati() {
        return this.listaImpiegati.size();
    }

    public void incrementaCapitale(int incremento) {
        this.capitaleSociale += incremento;
    }

    public Imp cercaImpiegato(String nome) {
        for (Imp i : this.listaImpiegati) {
            if (i.getNome().equalsIgnoreCase(nome))
                return i;
        }

        return null;
    }

    public ArrayList<Imp> cercaImpiegatiSalarioMaggiore(double salario) {
        ArrayList<Imp> ris = new ArrayList<>();

        for (Imp i : this.listaImpiegati) {
            if (i.getSalario() > salario)
                ris.add(i);
        }

        return ris;
    }

    public ArrayList<Imp> cercaImpiegatiAnzianitaMaggiore(int anni) {
        ArrayList<Imp> ris = new ArrayList<>();

        Date oggi = new Date();
        long millisecondiInUnAnno = 1000L * 60 * 60 * 24 * 365;

        for (Imp i : this.listaImpiegati) {
            long differenza = oggi.getTime() - i.getDataAssunzione().getTime();
            
            if (differenza / millisecondiInUnAnno > anni) {
                ris.add(i);
            }
        }
        return ris;
    }

    @Override
    public String toString() {
        return "Azienda: " + this.nome + ", Capitale: " + this.capitaleSociale + ", Dipendenti: " + this.listaImpiegati;
    }
}