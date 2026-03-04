package com.its.universita.dao;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.its.universita.entity.Professore;

public class DAOProfessoreMappa {
    private final Map<String, Professore> mappa = new HashMap<>();

	public boolean insert(Professore professore) {
		if(mappa.containsKey(professore.getId()))
			return false;
		
		mappa.put(professore.getId(), professore);
		return true;

	}
	public List<Professore> selectAll(){
		return new ArrayList<>(mappa.values());
	}

	public Professore selectById(String idProfessore) {
		return mappa.get(idProfessore);
	}
	
	public Professore delete(String idProfessore) {
		Professore professore = mappa.remove(idProfessore);
		return professore;
	}
}
