package com.its.prodotti.dao;

import java.util.HashMap;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.its.prodotti.entity.Prodotto;

@Repository
public class ProdottiImpl implements DAOProdotti {
    
    private Map<Integer, Prodotto> mappa = new HashMap<>();

    @Override
    public void insert(Prodotto prodotto) {
        if (mappa.containsKey(prodotto.getId())) {
            throw new RuntimeException ("ID già presente");
        }

        mappa.put(prodotto.getId(), prodotto);
    }

    @Override
    public Prodotto selectById(int id) {
        Prodotto prodotto = mappa.get(id);

        if (prodotto == null) {
            throw new RuntimeException ("ID inesistente");
        }

        return prodotto;
    }

    public Map<Integer, Prodotto> getMappa() {
        return mappa;
    }

    public void setMappa(Map<Integer, Prodotto> mappa) {
        this.mappa = mappa;
    }
}
