package com.its.universita.dto.studenti;

import java.time.LocalDate;

public class CognAnnoYoungestDTO {
    private String cognome;
    private LocalDate annoNascita;

    public CognAnnoYoungestDTO() {
    }

    public CognAnnoYoungestDTO(String cognome, LocalDate annoNascita) {
        this.cognome = cognome;
        this.annoNascita = annoNascita;
    }

    public String getCognome() {
        return cognome;
    }

    public void setCognome(String cognome) {
        this.cognome = cognome;
    }

    public LocalDate getAnnoNascita() {
        return annoNascita;
    }

    public void setAnnoNascita(LocalDate annoNascita) {
        this.annoNascita = annoNascita;
    }
}
