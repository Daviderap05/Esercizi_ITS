package Esercitazioni.BankAccount;

public class Banca {

    public static void main(String[] args) {

        // --- TEST Conto Corrente Standard ---
        System.out.println("=== Conto Corrente Standard ===");
        ContoCorrente conto1 = new ContoCorrente("Mario Rossi", 12345, 500.0);

        // deposito
        conto1.doMovement(new Movimento(TipoMovimento.deposito, 200.0));
        // Prelievo
        conto1.doMovement(new Movimento(TipoMovimento.prelievo, 100.0));

        // Prelievo Spropositato
        // conto1.doMovement(new Movimento(TipoMovimento.prelievo, 900.0));

        // Controllo saldo
        System.out.println(conto1.checkBalance());

        // Stampa dettagli conto
        System.out.println(conto1.checkBalance());

        // Stampa dettagli conto
        System.out.println(conto1.toString());
        System.out.println(conto1.stampaMovimenti());


        System.out.println("");


        // --- TEST Conto Risparmio ---
        System.out.println("\n=== Conto Risparmio ===");
        SavingAccount contoRisparmio = new SavingAccount("Luigi Bianchi", 54321, 1000.0, 2.5, 3);

        // deposito
        contoRisparmio.doMovement(new Movimento(TipoMovimento.deposito, 500.0));

        // Prelievi
        try {
            contoRisparmio.doMovement(new Movimento(TipoMovimento.prelievo, 200.0));
            contoRisparmio.doMovement(new Movimento(TipoMovimento.prelievo, 100.0));
            contoRisparmio.doMovement(new Movimento(TipoMovimento.prelievo, 50.0));
            // Questo prelievo dovrebbe generare eccezione perché max prelievi raggiunto
            contoRisparmio.doMovement(new Movimento(TipoMovimento.prelievo, 30.0));
        } catch (IllegalArgumentException e) {
            System.out.println("Errore: " + e.getMessage());
        }

        // Calcolo interessi
        double interessi = contoRisparmio.interessiCalcolati();
        System.out.println("Interesse maturato: " + interessi);

        // Stampa dettagli conto risparmio
        System.out.println(contoRisparmio.toString());
    }
}
