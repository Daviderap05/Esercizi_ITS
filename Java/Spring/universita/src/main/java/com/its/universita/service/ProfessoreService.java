package com.its.universita.service;

import java.util.Comparator;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.its.universita.dao.DAOProfessore;
import com.its.universita.dto.professori.ProfessoreDTO;
import com.its.universita.mapper.Mapper;

@Service
public class ProfessoreService {

    @Autowired
    private DAOProfessore dao;

    public List<ProfessoreDTO> getAllProfMateria(String materia) {
        return dao.selectAll().stream()
                .filter(professore -> professore.getMateria().equals(materia))
                .map(p -> Mapper.daProfessoreAProfessoreDTO(p))
                .toList();
    }

    public List<ProfessoreDTO> getAllProfSortByCogn() {
        return dao.selectAll().stream()
                .sorted(Comparator.comparing(professore -> professore.getCognome()))
                .map(p -> Mapper.daProfessoreAProfessoreDTO(p))
                .toList();
    }

    public List<String> getAllMaterie() {
        return dao.selectAll().stream()
                .map(professore -> professore.getMateria())
                .distinct()
                .toList();
    }
}
