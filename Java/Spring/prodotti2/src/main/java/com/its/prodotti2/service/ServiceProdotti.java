package com.its.prodotti2.service;

import java.util.List;

import com.its.prodotti2.dto.ProdottoDTO;
import com.its.prodotti2.dto.ProdottoNoIdDTO;
import com.its.prodotti2.dto.ReportDTO;

public interface ServiceProdotti {
    public void insert (ProdottoDTO p);
    public void insert (ProdottoNoIdDTO p);
    public ProdottoDTO selectById (String id);
    public List<ProdottoNoIdDTO> selectAll();
    public ReportDTO getReport();
}
