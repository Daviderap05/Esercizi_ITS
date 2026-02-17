package Lezioni.lezione6;

public class CountDown implements Runnable {
    private int max;
    private String nome;

    public CountDown(String nome, int max) {
        super();
        this.nome = nome;
        this.max = max;
    }

    public int getMax() {
        return this.max;
    }

    public void setMax(int max) {
        this.max = max;
    }

    public String getNome() {
        return this.nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    @SuppressWarnings({ "BusyWait", "CallToPrintStackTrace", "null" })
    public void run() {
        for (int i = this.max; i > -1; i--) {
            if (i == this.max / 2) {
                String s = null;
                System.out.println(s.length());
            }

            System.out.println(Thread.currentThread().getName() + " - " + i + ", ");

            try {
                Thread.sleep(200);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
