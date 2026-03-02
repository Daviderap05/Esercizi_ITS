package com.spring2.demo.service;

import java.util.List;

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
}