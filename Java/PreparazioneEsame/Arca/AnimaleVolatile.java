public abstract class AnimaleVolatile implements Animale {

    private static final String CATEGORIA = "Animale Volatile";

    public static String getCategoria() {
        return AnimaleVolatile.CATEGORIA;
    }

    @Override
    public String categoria() {
        return AnimaleVolatile.CATEGORIA;
    }

    @Override
    public String toString() {
        return "Categoria: " + AnimaleVolatile.CATEGORIA;
    }
}
