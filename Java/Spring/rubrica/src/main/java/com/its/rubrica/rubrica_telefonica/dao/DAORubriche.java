package com.its.rubrica.rubrica_telefonica.dao;

import java.util.List;

import com.its.rubrica.rubrica_telefonica.entity.Contatto;
import com.its.rubrica.rubrica_telefonica.entity.Rubrica;

// insert standard (rubrica, contatto), select by id (c e r), delete (c e r), update (c e r), select all
public interface DAORubriche {

    // --- FUNZIONALITÀ RELATIVE ALLE RUBRICHE ---

    void insert(Rubrica rubrica);

    Rubrica selectRubrById(String id);

    List<Rubrica> selectAllRubr();

    void delete(String id);

    // --- FUNZIONALITÀ PER UNA DATA RUBRICA (ID Rubrica sempre richiesto) ---

    void insertContact(String idRubrica, Contatto contatto);

    Contatto updateContact(String idRubrica, String idContatto, Contatto nuoviDati);

    Contatto selectContById(String idRubrica, String idContatto);

    void deleteCont(String idRubrica, String idContatto);

    List<Contatto> selectAllCont(String idRubrica);
}