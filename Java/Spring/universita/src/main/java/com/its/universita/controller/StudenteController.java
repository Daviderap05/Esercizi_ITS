package com.its.universita.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.its.universita.dto.studenti.CognAnnoImmLongestDTO;
import com.its.universita.dto.studenti.CognAnnoYoungestDTO;
import com.its.universita.dto.studenti.StudenteDTO;
import com.its.universita.service.StudenteService;

@RestController
@RequestMapping("/api/studenti")
public class StudenteController {

    @Autowired
    private StudenteService studenteService;

    @GetMapping("/nomi")
    public List<String> getAllNomi() {
        return studenteService.getAllNomi();
    }

    @GetMapping("/immatricolazione-storica")
    public CognAnnoImmLongestDTO getCognAnnoImmLongest() {
        return studenteService.getCognAnnoImmLongest();
    }

    @GetMapping("/piu-giovane")
    public CognAnnoYoungestDTO getCognAnnoYoungest() {
        return studenteService.getCognAnnoYoungest();
    }

    @PatchMapping("/{matricola}/indirizzo")
    public StudenteDTO modificaIndirizzo(
            @PathVariable String matricola,
            @RequestParam String nuovoIndirizzo) {
        return studenteService.modificaIndirizzo(matricola, nuovoIndirizzo);
    }
}