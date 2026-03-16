package com.its.rubrica.rubrica_telefonica.service;

import java.time.LocalDate;
import java.util.Comparator;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.its.rubrica.rubrica_telefonica.dao.DAORubriche;
import com.its.rubrica.rubrica_telefonica.dto.ContattoDTO;
import com.its.rubrica.rubrica_telefonica.dto.OwnersTotalDTO;
import com.its.rubrica.rubrica_telefonica.dto.RubricaBasicInfoDTO;
import com.its.rubrica.rubrica_telefonica.dto.RubricaDTO;
import com.its.rubrica.rubrica_telefonica.dto.RubricaReportDTO;
import com.its.rubrica.rubrica_telefonica.entity.Rubrica;
import com.its.rubrica.rubrica_telefonica.mapper.Mapper;

@Service
public class RubricaServiceImpl implements RubricaService {

    @Autowired
    private DAORubriche dao;

    @Override
    public RubricaDTO aggiornaAnno(String id, LocalDate nuovoAnno) {
        Rubrica rubrica = dao.selectRubrById(id);

        rubrica.setAnnoCreazione(nuovoAnno);

        return Mapper.toRubricaDTO(rubrica);
    }

    @Override
    public RubricaDTO aggiornaProprietario(String id, String nuovoNome) {
        Rubrica rubrica = dao.selectRubrById(id);

        rubrica.setNomeProprietario(nuovoNome);

        return Mapper.toRubricaDTO(rubrica);
    }

    @Override
    public void aggiungiContatto(String idRubrica, ContattoDTO contattoDto) {
        dao.insertContact(idRubrica, Mapper.toContattoEntity(contattoDto));
    }

    @Override
    public List<ContattoDTO> cercaPerGruppo(String idRubrica, String gruppo) {
        return dao.selectAllCont(idRubrica).stream()
                .filter(c -> c.getGruppo().equals(gruppo))
                .map(c -> Mapper.toContattoDTO(c))
                .toList();
    }

    @Override
    public ContattoDTO cercaPerNumero(String idRubrica, String numero) {
        return Mapper.toContattoDTO(
                dao.selectAllCont(idRubrica).stream()
                        .filter(c -> c.getNumero().equals(numero))
                        .findFirst()
                        .orElseThrow(() -> new RuntimeException("Contatto non trovato")));
    }

    @Override
    public int contaPerGruppo(String idRubrica, String gruppo) {
        return (int) dao.selectAllCont(idRubrica).stream()
                .filter(c -> c.getGruppo().equals(gruppo))
                .count();
    }

    @Override
    public void creaRubrica(RubricaDTO rubricaDto) {
        dao.insert(Mapper.toRubricaEntity(rubricaDto));
    }

    @Override
    public void eliminaContatto(String idRubrica, String idContatto) {
        dao.deleteCont(idRubrica, idContatto);
    }

    @Override
    public void eliminaInteroGruppo(String idRubrica, String gruppo) {
        List<ContattoDTO> contatti = cercaPerGruppo(idRubrica, gruppo);

        for (ContattoDTO c : contatti) {
            dao.deleteCont(idRubrica, c.getId());
        }
    }

    @Override
    public void eliminaRubrica(String id) {
        dao.delete(id);
    }

    @Override
    public List<ContattoDTO> getAllContatti(String idRubrica) {
        return dao.selectAllCont(idRubrica).stream()
                .map(c -> Mapper.toContattoDTO(c))
                .toList();
    }

    @Override
    public List<RubricaDTO> getAllRubriche() {
        return dao.selectAllRubr().stream()
                .map(r -> Mapper.toRubricaDTO(r))
                .toList();
    }

    @Override
    public List<LocalDate> getAnniCreazioneOrdinati() {
        return dao.selectAllRubr().stream()
                .map(r -> r.getAnnoCreazione())
                .sorted()
                .toList();
    }

    @Override
    public ContattoDTO getContattoPerId(String idRubrica, String idContatto) {
        return Mapper.toContattoDTO(dao.selectContById(idRubrica, idContatto));
    }

    @Override
    public RubricaBasicInfoDTO getInfoBaseRubrica(String id) {
        return Mapper.toBasicInfoDTO(dao.selectRubrById(id));
    }

    @Override
    public int getNumeroTotaleContatti(String idRubrica) {
        return dao.selectAllCont(idRubrica).size();
    }

    @Override
    public RubricaReportDTO getReportContattiRubrica(String id) {
        return Mapper.toReportDTO(dao.selectRubrById(id));
    }

    @Override
    public OwnersTotalDTO getReportProprietari() {
        return Mapper.toOwnersTotalDTO(
                dao.selectAllRubr().stream()
                        .map(r -> r.getNomeProprietario())
                        .toList());
    }

    @Override
    public RubricaDTO getRubricaPerId(String id) {
        return Mapper.toRubricaDTO(dao.selectRubrById(id));
    }

    @Override
    public RubricaBasicInfoDTO getRubricaPiuVecchia() {
        return dao.selectAllRubr().stream()
                .min(Comparator.comparing(r -> r.getAnnoCreazione()))
                .map(r -> Mapper.toBasicInfoDTO(r))
                .orElseThrow(() -> new RuntimeException("Nessuna rubrica presente"));
    }

    @Override
    public List<ContattoDTO> getTuttiIPreferiti(String idRubrica) {
        return dao.selectAllCont(idRubrica).stream()
                .filter(c -> c.isPreferito())
                .map(c -> Mapper.toContattoDTO(c))
                .toList();
    }

    @Override
    public void invertiPreferito(String idRubrica, String idContatto) {
        ContattoDTO contatto = Mapper.toContattoDTO(dao.selectAllCont(idRubrica).stream()
                .filter(c -> c.getId().equals(idContatto))
                .findFirst()
                .orElseThrow(() -> new RuntimeException("Contatto non trovato")));

        contatto.setPreferito(!contatto.isPreferito());
        dao.updateContact(idRubrica, idContatto, Mapper.toContattoEntity(contatto));
    }

    @Override
    public ContattoDTO modificaContatto(String idRubrica, String idContatto, ContattoDTO datiNuovi) {
        return Mapper.toContattoDTO(dao.updateContact(idRubrica, idContatto, Mapper.toContattoEntity(datiNuovi)));
    }
}
