package com.its.rubrica.rubrica_telefonica.entity;

import java.time.LocalDate;
import java.util.Objects;

public class Contatto {
    private String id, nome, cognome, gruppo, numero;
    private LocalDate annoNascita;
    private boolean preferito;

    public Contatto() {
    }

    public Contatto(String id, String nome, String cognome, String numero, LocalDate annoNascita) {
        this.id = id;
        this.nome = nome;
        this.cognome = cognome;
        this.numero = numero;
        this.annoNascita = annoNascita;
        this.gruppo = "default";
        this.preferito = false;
    }

    // --- LOGICA PER GESTIONE DUPLICATI ---

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || getClass() != o.getClass())
            return false;

        Contatto contatto = (Contatto) o;

        // Consideriamo uguali due contatti con stesso nome e cognome (case-insensitive)
        return Objects.equals(nome.toLowerCase(), contatto.nome.toLowerCase()) &&
                Objects.equals(cognome.toLowerCase(), contatto.cognome.toLowerCase());
    }

    @Override
    public int hashCode() {
        // Genera il codice basato solo su nome e cognome trasformati in minuscolo
        return Objects.hash(nome.toLowerCase(), cognome.toLowerCase());
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
