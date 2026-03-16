package com.its.prodotti2.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.its.prodotti2.dto.ProdottoDTO;
import com.its.prodotti2.dto.ProdottoNoIdDTO;
import com.its.prodotti2.dto.ReportDTO;
import com.its.prodotti2.service.ServiceProdotti;

@RestController
@RequestMapping("/prodotti")
public class ProdottoController {

    @Autowired
    private ServiceProdotti serviceProdotti;

    @PostMapping("/inserisci")
    public void inserisciProdotto(@RequestBody ProdottoDTO pDto) {
        serviceProdotti.insert(pDto);
    }

    @GetMapping("/tutti")
    public List<ProdottoNoIdDTO> getTuttiProdotti() {
        return serviceProdotti.selectAll();
    }

    @GetMapping("/cerca/{id}")
    public ProdottoDTO getProdottoById(@PathVariable String id) {
        return serviceProdotti.selectById(id);
    }

    @GetMapping("/report")
    public ReportDTO getReport() {
        return serviceProdotti.getReport();
    }
}
