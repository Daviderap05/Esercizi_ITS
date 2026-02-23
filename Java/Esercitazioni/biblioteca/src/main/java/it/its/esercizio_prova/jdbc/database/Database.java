package it.its.esercizio_prova.jdbc.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Database {
    // Se non fossero statiche, servirebbe il costruttore 
    // e visto che il metodo è statico, non è possibile usare attrib. 
    // non statici perché richiederebbero un'instanzazione che entra in 
    // conflitto con il metodo a cui non serve.

    private static final String URL = "jdbc:postgresql://localhost:5432/mavenits";
    private static final String USER = "postgres";
    private static final String PSW = "postgres";

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PSW);
    }
}
