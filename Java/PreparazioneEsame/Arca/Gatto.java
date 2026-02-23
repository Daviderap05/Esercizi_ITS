public class Gatto extends AnimaleTerrestre {

    @Override
    public String verso() {
        return "Miao";
    }

    @Override
    public String toString() {
        return "Categoria: " + categoria() + ", Verso: " + verso();
    }
}