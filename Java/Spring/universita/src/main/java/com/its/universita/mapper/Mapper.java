package com.its.universita.mapper;

import com.its.universita.dto.ProfessoreDTO;
import com.its.universita.dto.StudenteDTO;
import com.its.universita.entity.Professore;
import com.its.universita.entity.Studente;

public class Mapper {
    public static Studente daStudenteDTOAStudente(StudenteDTO dto) {
        return new Studente(dto.getMatricola(), dto.getNome(), dto.getCognome(), dto.getIndirizzo(), dto.getAnnoNascita(), dto.getAnnoImmatricolazione());
    }

    public static StudenteDTO daStudenteAStudenteDTO(Studente studente) {
        return new StudenteDTO(studente.getMatricola(), studente.getNome(), studente.getCognome(), studente.getIndirizzo(), studente.getAnnoNascita(), studente.getAnnoImmatricolazione());
    }

    public static Professore daProfessoreDTOAProfessore(ProfessoreDTO dto) {
        return new Professore(dto.getId(), dto.getNome(), dto.getCognome(), dto.getMateria());
    }

    public static ProfessoreDTO daProfessoreAProfessoreDTO(Professore professore) {
        return new ProfessoreDTO(professore.getId(), professore.getNome(), professore.getCognome(), professore.getMateria());
    }
}
