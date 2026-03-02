package com.spring2.demo.controller;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.spring2.demo.entity.Utente;
import com.spring2.demo.service.UtenteService;

@RestController
@RequestMapping(path = "/utenti")
public class UtenteController {

    private final UtenteService service = new UtenteService();

    @GetMapping(path = "/registra", consumes = "application/json")
    public boolean registra(@RequestBody Utente utente) {
        System.out.println("Ho registrato l'utente: " + utente.getNome());
        return service.registra(utente);
    }

    @GetMapping(path = "/cerca/{idUtente}", produces = "application/json")
    public Utente cercaPerId(@PathVariable int idUtente) {
        return new Utente(idUtente, "Mario", "Rossi", "mail", "333222222");
    }

    @GetMapping(path = "/cercaTutti", produces = "application/json")
    public List<Utente> cercaTutti() {
        return service.selectAll();
    }

    @DeleteMapping(path = "/cancella/{idUtente}", produces = "application/json")
    public Utente cancellaUtente(@PathVariable int idUtente) {
        Utente utenteCancellato = service.cancella(idUtente);
        return utenteCancellato;
    }

    @PatchMapping(path = "/aggiorna/{idUtente}", produces = "application/json")
    public Utente aggiornaUtente(@PathVariable int idUtente, String email) {
        return service.aggiorna(idUtente, email);
    }

}
