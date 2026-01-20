package Esercitazioni.ArcaDiNoe.Animali;

public interface Animale {
    String verso();
    String categoria();
    @SuppressWarnings("override")
    String toString();
}
