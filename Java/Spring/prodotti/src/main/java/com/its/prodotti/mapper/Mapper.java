package com.its.prodotti.mapper;

import com.its.prodotti.dto.ProdottoDTO;
import com.its.prodotti.entity.Prodotto;

public class Mapper {
    
    public static Prodotto daDtoAEntity (ProdottoDTO dto) {
        return new Prodotto(dto.getId(), dto.getDescrizione());
    }

    public static ProdottoDTO daEntityADto (Prodotto entity) {
        return new ProdottoDTO(entity.getId(), entity.getDescrizione());
    }
}
