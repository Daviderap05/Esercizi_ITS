package com.its.prodotti.dao;

import com.its.prodotti.entity.Prodotto;

public interface DAOProdotti {
    public void insert (Prodotto prodotto);
    public Prodotto selectById (int id);
}
