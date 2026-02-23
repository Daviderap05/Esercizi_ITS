public class Canarino extends AnimaleVolatile {

    @Override
    public String verso() {
        return "Cip";
    }

    @Override
    public String toString() {
        return "Categoria: " + categoria() + ", Verso: " + verso();
    }
}
