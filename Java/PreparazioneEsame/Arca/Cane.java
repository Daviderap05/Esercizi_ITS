public class Cane extends AnimaleTerrestre {
    
    @Override
    public String verso() {
        return "Bau";
    }

    @Override
    public String toString() {
        return "Categoria: " + categoria() + ", Verso: " + verso();
    }    
}
