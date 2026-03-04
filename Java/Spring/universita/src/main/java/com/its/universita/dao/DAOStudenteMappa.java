package com.its.universita.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.its.universita.entity.Studente;

public class DAOStudenteMappa {
    private final Map<String, Studente> mappa = new HashMap<>();

	public boolean insert(Studente studente) {
		if(mappa.containsKey(studente.getMatricola()))
			return false;
		
		mappa.put(studente.getMatricola(), studente);
		return true;

	}
	public List<Studente> selectAll(){
		return new ArrayList<>(mappa.values());
	}

	public Studente selectById(String idStudente) {
		return mappa.get(idStudente);
	}
	
	public Studente delete(String idStudente) {
		Studente studente = mappa.remove(idStudente);
		return studente;
	}
}
