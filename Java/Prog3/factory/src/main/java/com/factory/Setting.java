package com.factory;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Setting {
    @SuppressWarnings("CallToPrintStackTrace")
    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5432/factory";
        Map<Integer, String> opzioni = new HashMap<>();

        try (Connection conn = DriverManager.getConnection(url, "postgres", "postgres")) {
            System.out.println("Seleziona il formato di esportazione:");
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM ExportType");

            while (rs.next()) {
                int id = rs.getInt("id");
                String format = rs.getString("format_name");
                String path = rs.getString("class_path");
                opzioni.put(id, path);
                System.out.println(id + ") " + format);
            }

            try (Scanner sc = new Scanner(System.in)) {
                int scelta = sc.nextInt();

                if (opzioni.containsKey(scelta)) {
                    // Ottieni l'exporter tramite la Factory (Reflection + Singleton) [cite: 14, 15]
                    DataExport exporter = FactoryDataExport.getExporter(opzioni.get(scelta));

                    Statistiche stats = new Statistiche();
                    stats.setExporter(exporter);
                    stats.eseguiEsportazione();

                    System.out.println("Operazione completata con successo!");
                } else {
                    System.out.println("Scelta non valida.");
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}