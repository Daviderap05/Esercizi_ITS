package it.its.esercizio_prova;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

public class App {
    @SuppressWarnings("CallToPrintStackTrace")

    public static void insertLibro(Connection conn, String titolo, String autore, double prezzo) throws SQLException {
        String insertSql = "Insert into libro (titolo,autore,prezzo) values(?,?,?)";

        try (PreparedStatement psInsert = conn.prepareStatement(insertSql, Statement.RETURN_GENERATED_KEYS)) {
            psInsert.setString(1, titolo);
            psInsert.setString(2, autore);
            psInsert.setDouble(3, prezzo);

            // COMANDO DI ESECUZIONE
            int righeInserite = psInsert.executeUpdate();

            if (righeInserite == 1) {
                try (ResultSet generatedKeys = psInsert.getGeneratedKeys()) {
                    if (generatedKeys.next()) {
                        int idGenerato = generatedKeys.getInt(1);
                        System.out.println("\nLibro inserito ha ID: " + idGenerato);
                    }
                }
            }

            // System.out.println("Righe inserite: " + righeInserite);
            System.out.println("Libro inserito con successo!");
        }
    }

    public static void getLibri(Connection conn) throws SQLException {
        String selectSql = "Select id,titolo,autore,prezzo from libro";

        try (PreparedStatement psSelect = conn.prepareStatement(selectSql)) {
            ResultSet rs = psSelect.executeQuery();

            System.out.println("-----------------------------------LIBRI-----------------------------------");
            while (rs.next()) {
                int id = rs.getInt("id");
                String titolo = rs.getString("titolo");
                String autore = rs.getString("autore");
                double prezzo = rs.getDouble("prezzo");

                System.out.println(
                        "ID: " + id + ", Titolo: " + titolo + ", Autore: " + autore + ", Prezzo: " + prezzo);
            }
        }
    }

    public static void deleteLibro(Connection conn, int id) throws SQLException {
        String deleteSql = "Delete from libro where id = ?";

        try (PreparedStatement psDelete = conn.prepareStatement(deleteSql)) {
            psDelete.setInt(1, id);

            int righeCancellate = psDelete.executeUpdate();

            if (righeCancellate == 1) {
                System.out.println("Libro con ID " + id + " cancellato con successo!");
            } else {
                System.out.println("Nessun libro trovato con ID: " + id);
            }
        }
    }

    @SuppressWarnings("CallToPrintStackTrace")
    public static void main(String[] args) {
        final String URL = "jdbc:postgresql://localhost:5432/mavenits";
        final String USER = "postgres";
        final String PSW = "postgres";

        try (Scanner scanner = new Scanner(System.in)) {
            try {
                Connection conn = DriverManager.getConnection(URL, USER, PSW);

                while (true) {
                    System.out.println("\nScegli un'opzione:");

                    System.out.println("1. Inserisci un nuovo libro");
                    System.out.println("2. Visualizza tutti i libri");
                    System.out.println("3. Cancella un libro");
                    System.out.println("4. Esci");

                    int scelta;

                    try {
                        System.out.print("\nInserisci il numero dell'opzione desiderata: ");
                        scelta = scanner.nextInt();

                        scanner.nextLine();
                        System.out.print("\n");
                    } catch (Exception e) {
                        System.out.println("Input non valido. Riprova.");
                        scanner.nextLine();
                        continue;
                    }

                    switch (scelta) {
                        case 1 -> {
                            System.out.println("Inserisci un nuovo libro\n");

                            System.out.print("Inserisci il titolo: ");
                            String titolo = scanner.nextLine();

                            System.out.print("Inserisci l'autore: ");
                            String autore = scanner.nextLine();

                            System.out.print("Inserisci il prezzo: ");
                            double prezzo = scanner.nextDouble();

                            insertLibro(conn, titolo, autore, prezzo);
                        }
                        case 2 -> getLibri(conn);
                        case 3 -> {
                            getLibri(conn);

                            int id;
                            
                            try {
                                System.out.print("\nInserisci l'ID del libro da cancellare: ");
                                id = scanner.nextInt();
                            } catch (Exception e) {
                                System.out.println("Input non valido. Riprova.");
                                scanner.nextLine();
                                continue;
                            }

                            deleteLibro(conn, id);
                        }
                        case 4 -> {
                            System.out.println("Arrivederci!");
                            conn.close();
                            return;
                        }
                        default -> System.out.println("Opzione non valida. Riprova.\n");
                    }
                }

            } catch (SQLException e) {
                System.out.println("Errore JDBC: " + e.getMessage());
                e.printStackTrace();
            }
        }
    }
}
