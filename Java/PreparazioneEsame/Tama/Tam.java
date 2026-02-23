public class Tam {
    private final String nome;
    private final String specie;

    private int peso;
    private int altezza;
    private int energia = 3;

    public Tam(String nome, String specie) {
        this.nome = nome;

        switch (specie.toLowerCase().trim()) {
            case "gatto" -> {
                this.specie = "gatto";
                this.altezza = 10;
                this.peso = 100;
            }
            case "canarino" -> {
                this.specie = "canarino";
                this.altezza = 3;
                this.peso = 10;
            }
            case "coniglio" -> {
                this.specie = "coniglio";
                this.altezza = 10;
                this.peso = 100;
            }
            default -> {
                this.specie = "cane";
                this.altezza = 20;
                this.peso = 300;
            }
        }
    }

    public Tam(String nome) {
        this(nome, "cane");
    }

    public int getPeso() {
        return this.peso;
    }

    public void setPeso(int peso) {
        this.peso = peso;
    }

    public int getAltezza() {
        return this.altezza;
    }

    public void setAltezza(int altezza) {
        this.altezza = altezza;
    }

    public int getEnergia() {
        return this.energia;
    }

    public void setEnergia(int energia) {
        this.energia = energia;
    }

    public String getNome() {
        return this.nome;
    }

    public String getSpecie() {
        return this.specie;
    }

    public boolean mangia() {
        if (this.energia < 1) {
            return false;
        } else {
            this.setAltezza(this.getAltezza() + 1);
            this.setPeso(this.getPeso() + 150);
        }

        if (this.energia < 10) {
            this.energia += 1;
        }

        return true;
    }

    public boolean dorme() {
        if (this.energia < 10) {
            this.energia += 1;
            return true;
        } else {
            return false;
        }
    }

    public boolean gioca() {
        if (this.energia < 1) {
            return false;
        } else {
            this.setPeso(this.getPeso() - 100);
            this.energia -= 1;
            return true;
        }
    }
}
