package Esercitazioni.PrenotazioneVoli;

public class Simulazione {
    public static void main(String[] args) {
        Assegnatore assegnatoreCondiviso = new Assegnatore();

        Cliente c1 = new Cliente("Cliente_A", 5, assegnatoreCondiviso);
        Cliente c2 = new Cliente("Cliente_B", 8, assegnatoreCondiviso);
        Cliente c3 = new Cliente("Cliente_C", 6, assegnatoreCondiviso);
        Cliente c4 = new Cliente("Cliente_D", 5, assegnatoreCondiviso);

        c1.start();
        c2.start();
        c3.start();
        c4.start();
    }
}
