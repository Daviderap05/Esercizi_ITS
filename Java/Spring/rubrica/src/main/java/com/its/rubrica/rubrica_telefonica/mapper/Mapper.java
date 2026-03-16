package com.its.rubrica.rubrica_telefonica.mapper;

import java.util.List;
import java.util.stream.Collectors;

import com.its.rubrica.rubrica_telefonica.dto.ContattoDTO;
import com.its.rubrica.rubrica_telefonica.dto.OwnersTotalDTO;
import com.its.rubrica.rubrica_telefonica.dto.RubricaBasicInfoDTO;
import com.its.rubrica.rubrica_telefonica.dto.RubricaDTO;
import com.its.rubrica.rubrica_telefonica.dto.RubricaReportDTO;
import com.its.rubrica.rubrica_telefonica.entity.Contatto;
import com.its.rubrica.rubrica_telefonica.entity.Rubrica;

public class Mapper {

    // Trasforma Entity -> RubricaBasicInfoDTO (Proprietario + Anno)
    public static RubricaBasicInfoDTO toBasicInfoDTO(Rubrica r) {
        return new RubricaBasicInfoDTO(r.getNomeProprietario(), r.getAnnoCreazione());
    }

    // Trasforma Entity -> RubricaReportDTO (Proprietario + Numero Contatti)
    public static RubricaReportDTO toReportDTO(Rubrica r) {
        return new RubricaReportDTO(r.getNomeProprietario(), r.getContatti().size());
    }

    // Crea il DTO per i nomi dei proprietari e il conteggio totale
    public static OwnersTotalDTO toOwnersTotalDTO(List<String> nomi) {
        return new OwnersTotalDTO(nomi);
    }

    // Trasforma Contatto -> ContattoDTO
    public static ContattoDTO toContattoDTO(Contatto c) {
        ContattoDTO dto = new ContattoDTO(c.getId(), c.getNome(), c.getCognome(), c.getNumero(), c.getAnnoNascita());

        dto.setGruppo(c.getGruppo());
        dto.setPreferito(c.isPreferito());

        return dto;
    }

    public static Contatto toContattoEntity(ContattoDTO dto) {
        Contatto c = new Contatto();

        c.setId(dto.getId());
        c.setNome(dto.getNome());
        c.setCognome(dto.getCognome());
        c.setNumero(dto.getNumero());
        c.setGruppo(dto.getGruppo());
        c.setAnnoNascita(dto.getAnnoNascita());
        c.setPreferito(dto.isPreferito());

        return c;
    }

    public static Rubrica toRubricaEntity(RubricaDTO dto) {
        Rubrica r = new Rubrica();

        r.setId(dto.getId());
        r.setNomeProprietario(dto.getNomeProprietario());
        r.setAnnoCreazione(dto.getAnnoCreazione());

        return r;
    }

    public static RubricaDTO toRubricaDTO(Rubrica r) {
        RubricaDTO dto = new RubricaDTO();

        dto.setId(r.getId());
        dto.setNomeProprietario(r.getNomeProprietario());
        dto.setAnnoCreazione(r.getAnnoCreazione());

        if (r.getContatti() != null && !r.getContatti().isEmpty()) {
            dto.setContatti(r.getContatti().stream()
                    .map(c -> Mapper.toContattoDTO(c))
                    .collect(Collectors.toSet()));
        }

        return dto;
    }
}
