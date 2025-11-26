public class Main {

    public static int function(int numero, int numero2) {
        int somma = numero + numero2;
        return somma;
    }

    public static void function2(String[] arr) {
        for (String elem : arr) {
            System.out.println(elem);
        }
    }

    public static void main(String[] args) {
        System.out.println("\n\nJava funziona!");

        for (int i = 0; i <= 12; i++) {

            if (i == 1 || i == 5) {

                System.out.print("Banana, ");
                continue;

            } else if (i == 10) {

                System.out.print("Ciao.");
                break;
            }

            System.out.print(i + ", ");
        }

        System.out.print("\n\n");

        int cont = 1;

        while (cont <= 5) {

            // nuovo sistema per lo switch senza il bisogno di break alla fine
            switch (cont) {

                case 1 -> System.out.println("Sei nel " + cont + "° case");

                case 2 -> System.out.println("Sei nel " + cont + "° case");

                case 3 -> System.out.println("Sei nel " + cont + "° case");

                default -> System.out.println("Sei nel default");

            }

            cont++;
        }

        System.out.print("\n\n");

        int n = function(2, 3);
        System.out.println(n);

        System.out.print("\n");

        // Questo è un array le liste sono diverse
        String[] arr = { "Davide", "Giulia" };
        function2(arr);
    }

}
