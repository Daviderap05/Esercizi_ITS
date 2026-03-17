package com.its.universita.dao;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.its.universita.entity.Professore;
import com.its.universita.exception.RisorsaNonTrovataException;

@Repository
public class DAOProfessore {
	private final Map<String, Professore> mappa = new HashMap<>();

	public boolean insert(Professore professore) {
		if (mappa.containsKey(professore.getId()))
			throw new RisorsaNonTrovataException("Professore non trovato!");

		mappa.put(professore.getId(), professore);
		return true;
	}

	public List<Professore> selectAll() {
		return mappa.values().stream().toList();
	}

	public Professore selectById(String idProfessore) {
		Professore professore = mappa.get(idProfessore);
		
		if (professore == null)
			throw new RisorsaNonTrovataException("Professore non trovato!");	

		return professore;
	}

	public Professore delete(String idProfessore) {
		Professore professore = mappa.remove(idProfessore);

		if (professore == null)
			throw new RisorsaNonTrovataException("Professore non trovato!");
		
		return professore;
	}
}
