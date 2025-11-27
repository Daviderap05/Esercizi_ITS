import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class esercizio6 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Inserisci il numero: ");
        int n = s.nextInt();

        List<Integer> nums = new ArrayList<>();
        nums.add(1);

        int div = 2;
        while (div <= n) {
            if (n % div == 0) {
                nums.add(div);
                n /= div;
            } else {
                div++;
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < nums.size(); i++) {
            sb.append(nums.get(i));
            if (i < nums.size() - 1) {
                sb.append("*");
            }
        }
        
        String risultato = sb.toString();
        System.out.println(risultato);
        s.close();
    }
}