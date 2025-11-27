import java.util.Scanner;

public class esercizio1 {
    public static void main(String[] args) {
        
        Scanner s = new Scanner(System.in);

        System.out.print("Inserisci N: ");
        int n = s.nextInt();

        System.out.print("Inserisci K: ");
        int k = s.nextInt();


        if (n > 0 && k > 0) {
            System.out.println("\nris: " + Math.pow(n, k));
        } else {
            System.err.println("N o K inferiori a 0");
        }

        s.close();

    }
}
