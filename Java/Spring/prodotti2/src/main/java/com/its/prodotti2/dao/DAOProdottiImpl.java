package com.its.prodotti2.dao;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.its.prodotti2.entity.Prodotto;

@Repository
public class DAOProdottiImpl implements DAOProdotti{

    private final Map<String, Prodotto> database = new HashMap<>();

    @Override
    public void insert(Prodotto prodotto) {
        database.put(prodotto.getId(), prodotto);
    }

    @Override
    public List<Prodotto> selectAll() {
        return database.values().stream().toList();
    }

    @Override
    public Prodotto selectById(String id) {
        return database.get(id);
    }
}
