package com.its.universita.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.its.universita.dto.professori.ProfessoreDTO;
import com.its.universita.service.ProfessoreService;

@RestController
@RequestMapping("/api/professori")
public class ProfessoreController {

    @Autowired
    private ProfessoreService professoreService;

    @GetMapping("/materia/{materia}")
    public List<ProfessoreDTO> getAllProfMateria(@PathVariable String materia) {
        return professoreService.getAllProfMateria(materia);
    }

    @GetMapping("/ordinati")
    public List<ProfessoreDTO> getAllProfSortByCogn() {
        return professoreService.getAllProfSortByCogn();
    }

    @GetMapping("/materie")
    public List<String> getAllMaterie() {
        return professoreService.getAllMaterie();
    }
}