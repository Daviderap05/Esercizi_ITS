package com.spring2.demo.service;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

import com.spring2.demo.dao.DAOUtenteMappa;
import com.spring2.demo.entity.Utente;

public class UtenteService {

    private final DAOUtenteMappa dao = new DAOUtenteMappa();

    public boolean registra(Utente utente) {
        return dao.insert(utente);
    }

    public Utente cercaPerId(int id) {
        return dao.selectById(id);
    }

    public Utente cancella(int id) {
        return dao.delete(id);
    }

    public List<Utente> selectAll() {
        return dao.selectAll();
    }

    public Utente aggiorna(int id, String mail) {
        Utente utente = cercaPerId(id);

        if (utente == null) {
            return null;
        }
        
        utente.setMail(mail);
        return utente;
    }
    public List<Utente> ordinaPerNome() {
        List<Utente> utenti = dao.selectAll();
        utenti.sort(Comparator.comparing(u -> u.getNome()));
        return utenti;
    }

    public List<String> visualizzaNomi() {
        List<Utente> utenti = dao.selectAll();
        List<String> utentiNomi = utenti.stream()
        .map(u -> u.getNome())
        .collect(Collectors.toList());
        return utentiNomi;
    }
}