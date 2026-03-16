package com.its.prodotti2.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.its.prodotti2.dao.DAOProdotti;
import com.its.prodotti2.dto.ProdottoDTO;
import com.its.prodotti2.dto.ProdottoNoIdDTO;
import com.its.prodotti2.dto.ReportDTO;
import com.its.prodotti2.entity.Prodotto;
import com.its.prodotti2.mapper.Mapper;

@Service
public class ServiceProdottiImpl implements ServiceProdotti {

    @Autowired
    private DAOProdotti daoProdotti;

    @Override
    public void insert(ProdottoDTO p) {
        daoProdotti.insert(Mapper.daProdottoDTOAProdotto(p));
    }

    @Override
    public void insert(ProdottoNoIdDTO p) {
        daoProdotti.insert(Mapper.daProdottoNoIdDTOAProdotto(p));
    }

    @Override
    public ProdottoDTO selectById(String id) {
        Prodotto p = daoProdotti.selectById(id);
        return (p != null) ? Mapper.daProdottoAProdottoDTO(p) : null;
    }

    @Override
    public List<ProdottoNoIdDTO> selectAll() {
        // Trasforma ogni Prodotto della lista in un ProdottoNoIdDTO
        return daoProdotti.selectAll().stream()
                .map(p -> Mapper.daProdottoAProdottoNoIdDTO(p))
                .toList();
    }

    @Override
    public ReportDTO getReport() {
        return Mapper.generaReportDaProdotti(daoProdotti.selectAll());
    }
}
