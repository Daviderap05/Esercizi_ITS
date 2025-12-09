package lezione5;

public class Tamagotchi {
    String nome;
    String specie;
    double peso;
    double altezza;
    int energia;

    public Tamagotchi(String nome, String specie) {
        this.nome = nome;

        switch (specie.toLowerCase()) {

            case "gatto" -> {
                this.specie = specie.toLowerCase();
                this.altezza = 10;
                this.peso = 100;
            }

            case "canarino" -> {
                this.specie = specie.toLowerCase();
                this.altezza = 3;
                this.peso = 10;
            }

            case "coniglio" -> {
                this.specie = specie.toLowerCase();
                this.altezza = 10;
                this.peso = 100;
            }

            case "cane" -> {
                this.specie = specie.toLowerCase();
                this.altezza = 20;
                this.peso = 300;
            }

            default -> {
                System.out.println("Specie non valida: " + specie.toLowerCase() + ". Verrà impostato 'Cane' per default");
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
        return nome;
    }

    public String getSpecie() {
        return specie;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public double getAltezza() {
        return altezza;
    }

    public void setAltezza(double altezza) {
        this.altezza = altezza;
    }

    public int getEnergia() {
        return energia;
    }

    public void setEnergia(int energia) {
        this.energia = energia;
    }

    public boolean mangia() {
        
        if (this.energia > 0 && this.energia < 10) {
            this.energia += 1;
            this.altezza += 1;
            this.peso += 150;
            return true;
        }
        return false;
        
    }

    public boolean dorme() {

        if (this.energia > 0 && this.energia < 10) {
            this.energia += 1;
            return true;
        }
        
        return false;
    }

    public boolean gioca() {

        if (this.energia > 0 && this.energia <= 10 && this.peso > 150) {
            this.peso -= 150;
            this.energia -= 1;
            return true;
        }
        return false;
    }
}
