package com.its.rubrica.rubrica_telefonica.dto;

import java.time.LocalDate;
import java.util.HashSet;
import java.util.Set;

public class RubricaDTO {

    private String nomeProprietario, id;
    private LocalDate annoCreazione;
    private Set<ContattoDTO> contatti;

    public RubricaDTO() {
        this.contatti = new HashSet<>();
    }

    public RubricaDTO(LocalDate annoCreazione, Set<ContattoDTO> contatti, String id, String nomeProprietario) {
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

    public Set<ContattoDTO> getContatti() {
        return contatti;
    }

    public void setContatti(Set<ContattoDTO> contatti) {
        this.contatti = contatti;
    }
}
