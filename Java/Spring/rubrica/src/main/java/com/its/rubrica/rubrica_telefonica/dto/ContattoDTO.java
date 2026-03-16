package com.its.rubrica.rubrica_telefonica.dto;

import java.time.LocalDate;

public class ContattoDTO {

    private String id, nome, cognome, gruppo, numero;
    private LocalDate annoNascita;
    private boolean preferito;

    public ContattoDTO() {
    }

    public ContattoDTO(String id, String nome, String cognome, String numero, LocalDate annoNascita) {
        this.id = id;
        this.nome = nome;
        this.cognome = cognome;
        this.numero = numero;
        this.annoNascita = annoNascita;
        this.gruppo = "default";
        this.preferito = false;
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

    public String getGruppo() {
        return gruppo;
    }

    public void setGruppo(String gruppo) {
        this.gruppo = gruppo;
    }

    public LocalDate getAnnoNascita() {
        return annoNascita;
    }

    public void setAnnoNascita(LocalDate annoNascita) {
        this.annoNascita = annoNascita;
    }

    public boolean isPreferito() {
        return preferito;
    }

    public void setPreferito(boolean preferito) {
        this.preferito = preferito;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }
}
