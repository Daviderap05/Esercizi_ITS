package com.spring2.demo.service;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

import com.spring2.demo.dao.DAOUtenteMappa;
import com.spring2.demo.dto.NomeCognomeDTO;
import com.spring2.demo.dto.UtenteDTO;
import com.spring2.demo.entity.Utente;
import com.spring2.demo.mapper.Mapper;

public class UtenteService {

    private final DAOUtenteMappa dao = new DAOUtenteMappa();

    public boolean registra(UtenteDTO dto) {
        // trasforma il dto in entity
        // chiama il dao
        Utente utente = Mapper.daUtenteDTOAUtente(dto);
        return dao.insert(utente);
    }

    public UtenteDTO cercaPerId(int id) {
        // chiama il dao
        Utente utente = dao.selectById(id);

        if (utente != null) {
            // trasforma da entity a dto
            UtenteDTO dto =  Mapper.daUtenteAUtenteDTO(utente);
            return dto;
        } else {
            return null;
        }
    }

    public UtenteDTO cancella(int id) {
        Utente utente = dao.delete(id);

        if (utente != null) {
            return Mapper.daUtenteAUtenteDTO(utente);
        } else {
            return null;
        }
    }

    public List<UtenteDTO> selectAll() {
        List<Utente> listaUtenti = dao.selectAll();

        // metodo 1
        // ArrayList<UtenteDTO> listaDTO = new ArrayList<>();
        // for (Utente utente : listaUtenti) {
            // UtenteDTO dto = Mapper.daUtenteAUtenteDTO(utente);
            // listaDTO.add(dto);
        // }

        //return listaDTO;

        // metodo 2
        return listaUtenti.stream()
            .map(u -> Mapper.daUtenteAUtenteDTO(u))
            .collect(Collectors.toList());
    }

    public UtenteDTO aggiorna(int id, String mail) {
        UtenteDTO utente = cercaPerId(id);

        if (utente == null) {
            return null;
        }
        
        utente.setMail(mail);
        return utente;
    }
    
    public List<UtenteDTO> ordinaPerNome() {
        // Richiamiamo il metodo selectAll() di questa classe (Service)
        // che restituisce correttamente una List<UtenteDTO>
        List<UtenteDTO> utenti = selectAll();

        utenti.sort(Comparator.comparing(u -> u.getNome()));
        return utenti;
    }

    public List<String> visualizzaNomi() {
        // Richiamiamo il metodo selectAll() di questa classe (Service)
        // che restituisce correttamente una List<UtenteDTO>
        List<UtenteDTO> utenti = selectAll();

        List<String> utentiNomi = utenti.stream()
            .map(u -> u.getNome())
            .collect(Collectors.toList());
        return utentiNomi;
    }

    public List<NomeCognomeDTO> getNomiCognomi() {
        List<Utente> lista = dao.selectAll();

        return lista.stream()
            .map(u -> new NomeCognomeDTO(u.getNome(), u.getCognome()))
            .collect(Collectors.toList());
    }
}