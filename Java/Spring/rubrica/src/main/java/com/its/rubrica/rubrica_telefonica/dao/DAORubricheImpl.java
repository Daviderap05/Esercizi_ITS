package com.its.rubrica.rubrica_telefonica.dao;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.springframework.stereotype.Repository;

import com.its.rubrica.rubrica_telefonica.entity.Contatto;
import com.its.rubrica.rubrica_telefonica.entity.Rubrica;

@Repository
public class DAORubricheImpl implements DAORubriche {

    private final Map<String, Rubrica> rubriche = new HashMap<>();

    @Override
    public void delete(String id) {
        if (!rubriche.containsKey(id))
            throw new RuntimeException("Rubrica non trovata con ID: " + id);

        rubriche.remove(id);
    }

    @Override
    public void deleteCont(String idRubrica, String idContatto) {
        Rubrica rubrica = rubriche.get(idRubrica);

        if (rubrica == null)
            throw new RuntimeException("Rubrica non trovata con ID: " + idRubrica);

        Set<Contatto> contatti = rubrica.getContatti();

        Contatto daCancellare = contatti.stream()
                .filter(c -> c.getId().equals(idContatto))
                .findFirst()
                .orElseThrow(() -> new RuntimeException("Contatto non trovato"));

        contatti.remove(daCancellare);
    }

    @Override
    public void insert(Rubrica rubrica) {
        if (rubriche.containsKey(rubrica.getId()))
            throw new RuntimeException("Attenzione: una rubrica con questo ID esiste già!");

        rubriche.put(rubrica.getId(), rubrica);
    }

    @Override
    public void insertContact(String idRubrica, Contatto contatto) {
        Rubrica rubrica = rubriche.get(idRubrica);

        if (rubrica == null)
            throw new RuntimeException("Rubrica non trovata con ID: " + idRubrica);

        boolean inserito = rubrica.getContatti().add(contatto);

        if (!inserito)
            throw new RuntimeException("Contatto già esistente in questa rubrica");

    }

    @Override
    public List<Contatto> selectAllCont(String idRubrica) {
        Rubrica rubrica = rubriche.get(idRubrica);

        if (rubrica == null)
            throw new RuntimeException("Rubrica non trovata con ID: " + idRubrica);

        return rubrica.getContatti().stream().toList();
    }

    @Override
    public List<Rubrica> selectAllRubr() {
        return rubriche.values().stream().toList();
    }

    @Override
    public Contatto selectContById(String idRubrica, String idContatto) {
        Rubrica rubrica = rubriche.get(idRubrica);

        if (rubrica == null)
            throw new RuntimeException("Rubrica non trovata con ID: " + idRubrica);

        return rubrica.getContatti().stream()
                .filter(c -> c.getId().equals(idContatto))
                .findFirst()
                .orElseThrow(() -> new RuntimeException("Contatto non trovato"));
    }

    @Override
    public Rubrica selectRubrById(String id) {
        Rubrica rubrica = rubriche.get(id);

        if (rubrica == null)
            throw new RuntimeException("Rubrica non trovata con ID: " + id);

        return rubrica;
    }

    @Override
    public Contatto updateContact(String idRubrica, String idContatto, Contatto nuoviDati) {
        Rubrica rubrica = rubriche.get(idRubrica);

        if (rubrica == null)
            throw new RuntimeException("Rubrica non trovata con ID: " + idRubrica);

        Set<Contatto> contatti = rubrica.getContatti();

        Contatto contatto = contatti.stream()
                .filter(c -> c.getId().equals(idContatto))
                .findFirst()
                .orElseThrow(() -> new RuntimeException("Contatto non trovato"));

        contatti.remove(contatto);

        contatto.setNome(nuoviDati.getNome());
        contatto.setCognome(nuoviDati.getCognome());
        contatto.setNumero(nuoviDati.getNumero());
        contatto.setGruppo(nuoviDati.getGruppo());
        contatto.setAnnoNascita(nuoviDati.getAnnoNascita());
        contatto.setPreferito(nuoviDati.isPreferito());

        // Verifichiamo se i nuovi dati creano un duplicato
        boolean aggiunto = contatti.add(contatto);

        if (!aggiunto)
            throw new RuntimeException("Errore: esiste già un contatto con lo stesso nome e cognome in questa rubrica");

        return contatto;
    }
}
