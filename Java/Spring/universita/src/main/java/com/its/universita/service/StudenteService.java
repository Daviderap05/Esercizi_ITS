package com.its.universita.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.its.universita.dao.DAOStudente;
import com.its.universita.dto.studenti.CognAnnoImmLongestDTO;
import com.its.universita.dto.studenti.CognAnnoYoungestDTO;
import com.its.universita.dto.studenti.StudenteDTO;
import com.its.universita.entity.Studente;
import com.its.universita.exception.RisorsaNonTrovataException;
import com.its.universita.mapper.Mapper;

@Service
public class StudenteService {

    @Autowired
    private DAOStudente dao;

    public StudenteDTO modificaIndirizzo(String matricola, String nuovoIndirizzo) {
        Studente studente = dao.selectById(matricola);
        studente.setIndirizzo(nuovoIndirizzo);

        return Mapper.daStudenteAStudenteDTO(studente);
    }

    public List<String> getAllNomi() {
        return dao.selectAll().stream()
                .map(Studente::getNome)
                .toList();
    }

    public CognAnnoImmLongestDTO getCognAnnoImmLongest() {
        return dao.selectAll().stream()
                .min((s1, s2) -> Integer.compare(s1.getAnnoImmatricolazione().getYear(), s2.getAnnoImmatricolazione().getYear()))
                .map(Mapper::toCognAnnoImmLongestDTo)
                .orElseThrow(() -> new RisorsaNonTrovataException("Nessun studente trovato"));
    }

    public CognAnnoYoungestDTO getCognAnnoYoungest() {
        return dao.selectAll().stream()
                .max((s1, s2) -> Integer.compare(s1.getAnnoNascita().getYear(), s2.getAnnoNascita().getYear()))
                .map(Mapper::toCognAnnoYoungestDTO)
                .orElseThrow(() -> new RisorsaNonTrovataException("Nessun studente trovato"));
    }
}
