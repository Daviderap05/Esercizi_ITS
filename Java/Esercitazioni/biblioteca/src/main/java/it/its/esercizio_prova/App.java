package it.its.esercizio_prova;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class App {
    @SuppressWarnings("CallToPrintStackTrace")
    public static void main(String[] args) {
        final String URL = "jdbc:postgresql://localhost:5432/mavenits";
        final String USER = "postgres";
        final String PSW = "postgres";

        try {
            Connection conn = DriverManager.getConnection(URL, USER, PSW);
            String insertSql = "Insert into libro (titolo,autore,prezzo) values(?,?,?)";

            try (PreparedStatement psInsert = conn.prepareStatement(insertSql)) {
                psInsert.setString(1, "La bibbia");
                psInsert.setString(2, "Sconosciuto");
                psInsert.setDouble(3, 40.00);

                // COMANDO DI ESECUZIONE
                int righeInserite = psInsert.executeUpdate();
                System.out.println("Inserimento completato. Righe aggiunte: " + righeInserite);
            }

            // FACCIAMO LA SELECT
            String selectSql = "Select id,titolo,autore,prezzo from libro";

            try (PreparedStatement psSelect = conn.prepareStatement(selectSql)) {
                ResultSet rs = psSelect.executeQuery();

                while (rs.next()) {
                    int id = rs.getInt("id");
                    String titolo = rs.getString("titolo");
                    String autore = rs.getString("autore");
                    double prezzo = rs.getDouble("prezzo");

                    System.out.println(
                            "ID: " + id + ", Titolo: " + titolo + ", Autore: " + autore + ", Prezzo: " + prezzo);
                }
            }

        } catch (SQLException e) {
            System.out.println("Errore JDBC: " + e.getMessage());
            e.printStackTrace();
        }
    }
}