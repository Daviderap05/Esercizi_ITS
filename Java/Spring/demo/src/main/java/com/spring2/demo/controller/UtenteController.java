package com.spring2.demo.controller;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring2.demo.dto.UtenteDTO;
import com.spring2.demo.service.UtenteService;

@RestController
@RequestMapping(path = "/utenti")
public class UtenteController {

    private final UtenteService service = new UtenteService();

    @GetMapping(path = "/registra", consumes = "application/json")
    public boolean registra(@RequestBody UtenteDTO utente) {
        return service.registra(utente);
    }

    @GetMapping(path = "/cerca/{idUtente}", produces = "application/json")
    public UtenteDTO cercaPerId(@PathVariable int idUtente) {
        return service.cercaPerId(idUtente);
    }

    @GetMapping(path = "/cercaTutti", produces = "application/json")
    public List<UtenteDTO> cercaTutti() {
        return service.selectAll();
    }

    @DeleteMapping(path = "/cancella/{idUtente}", produces = "application/json")
    public UtenteDTO cancellaUtente(@PathVariable int idUtente) {
        UtenteDTO utenteCancellato = service.cancella(idUtente);
        return utenteCancellato;
    }

    @PatchMapping(path = "/aggiorna/{idUtente}", produces = "application/json")
    public UtenteDTO aggiornaUtente(@PathVariable int idUtente, String email) {
        return service.aggiorna(idUtente, email);
    }

    @GetMapping(path = "/cercaTuttiPerNome", produces = "application/json")
    public List<UtenteDTO> cercaTuttiPerNome() {
        return service.ordinaPerNome();
    }

    @GetMapping(path = "/visualizzaNomi", produces = "application/json")
    public List<String> visualizzaNomi() {
        return service.visualizzaNomi();
    }
}
