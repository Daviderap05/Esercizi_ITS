package com.its.universita.dao;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Repository;

import com.its.universita.entity.Studente;
import com.its.universita.exception.RisorsaNonTrovataException;

@Repository
public class DAOStudente {

	private final Map<String, Studente> mappa = new HashMap<>();

	public boolean insert(Studente studente) {
		if (mappa.containsKey(studente.getMatricola()))
			throw new RisorsaNonTrovataException("Studente non trovato!");

		mappa.put(studente.getMatricola(), studente);
		return true;
	}

	public List<Studente> selectAll() {
		return mappa.values().stream().toList();
	}

	public Studente selectById(String idStudente) {
		Studente stu = mappa.get(idStudente);

		if (stu == null)
			throw new RisorsaNonTrovataException("Studente non trovato!");
		return stu;
	}

	public Studente delete(String idStudente) {
		Studente stu = mappa.get(idStudente);

		if (stu == null)
			throw new RisorsaNonTrovataException("Studente non trovato!");
		mappa.remove(idStudente);
		return stu;
	}
}
