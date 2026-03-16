package com.its.rubrica.rubrica_telefonica.service;

import java.time.LocalDate;
import java.util.List;

import com.its.rubrica.rubrica_telefonica.dto.ContattoDTO;
import com.its.rubrica.rubrica_telefonica.dto.OwnersTotalDTO;
import com.its.rubrica.rubrica_telefonica.dto.RubricaBasicInfoDTO;
import com.its.rubrica.rubrica_telefonica.dto.RubricaDTO;
import com.its.rubrica.rubrica_telefonica.dto.RubricaReportDTO;

public interface RubricaService {

    // --- FUNZIONALITÀ RELATIVE ALLE RUBRICHE ---

    void creaRubrica(RubricaDTO rubricaDto);

    RubricaDTO getRubricaPerId(String id);

    List<RubricaDTO> getAllRubriche();

    void eliminaRubrica(String id);

    RubricaBasicInfoDTO getInfoBaseRubrica(String id);

    RubricaDTO aggiornaProprietario(String id, String nuovoNome);

    RubricaDTO aggiornaAnno(String id, LocalDate nuovoAnno);

    OwnersTotalDTO getReportProprietari();

    RubricaBasicInfoDTO getRubricaPiuVecchia();

    List<LocalDate> getAnniCreazioneOrdinati();

    RubricaReportDTO getReportContattiRubrica(String id);

    // --- FUNZIONALITÀ PER I CONTATTI ---

    void aggiungiContatto(String idRubrica, ContattoDTO contattoDto);

    ContattoDTO getContattoPerId(String idRubrica, String idContatto);

    ContattoDTO modificaContatto(String idRubrica, String idContatto, ContattoDTO datiNuovi);

    void eliminaContatto(String idRubrica, String idContatto);

    List<ContattoDTO> getAllContatti(String idRubrica);

    int getNumeroTotaleContatti(String idRubrica);

    ContattoDTO cercaPerNumero(String idRubrica, String numero);

    List<ContattoDTO> cercaPerGruppo(String idRubrica, String gruppo);

    int contaPerGruppo(String idRubrica, String gruppo);

    void eliminaInteroGruppo(String idRubrica, String gruppo);

    void invertiPreferito(String idRubrica, String idContatto);

    List<ContattoDTO> getTuttiIPreferiti(String idRubrica);
}
