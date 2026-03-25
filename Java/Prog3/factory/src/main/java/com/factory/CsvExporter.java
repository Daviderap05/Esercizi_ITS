package com.factory;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class CsvExporter implements DataExport {
    private static CsvExporter instance;

    private CsvExporter() {
    }

    public static synchronized CsvExporter getInstance() {
        if (instance == null)
            instance = new CsvExporter();
        return instance;
    }

    @Override
    @SuppressWarnings("CallToPrintStackTrace")
    public void export(List<String> data, String fileName) {
        String testo = String.join(",", data) + "\n";
        try (BufferedWriter bf = new BufferedWriter(new FileWriter(fileName, true))) {
            bf.write(testo);
            System.out.println("CSV creato con successo.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public String getMime() {
        return "text/csv";
    }
}