package com.its.prodotti.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.its.prodotti.dto.ErroreDTO;
import com.its.prodotti.dto.ProdottoDTO;
import com.its.prodotti.service.ProdottoService;

@RestController
@RequestMapping(path = "/prodotti")
public class ProdottoController {
    
    @Autowired
    private ProdottoService service;

    @PostMapping(path = "/carica", consumes = "application/json")
    public void carica(@RequestBody ProdottoDTO dto) {
        service.carica(dto);
    }

    @GetMapping(path = "/cerca/{id}", produces = "application/json")
    public ProdottoDTO cercaPerId(@PathVariable int id) {
        return service.cercaPerId(id);
    }

    // Gestione degli errori
    @ExceptionHandler
    public ResponseEntity<ErroreDTO> gestoreErrori (RuntimeException ex) {
        return ResponseEntity.status(500).body(new ErroreDTO(ex.getMessage()));
    } 
}
