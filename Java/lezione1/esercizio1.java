import java.util.Scanner;

public class esercizio1 {
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);

        System.out.print("Inserisci N: ");
        int n = s.nextInt();

        System.out.print("Inserisci K: ");
        int k = s.nextInt();

        int pow = n;
        if (n > 0 && k > 0) {
            for (int i = 1; i < k; i++) {
                pow *= n;
            }
            System.out.println("\nris: " + pow);
        } else {
            System.err.println("N o K inferiori a 0");
        }

        s.close();

    }
}
