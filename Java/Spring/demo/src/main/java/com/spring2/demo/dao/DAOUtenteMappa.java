package com.spring2.demo.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.spring2.demo.entity.Utente;

public class DAOUtenteMappa {

    private final Map<Integer, Utente> mappa = new HashMap<>();

    public boolean insert(Utente utente) {
        if(mappa.containsKey(utente.getIdUtente()))
            return false;

        mappa.put(utente.getIdUtente(), utente);
        return true;

    }
    public List<Utente> selectAll(){
        return new ArrayList<>(mappa.values());
    }

    public Utente selectById(Integer idUtente) {
        return mappa.get(idUtente);
    }

    public Utente delete(Integer idUtente) {
        Utente utente = mappa.remove(idUtente);
        return utente;
    }
}