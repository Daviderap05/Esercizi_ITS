package com.spring2.demo.mapper;

import com.spring2.demo.dto.UtenteDTO;
import com.spring2.demo.entity.Utente;

public class Mapper {

    public static Utente daUtenteDTOAUtente(UtenteDTO dto) {
        return new Utente (dto.getIdUtente(), dto.getNome(), dto.getMail(), dto.getTelefono(), dto.getMail());
    }

    public static UtenteDTO daUtenteAUtenteDTO(Utente utente) {
        return new UtenteDTO(utente.getIdUtente(), utente.getNome(), utente.getCognome(), utente.getMail(), utente.getTelefono());
    }
}