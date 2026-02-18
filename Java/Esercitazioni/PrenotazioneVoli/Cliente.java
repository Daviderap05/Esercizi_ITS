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
            // Il cliente prova a prenotare
            assegnatore.assegnaPosti(nome, postiRichiesti);
            System.out.println("SUCCESSO: " + nome + " ha acquistato " + postiRichiesti + " posti.");
        } catch (PostiNonDispException e) {
            System.out.println("FALLIMENTO: " + nome + " non ha potuto acquistare " + postiRichiesti + " posti. ("
                    + e.getMessage() + ")");
        }
    }
}
