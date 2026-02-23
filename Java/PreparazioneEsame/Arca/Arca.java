import java.util.ArrayList;

public class Arca {
    ArrayList<Animale> arca;

    public Arca() {
        this.arca = new ArrayList<>();
    }

    public void salva(Animale a) {
        int count = 0;

        for (Animale animale : this.arca) {
            if (animale.getClass().equals(a.getClass()))
                count++;
        }

        if (count < 2)
            arca.add(a);
    }

    public int getNumeroAnimali() {
        return arca.size();
    }

    public String coro() {
        StringBuilder sb1 = new StringBuilder("| ");

        for (Animale animale : this.arca) {
            sb1.append(animale.verso()).append(" | ");
        }

        return sb1.toString();
    }

    
    @Override
    public String toString() {
        StringBuilder sb1 = new StringBuilder("| ");

        for (Animale animale : this.arca) {
            sb1.append(animale.toString()).append(" | ");
        }

        return sb1.toString();
    }
}