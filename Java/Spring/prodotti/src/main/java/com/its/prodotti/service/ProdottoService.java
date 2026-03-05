package com.its.prodotti.service;

import com.its.prodotti.dto.ProdottoDTO;

public interface ProdottoService {
    public void carica (ProdottoDTO dto);
    public ProdottoDTO cercaPerId (int id);
}
