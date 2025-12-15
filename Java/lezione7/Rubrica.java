package lezione7;

import java.util.ArrayList;

public class Rubrica {
    private ArrayList<Contatto> rubrica = new ArrayList<>();
    private final int soglia = 10;

    public Rubrica(ArrayList<Contatto> rubrica) {

        if (rubrica.size() <= soglia) {
            this.rubrica = rubrica;
        } else {
            System.err.println("Lista troppo lunga, soglia = 10");
        }
    }

    public ArrayList<Contatto> getRubrica() {
        return this.rubrica;
    }

    public void addContact(Contatto contatto) {
        if (this.rubrica.size() < soglia) {
            this.rubrica.add(contatto);
        }
    }

    public Contatto showContact(int pos) {
        if (pos >= 0 && pos <= this.rubrica.size() - 1) {
            return this.rubrica.get(pos);
        }
        return null;
    }

    public int countContact() {
        return this.rubrica.size();
    }

    public int countFreeContact() {
        return soglia - this.rubrica.size();
    }

    public Contatto findContactByName(String nome) {
        if (nome == null) {
            System.err.println("Inserire un nome valido");
            return null;
        }
        for (Contatto contatto : this.rubrica) {
            if (contatto.getNome().toLowerCase().equals(nome.toLowerCase())) {
                return contatto;
            }
        }
        return null;
    }

    public Contatto findContactByNumber(String numero) {
        for (Contatto contatto : this.rubrica) {
            if (contatto.getNumero() != null && contatto.getNumero().equals(numero)) {
                return contatto;
            }
        }
        return null;
    }
}
