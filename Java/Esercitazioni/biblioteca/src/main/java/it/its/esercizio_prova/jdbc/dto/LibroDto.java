package it.its.esercizio_prova.jdbc.dto;

public class LibroDto {
    private int id;
    private String titolo;
    private String autore;
    private Double prezzo;

    public LibroDto(int id, String titolo, String autore, Double prezzo) {
        this.id = id;
        this.titolo = titolo;
        this.autore = autore;
        this.prezzo = prezzo;
    }

    public LibroDto(String titolo, String autore, Double prezzo) {
        this.titolo = titolo;
        this.autore = autore;
        this.prezzo = prezzo;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitolo() {
        return titolo;
    }

    public void setTitolo(String titolo) {
        this.titolo = titolo;
    }

    public String getAutore() {
        return autore;
    }

    public void setAutore(String autore) {
        this.autore = autore;
    }

    public Double getPrezzo() {
        return prezzo;
    }

    public void setPrezzo(Double prezzo) {
        this.prezzo = prezzo;
    }
}
