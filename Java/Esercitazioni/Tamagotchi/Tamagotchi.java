package Esercitazioni.Tamagotchi;

public class Tamagotchi {
    private String nome;
    private String specie;
    private double peso;
    private double altezza;
    private int energia;

    public Tamagotchi(String nome, String specie) {
        this.nome = nome;

        String sp = (specie == null) ? "" : specie.trim().toLowerCase();
        switch (sp) {

            case "gatto" -> {
                this.specie = sp;
                this.altezza = 10;
                this.peso = 100;
            }

            case "canarino" -> {
                this.specie = sp;
                this.altezza = 3;
                this.peso = 10;
            }

            case "coniglio" -> {
                this.specie = sp;
                this.altezza = 10;
                this.peso = 100;
            }

            case "cane" -> {
                this.specie = sp;
                this.altezza = 20;
                this.peso = 300;
            }

            default -> {
                System.out.println("Specie non valida. Verrà impostato 'Cane' per default\n");
                this.specie = "cane";
                this.altezza = 20;
                this.peso = 300;
            }
        }

        this.energia = 3;
    }

    public Tamagotchi(String nome) {
        this.nome = nome;
        this.specie = "cane";
        this.altezza = 20;
        this.peso = 300;
        this.energia = 3;
    }

    public String getNome() {
        return this.nome;
    }

    public String getSpecie() {
        return this.specie;
    }

    public double getPeso() {
        return this.peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getAltezza() {
        return this.altezza;
    }

    public void setAltezza(double altezza) {
        this.altezza = altezza;
    }

    public int getEnergia() {
        return this.energia;
    }

    public void setEnergia(int energia) {
        if (energia >= 0 && energia <= 10) {
            this.energia = energia;
        } else {
            System.err.println("Energia deve essere tra 0 e 10");
        }

    }

    public boolean mangia() {

        if (this.energia >= 0 && this.energia < 10) {
            this.energia += 1;
            this.altezza += 1;
            this.peso += 150;
            return true;
        }
        return false;

    }

    public boolean dorme() {

        if (this.energia >= 0 && this.energia < 10) {
            this.energia += 1;
            return true;
        }

        return false;
    }

    public boolean gioca() {

        if (this.energia > 0 && this.energia <= 10 && this.peso >= 150) {
            this.peso -= 150;
            this.energia -= 1;
            return true;
        }
        return false;
    }
}
