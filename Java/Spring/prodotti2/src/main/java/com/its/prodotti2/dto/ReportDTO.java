package com.its.prodotti2.dto;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ReportDTO {

    private Map<String, List<String>> elencoIdProdPerCat = new HashMap<>();
    private List<String> listaDescr = new ArrayList<>();
    private List<String> modProdNonDisp = new ArrayList<>();
    private int sommaPezziInMagaz;
    private int prodNonDisp;
    private Double mediaPrezziCons;

    public ReportDTO() {
    }

    public Map<String, List<String>> getElencoIdProdPerCat() {
        return elencoIdProdPerCat;
    }

    public void setElencoIdProdPerCat(Map<String, List<String>> elencoIdProdPerCat) {
        this.elencoIdProdPerCat = elencoIdProdPerCat;
    }

    public List<String> getListaDescr() {
        return listaDescr;
    }

    public void setListaDescr(List<String> listaDescr) {
        this.listaDescr = listaDescr;
    }

    public List<String> getModProdNonDisp() {
        return modProdNonDisp;
    }

    public void setModProdNonDisp(List<String> modProdNonDisp) {
        this.modProdNonDisp = modProdNonDisp;
    }

    public int getSommaPezziInMagaz() {
        return sommaPezziInMagaz;
    }

    public void setsommaPezziInMagaz(int sommaPezziInMagaz) {
        this.sommaPezziInMagaz = sommaPezziInMagaz;
    }

    public int getProdNonDisp() {
        return prodNonDisp;
    }

    public void setProdNonDisp(int prodNonDisp) {
        this.prodNonDisp = prodNonDisp;
    }

    public Double getMediaPrezziCons() {
        return mediaPrezziCons;
    }

    public void setMediaPrezziCons(Double mediaPrezziCons) {
        this.mediaPrezziCons = mediaPrezziCons;
    }
}
