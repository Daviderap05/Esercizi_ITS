package com.its.prodotti2.entity;

public class Prodotto {
    
    private String id, marca, modello, descrizione, categoria;
    private Double prezzoCons, prezzoMax;
    private int qtaDisp;

    public Prodotto() {
    }

    public Prodotto(String id, String marca, String modello, String descrizione, String categoria, Double prezzoCons,
            Double prezzoMax, int qtaDisp) {
        this.id = id;
        this.marca = marca;
        this.modello = modello;
        this.descrizione = descrizione;
        this.categoria = categoria;
        this.prezzoCons = prezzoCons;
        this.prezzoMax = prezzoMax;
        this.qtaDisp = qtaDisp;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getModello() {
        return modello;
    }

    public void setModello(String modello) {
        this.modello = modello;
    }

    public String getDescrizione() {
        return descrizione;
    }

    public void setDescrizione(String descrizione) {
        this.descrizione = descrizione;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public Double getPrezzoCons() {
        return prezzoCons;
    }

    public void setPrezzoCons(Double prezzoCons) {
        this.prezzoCons = prezzoCons;
    }

    public Double getPrezzoMax() {
        return prezzoMax;
    }

    public void setPrezzoMax(Double prezzoMax) {
        this.prezzoMax = prezzoMax;
    }

    public int getQtaDisp() {
        return qtaDisp;
    }

    public void setQtaDisp(int qtaDisp) {
        this.qtaDisp = qtaDisp;
    }
}
