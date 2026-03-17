package com.its.universita.entity;

import java.time.LocalDate;

public class Studente {
    private String matricola, nome, cognome, indirizzo;
    private LocalDate annoNascita, annoImmatricolazione;

    public Studente() {
    }

    public Studente(String matricola, String nome, String cognome, String indirizzo, LocalDate annoNascita,
            LocalDate annoImmatricolazione) {
        this.matricola = matricola;
        this.nome = nome;
        this.cognome = cognome;
        this.indirizzo = indirizzo;
        this.annoNascita = annoNascita;
        this.annoImmatricolazione = annoImmatricolazione;
    }

    public String getMatricola() {
        return matricola;
    }

    public void setMatricola(String matricola) {
        this.matricola = matricola;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCognome() {
        return cognome;
    }

    public void setCognome(String cognome) {
        this.cognome = cognome;
    }

    public String getIndirizzo() {
        return indirizzo;
    }

    public void setIndirizzo(String indirizzo) {
        this.indirizzo = indirizzo;
    }

    public LocalDate getAnnoNascita() {
        return annoNascita;
    }

    public void setAnnoNascita(LocalDate annoNascita) {
        this.annoNascita = annoNascita;
    }

    public LocalDate getAnnoImmatricolazione() {
        return annoImmatricolazione;
    }

    public void setAnnoImmatricolazione(LocalDate annoImmatricolazione) {
        this.annoImmatricolazione = annoImmatricolazione;
    }
}
