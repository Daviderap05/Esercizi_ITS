import java.util.Scanner;

public class esercizio3 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Inserisci N: ");
        int n = s.nextInt();

        if (n <= 0) {
            System.err.println("N inferiore a 0");
        }else if (n == 1){
            System.out.println("Fattoriale: 1");
        }

        int fattoriale = n;

        for (int i = 0; i < n; i++) {
            fattoriale *= (n - 1);
            n -= 1;
        }

        System.out.println("Fattoriale: " + fattoriale);

        s.close();
    }
}