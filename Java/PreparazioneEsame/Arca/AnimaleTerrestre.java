public abstract class AnimaleTerrestre implements Animale {

    private static final String CATEGORIA = "Animale Terrestre";

    public static String getCategoria() {
        return AnimaleTerrestre.CATEGORIA;
    }

    @Override
    public String categoria() {
        return AnimaleTerrestre.CATEGORIA;
    }

    @Override
    public String toString() {
        return "Categoria: " + AnimaleTerrestre.CATEGORIA;
    }
}
