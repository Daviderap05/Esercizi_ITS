package com.its.rubrica.rubrica_telefonica.dto;

public class RubricaReportDTO {

    private String nomeProprietario;
    private int numeroContatti;

    public RubricaReportDTO() {
    }

    public RubricaReportDTO(String nomeProprietario, int numeroContatti) {
        this.nomeProprietario = nomeProprietario;
        this.numeroContatti = numeroContatti;
    }

    public String getNomeProprietario() {
        return nomeProprietario;
    }

    public void setNomeProprietario(String nomeProprietario) {
        this.nomeProprietario = nomeProprietario;
    }

    public int getNumeroContatti() {
        return numeroContatti;
    }

    public void setNumeroContatti(int numeroContatti) {
        this.numeroContatti = numeroContatti;
    }
}
