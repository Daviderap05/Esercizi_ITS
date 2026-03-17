package com.its.universita.mapper;

import com.its.universita.dto.professori.ProfessoreDTO;
import com.its.universita.dto.studenti.CognAnnoImmLongestDTO;
import com.its.universita.dto.studenti.CognAnnoYoungestDTO;
import com.its.universita.dto.studenti.StudenteDTO;
import com.its.universita.entity.Professore;
import com.its.universita.entity.Studente;

public class Mapper {
    public static Studente daStudenteDTOAStudente(StudenteDTO dto) {
        return new Studente(dto.getMatricola(), dto.getNome(), dto.getCognome(), dto.getIndirizzo(),
                dto.getAnnoNascita(), dto.getAnnoImmatricolazione());
    }

    public static StudenteDTO daStudenteAStudenteDTO(Studente studente) {
        return new StudenteDTO(studente.getMatricola(), studente.getNome(), studente.getCognome(),
                studente.getIndirizzo(), studente.getAnnoNascita(), studente.getAnnoImmatricolazione());
    }

    public static Professore daProfessoreDTOAProfessore(ProfessoreDTO dto) {
        return new Professore(dto.getId(), dto.getNome(), dto.getCognome(), dto.getMateria());
    }

    public static ProfessoreDTO daProfessoreAProfessoreDTO(Professore professore) {
        return new ProfessoreDTO(professore.getId(), professore.getNome(), professore.getCognome(),
                professore.getMateria());
    }

    public static CognAnnoImmLongestDTO toCognAnnoImmLongestDTo(Studente studente) {
        return new CognAnnoImmLongestDTO(studente.getCognome(), studente.getAnnoImmatricolazione());
    }

    public static CognAnnoYoungestDTO toCognAnnoYoungestDTO(Studente studente) {
        return new CognAnnoYoungestDTO(studente.getCognome(), studente.getAnnoNascita());
    }
}
