package com.its.rubrica.rubrica_telefonica.dto;

import java.util.List;

public class OwnersTotalDTO {

    private List<String> nomi;
    private int totale;

    public OwnersTotalDTO() {
    }

    public OwnersTotalDTO(List<String> nomi) {
        this.nomi = nomi;
        this.totale = nomi.size();
    }

    public List<String> getNomi() {
        return nomi;
    }

    public void setNomi(List<String> nomi) {
        this.nomi = nomi;
    }

    public int getTotale() {
        return totale;
    }

    public void setTotale(int totale) {
        this.totale = totale;
    }
}
