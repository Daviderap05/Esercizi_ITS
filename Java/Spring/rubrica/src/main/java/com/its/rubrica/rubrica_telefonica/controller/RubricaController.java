package com.its.rubrica.rubrica_telefonica.controller;

import java.time.LocalDate;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.its.rubrica.rubrica_telefonica.dto.*;
import com.its.rubrica.rubrica_telefonica.service.RubricaService;

@RestController
@RequestMapping("/api/rubriche")
public class RubricaController {

    @Autowired
    private RubricaService service;

    // --- OPERAZIONI SULLE RUBRICHE ---

    @PostMapping
    public void creaRubrica(@RequestBody RubricaDTO rubrica) {
        service.creaRubrica(rubrica);
    }

    @GetMapping
    public List<RubricaDTO> getAllRubriche() {
        return service.getAllRubriche();
    }

    @GetMapping("/{id}")
    public RubricaDTO getRubrica(@PathVariable String id) {
        return service.getRubricaPerId(id);
    }

    @DeleteMapping("/{id}")
    public void eliminaRubrica(@PathVariable String id) {
        service.eliminaRubrica(id);
    }

    @GetMapping("/report-proprietari")
    public OwnersTotalDTO getReportProprietari() {
        return service.getReportProprietari();
    }

    @GetMapping("/piu-vecchia")
    public RubricaBasicInfoDTO getPiuVecchia() {
        return service.getRubricaPiuVecchia();
    }

    @GetMapping("/{id}/info-base")
    public RubricaBasicInfoDTO getInfoBaseRubrica(@PathVariable String id) {
        return service.getInfoBaseRubrica(id);
    }

    @PatchMapping("/{id}/anno")
    public RubricaDTO aggiornaAnno(@PathVariable String id, @RequestParam LocalDate nuovoAnno) {
        // Su Postman lo chiamerai: PATCH /api/rubriche/R1/anno?nuovoAnno=2024-01-01
        return service.aggiornaAnno(id, nuovoAnno);
    }

    @GetMapping("/anni-ordinati")
    public List<LocalDate> getAnniCreazioneOrdinati() {
        return service.getAnniCreazioneOrdinati();
    }

    // --- OPERAZIONI SUI CONTATTI ---

    @PostMapping("/{idRubrica}/contatti")
    public void aggiungiContatto(@PathVariable String idRubrica, @RequestBody ContattoDTO contatto) {
        service.aggiungiContatto(idRubrica, contatto);
    }

    @GetMapping("/{idRubrica}/contatti")
    public List<ContattoDTO> getContatti(@PathVariable String idRubrica) {
        return service.getAllContatti(idRubrica);
    }

    @PutMapping("/{idRubrica}/contatti/{idContatto}")
    public ContattoDTO modificaContatto(@PathVariable String idRubrica, @PathVariable String idContatto,
            @RequestBody ContattoDTO dati) {
        return service.modificaContatto(idRubrica, idContatto, dati);
    }

    @PatchMapping("/{idRubrica}/contatti/{idContatto}/preferito")
    public void invertiPreferito(@PathVariable String idRubrica, @PathVariable String idContatto) {
        service.invertiPreferito(idRubrica, idContatto);
    }

    @DeleteMapping("/{idRubrica}/contatti/gruppo/{gruppo}")
    public void eliminaGruppo(@PathVariable String idRubrica, @PathVariable String gruppo) {
        service.eliminaInteroGruppo(idRubrica, gruppo);
    }

    @GetMapping("/{idRubrica}/report")
    public RubricaReportDTO getReportRubrica(@PathVariable String idRubrica) {
        return service.getReportContattiRubrica(idRubrica);
    }

    @DeleteMapping("/{idRubrica}/contatti/{idContatto}")
    public void eliminaSingoloContatto(@PathVariable String idRubrica, @PathVariable String idContatto) {
        service.eliminaContatto(idRubrica, idContatto);
    }

    @GetMapping("/{idRubrica}/contatti/filtra-gruppo/{gruppo}")
    public List<ContattoDTO> getPerGruppo(@PathVariable String idRubrica, @PathVariable String gruppo) {
        return service.cercaPerGruppo(idRubrica, gruppo);
    }

    @GetMapping("/{idRubrica}/contatti/cerca-numero")
    public ContattoDTO getPerNumero(@PathVariable String idRubrica, @RequestParam String numero) {
        return service.cercaPerNumero(idRubrica, numero);
    }

    @GetMapping("/{idRubrica}/contatti/preferiti")
    public List<ContattoDTO> getPreferiti(@PathVariable String idRubrica) {
        return service.getTuttiIPreferiti(idRubrica);
    }

    @PatchMapping("/{id}/proprietario")
    public RubricaDTO aggiornaProprietario(@PathVariable String id, @RequestParam String nuovoNome) {
        return service.aggiornaProprietario(id, nuovoNome);
    }

    @GetMapping("/{idRubrica}/contatti/{idContatto}")
    public ContattoDTO getContattoPerId(@PathVariable String idRubrica, @PathVariable String idContatto) {
        return service.getContattoPerId(idRubrica, idContatto);
    }

    @GetMapping("/{idRubrica}/contatti/totale")
    public int getNumeroTotaleContatti(@PathVariable String idRubrica) {
        return service.getNumeroTotaleContatti(idRubrica);
    }

    @GetMapping("/{idRubrica}/contatti/gruppo/{gruppo}/totale")
    public int contaPerGruppo(@PathVariable String idRubrica, @PathVariable String gruppo) {
        return service.contaPerGruppo(idRubrica, gruppo);
    }
}