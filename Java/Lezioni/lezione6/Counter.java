package Lezioni.lezione6;

public class Counter extends Thread {
    private int max;

    public Counter(String nome, int max) {
        super(nome);
        this.max = max;
    }

    @Override
    @SuppressWarnings({ "BusyWait", "CallToPrintStackTrace" })
    public void run() {
        for (int i = 0; i <= this.max; i++) {
            System.out.print(Thread.currentThread().getName() +
                    " - " + i + ", ");

            try {
                Thread.sleep(200);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public int getMax() {
        return this.max;
    }

    public void setMax(int max) {
        this.max = max;
    }
}
