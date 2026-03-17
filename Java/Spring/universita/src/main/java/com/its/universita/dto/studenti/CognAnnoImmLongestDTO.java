package com.its.universita.dto.studenti;

import java.time.LocalDate;

public class CognAnnoImmLongestDTO {
    private String cognome;
    private LocalDate annoImmatricolazione;

    public CognAnnoImmLongestDTO() {
    }

    public CognAnnoImmLongestDTO(String cognome, LocalDate annoImmatricolazione) {
        this.cognome = cognome;
        this.annoImmatricolazione = annoImmatricolazione;
    }

    public String getCognome() {
        return cognome;
    }

    public void setCognome(String cognome) {
        this.cognome = cognome;
    }

    public LocalDate getAnnoImmatricolazione() {
        return annoImmatricolazione;
    }

    public void setAnnoImmatricolazione(LocalDate annoImmatricolazione) {
        this.annoImmatricolazione = annoImmatricolazione;
    }
}
