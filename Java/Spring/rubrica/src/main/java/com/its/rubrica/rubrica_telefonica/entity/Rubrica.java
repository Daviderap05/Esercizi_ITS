package com.its.rubrica.rubrica_telefonica.entity;

import java.time.LocalDate;
import java.util.HashSet;
import java.util.Set;

public class Rubrica {
    
    private String nomeProprietario, id;
    private LocalDate annoCreazione;
    private Set<Contatto> contatti;

    public Rubrica() {
        this.contatti = new HashSet<>();
    }

    public Rubrica(LocalDate annoCreazione, Set<Contatto> contatti, String id, String nomeProprietario) {
        this.contatti = new HashSet<>();
        this.annoCreazione = annoCreazione;
        this.contatti = contatti;
        this.id = id;
        this.nomeProprietario = nomeProprietario;
    }

    public String getNomeProprietario() {
        return nomeProprietario;
    }

    public void setNomeProprietario(String nomeProprietario) {
        this.nomeProprietario = nomeProprietario;
    }
    
    public LocalDate getAnnoCreazione() {
        return annoCreazione;
    }

    public void setAnnoCreazione(LocalDate annoCreazione) {
        this.annoCreazione = annoCreazione;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Set<Contatto> getContatti() {
        return contatti;
    }

    public void setContatti(Set<Contatto> contatti) {
        this.contatti = contatti;
    }
}
