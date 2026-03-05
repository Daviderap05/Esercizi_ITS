package com.its.prodotti.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.its.prodotti.dao.DAOProdotti;
import com.its.prodotti.dto.ProdottoDTO;
import com.its.prodotti.entity.Prodotto;
import com.its.prodotti.mapper.Mapper;

@Service
public class ProdottoServiceImpl implements ProdottoService{

    @Autowired
    private DAOProdotti dao;

    @Override
    public void carica(ProdottoDTO dto) {
        Prodotto prodotto = Mapper.daDtoAEntity(dto);
        dao.insert(prodotto);
    }

    @Override
    public ProdottoDTO cercaPerId(int id) {
        Prodotto trovato = dao.selectById(id);
        return Mapper.daEntityADto(trovato);
    }
}
