package com.its.prodotti2.dao;

import java.util.List;

import com.its.prodotti2.entity.Prodotto;

public interface DAOProdotti {
    public void insert (Prodotto prodotto);
    public Prodotto selectById (String id);
    public List<Prodotto> selectAll();
}
