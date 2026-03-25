package com.factory;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class Statistiche {
    private DataExport exporter;
    private final String url = "jdbc:postgresql://localhost:5432/factory"; // Usa il nome db 'factory'
    private final String user = "postgres";
    private final String pass = "postgres";

    public void setExporter(DataExport exporter) {
        this.exporter = exporter;
    }

    @SuppressWarnings("CallToPrintStackTrace")
    public void eseguiEsportazione() {
        List<String> datiPerExport = new ArrayList<>();

        try (Connection conn = DriverManager.getConnection(url, user, pass)) {
            // 1. Leggi Categorie
            Statement stCat = conn.createStatement();
            ResultSet rsCat = stCat.executeQuery("SELECT * FROM Category");
            while (rsCat.next()) {
                datiPerExport.add("ID_Categoria:" + rsCat.getInt("idcategory"));
                datiPerExport.add("Descrizione:" + rsCat.getString("description"));
            }

            // 2. Leggi Città
            Statement stCity = conn.createStatement();
            ResultSet rsCity = stCity.executeQuery("SELECT * FROM City");
            while (rsCity.next()) {
                datiPerExport.add("Città:" + rsCity.getString("cityName"));
                datiPerExport.add("Regione:" + rsCity.getString("region"));
            }

            // Esporta nel file (il nome file dipende dal MIME) [cite: 11]
            String estensione = exporter.getMime().contains("json") ? ".json" : ".csv";
            exporter.export(datiPerExport, "export_finale" + estensione);

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}