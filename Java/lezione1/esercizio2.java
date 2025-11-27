import java.util.Scanner;

public class esercizio2 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Inserisci N: ");
        int n = s.nextInt();

        System.out.print("Inserisci K: ");
        int k = s.nextInt();


        if (n <= 0 || k <= 0) {
            System.err.println("N o K inferiori a 0");
        }

        double sommatoria = 0;
        int j = 1;

        for (int i = 1; i <= n; i++) {
            
            j *= k;
            sommatoria += j;
        }

        System.out.println("sommatoria K^1aN: " + sommatoria);

        s.close();
    }
}
