package com.factory;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class JsonExporter implements DataExport {
    private static JsonExporter instance;

    private JsonExporter() {
    }

    public static synchronized JsonExporter getInstance() {
        if (instance == null)
            instance = new JsonExporter();
        return instance;
    }

    @Override
    @SuppressWarnings("CallToPrintStackTrace")
    public void export(List<String> data, String fileName) {
        StringBuilder sb = new StringBuilder("[\n  {\n"); // Inizia con un array [

        for (int i = 0; i < data.size(); i++) {
            String[] kv = data.get(i).split(":");
            sb.append("    \"").append(kv[0]).append("\": \"").append(kv[1]).append("\"");

            // Aggiunge la virgola solo se NON è l'ultimo elemento del record
            // e gestisce la creazione di un nuovo oggetto se incontriamo un nuovo ID
            if (i < data.size() - 1) {
                if (data.get(i + 1).startsWith("ID_Categoria") || data.get(i + 1).startsWith("Città")) {
                    sb.append("\n  },\n  {\n"); // Chiude il vecchio oggetto e ne apre uno nuovo
                } else {
                    sb.append(",\n"); // Semplice virgola tra proprietà dello stesso oggetto
                }
            }
        }

        sb.append("\n  }\n]"); // Chiude l'ultimo oggetto e l'array

        try (BufferedWriter bf = new BufferedWriter(new FileWriter(fileName, false))) {
            bf.write(sb.toString());
            System.out.println("JSON corretto generato con successo.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public String getMime() {
        return "application/json";
    }
}