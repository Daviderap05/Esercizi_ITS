package it.its.esercizio_prova.main;

import it.its.esercizio_prova.jdbc.dao.LibroDao;
import it.its.esercizio_prova.jdbc.dto.LibroDto;

public class App {
    public static void main(String[] args) {

        LibroDao libroDao = new LibroDao();
        LibroDto l1 = new LibroDto("prova", "test", 9.9);
        boolean ok = libroDao.insert(l1);

        if (ok) {
            System.out.println("Libro inserito con id: " + l1.getId());
        } else {
            System.out.println("Libro non inserito");
        }

        LibroDao.stampaLibri();
    }
}
