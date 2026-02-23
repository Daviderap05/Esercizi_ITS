public class TamMain {
    public static void main(String[] args) {
        Tam t1 = new Tam("Fido", "DRAGO");
        System.out.println(t1.getSpecie());
        System.out.println(t1.getPeso());

        Tam t2 = new Tam("micio", "GaTto");
        System.out.println(t2.getSpecie());
        System.out.println(t2.getPeso());

        t1.gioca();
        t1.gioca();
        t1.gioca();
    }
}
