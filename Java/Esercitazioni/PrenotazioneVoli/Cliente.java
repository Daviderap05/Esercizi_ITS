package Esercitazioni.PrenotazioneVoli;

@SuppressWarnings("FieldMayBeFinal")
public class Cliente extends Thread {
    private String nome;
    private int postiRichiesti;
    
    private Assegnatore assegnatore;

    public Cliente(String nome, int postiRichiesti, Assegnatore assegnatore) {
        this.nome = nome;
        this.postiRichiesti = postiRichiesti;
        this.assegnatore = assegnatore;
    }

    @Override
    public void run() {
        try {
            assegnatore.assegnaPosti(this.nome, this.postiRichiesti);
            System.out.println("SUCCESSO: " + this.nome + " ha acquistato " + this.postiRichiesti + " posti.");
        } catch (PostiNonDispException e) {
            System.out.println("FALLIMENTO: " + this.nome + " non ha potuto acquistare " + this.postiRichiesti + " posti. ("
                    + e.getMessage() + ")");
        }
    }
}
