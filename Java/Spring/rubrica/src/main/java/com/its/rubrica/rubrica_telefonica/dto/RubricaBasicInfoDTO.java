package com.its.rubrica.rubrica_telefonica.dto;

import java.time.LocalDate;

public class RubricaBasicInfoDTO {

    private String nomeProprietario;
    private LocalDate annoCreazionDate;

    public RubricaBasicInfoDTO() {
    }

    public RubricaBasicInfoDTO(String nomeProprietario, LocalDate annoCreazionDate) {
        this.nomeProprietario = nomeProprietario;
        this.annoCreazionDate = annoCreazionDate;
    }

    public String getNomeProprietario() {
        return nomeProprietario;
    }

    public void setNomeProprietario(String nomeProprietario) {
        this.nomeProprietario = nomeProprietario;
    }

    public LocalDate getAnnoCreazionDate() {
        return annoCreazionDate;
    }

    public void setAnnoCreazionDate(LocalDate annoCreazionDate) {
        this.annoCreazionDate = annoCreazionDate;
    }
}
