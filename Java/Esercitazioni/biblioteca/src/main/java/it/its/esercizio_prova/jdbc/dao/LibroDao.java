package it.its.esercizio_prova.jdbc.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import it.its.esercizio_prova.jdbc.database.Database;
import it.its.esercizio_prova.jdbc.dto.LibroDto;

public class LibroDao {

    public List<LibroDto> findAll() throws SQLException {
        String sqlSelect = "Select id, titolo, autore, prezzo from libro order by id";
        List<LibroDto> libri = new ArrayList<>();

        try (Connection conn = Database.getConnection();
                PreparedStatement psSelect = conn.prepareStatement(sqlSelect)) {

            ResultSet rs = psSelect.executeQuery();
            while (rs.next()) {
                LibroDto l = new LibroDto(rs.getInt("id"), rs.getString("titolo"), rs.getString("autore"),
                        rs.getDouble("prezzo"));

                libri.add(l);
            }

        } catch (SQLException e) {
            System.out.println("Errore nell'inserimento " + e.getMessage());
        }

        return libri;
    };

    public boolean insert(LibroDto l) {

        String insertSql = "Insert into libro (titolo,autore,prezzo) values(?,?,?)";

        try (Connection conn = Database.getConnection();
                PreparedStatement psInsert = conn.prepareStatement(insertSql, Statement.RETURN_GENERATED_KEYS)) {
            psInsert.setString(1, l.getTitolo());
            psInsert.setString(2, l.getAutore());
            psInsert.setDouble(3, l.getPrezzo());

            int righe = psInsert.executeUpdate();

            if (righe == 0) {
                throw new SQLException("Non è stata inserita nessuna riga");
            }

            try (ResultSet keys = psInsert.getGeneratedKeys()) {
                if (keys.next()) {
                    int chiave = keys.getInt(1);
                    System.out.println("Id libro " + chiave);
                    l.setId(chiave);
                    return true;
                }
            }

            return false;
        } catch (SQLException e) {
            System.out.println("Errore nell'inserimento " + e.getMessage());
            return false;
        }
    }

    public static void stampaLibri() {
        try {
            List<LibroDto> libri = new LibroDao().findAll();
            System.out.println("\n\n---------------- TODO LIST ----------------");

            if (libri.isEmpty()) {
                System.out.println("Lista vuota");
            } else {
                for (LibroDto l : libri) {
                    System.out.println("Libro con id: " + l.getId() + " titolo: " + l.getTitolo() + " autore: "
                            + l.getAutore() + " prezzo: " + l.getPrezzo());
                }
            }
        } catch (SQLException e) {
            System.out.println("Errore nella stampa dei libri: " + e.getMessage());
        }
    }
}