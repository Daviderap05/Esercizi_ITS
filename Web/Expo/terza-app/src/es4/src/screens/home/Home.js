import React, { useState, useCallback } from "react";
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  ScrollView,
  ActivityIndicator,
} from "react-native";

import { useNavigation, useFocusEffect } from "@react-navigation/native";
import { FIREBASE_ENDPOINTS } from "../../../firebase/firebase";

const Home = () => {
  const navigation = useNavigation();

  // Stati per le statistiche
  const [stats, setStats] = useState({
    totaleLibri: 0,
    disponibili: 0,
    noleggiAttivi: 0,
  });
  const [loading, setLoading] = useState(true);

  // Scaricamento dati
  async function fetchStats() {
    setLoading(true);
    try {
      const [resLibri, resNoleggi] = await Promise.all([
        fetch(FIREBASE_ENDPOINTS.libri),
        fetch(FIREBASE_ENDPOINTS.noleggi),
      ]);

      const datiLibri = (await resLibri.json()) || {};
      const datiNoleggi = (await resNoleggi.json()) || {};

      const arrayLibri = Object.values(datiLibri);
      const arrayNoleggi = Object.values(datiNoleggi);

      setStats({
        totaleLibri: arrayLibri.length,
        disponibili: arrayLibri.filter((l) => l.disponibile === true).length,
        noleggiAttivi: arrayNoleggi.filter((n) => n.stato === "attivo").length,
      });
    } catch (error) {
      console.error("Errore statistiche:", error);
    } finally {
      setLoading(false);
    }
  }

  useFocusEffect(
    useCallback(() => {
      fetchStats();
    }, []),
  );

  const DashboardButton = ({ title, screen, color }) => (
    <TouchableOpacity
      style={[styles.button, { borderColor: color }]}
      onPress={() => navigation.navigate(screen)}
    >
      <Text style={[styles.buttonText, { color: color }]}>{title}</Text>
    </TouchableOpacity>
  );

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.welcomeText}>Biblioteca Digitale</Text>
        <Text style={styles.subtitle}>Gestione Prestiti e Catalogo</Text>
      </View>

      {/* GRIGLIA PULSANTI */}
      <View style={styles.grid}>
        {/* 1. Operazioni Quotidiane (Affitti) */}
        <DashboardButton
          title="Affitta un Libro"
          screen="Affitta Libro"
          color="#007bff"
        />
        <DashboardButton
          title="Restituisci Libro"
          screen="Restituisci Libro"
          color="#28a745"
        />

        {/* 2. Inserimento Dati */}
        <DashboardButton
          title="Aggiungi Libro"
          screen="Aggiungi Libro"
          color="#17a2b8"
        />
        <DashboardButton
          title="Aggiungi Utente"
          screen="Aggiungi Utente"
          color="#6610f2"
        />

        {/* 3. Modifica (Colore Arancione per leggibilità) */}
        <DashboardButton
          title="Modifica Libro"
          screen="Modifica Libro"
          color="#fd7e14"
        />
        <DashboardButton
          title="Modifica Utente"
          screen="Modifica Utente"
          color="#fd7e14"
        />

        {/* 4. Eliminazione (Zona Pericolo - Rosso) */}
        <DashboardButton
          title="Elimina Libri"
          screen="Elimina Libro"
          color="#dc3545"
        />
        <DashboardButton
          title="Elimina Utenti"
          screen="Elimina Utente"
          color="#dc3545"
        />
      </View>

      {/* STATISTICHE */}
      <View style={styles.infoCard}>
        <Text style={styles.infoTitle}>Statistiche Rapide</Text>

        {loading ? (
          <ActivityIndicator color="#007bff" />
        ) : (
          <View style={styles.statsRow}>
            <View style={styles.statBox}>
              <Text style={styles.statNumber}>{stats.totaleLibri}</Text>
              <Text style={styles.statLabel}>Libri Totali</Text>
            </View>
            <View style={styles.statBox}>
              <Text style={[styles.statNumber, { color: "green" }]}>
                {stats.disponibili}
              </Text>
              <Text style={styles.statLabel}>Disponibili</Text>
            </View>
            <View style={styles.statBox}>
              <Text style={[styles.statNumber, { color: "orange" }]}>
                {stats.noleggiAttivi}
              </Text>
              <Text style={styles.statLabel}>In Prestito</Text>
            </View>
          </View>
        )}
      </View>
    </ScrollView>
  );
};

export default Home;

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: "#f8f9fa" },
  header: {
    padding: 30,
    backgroundColor: "white",
    alignItems: "center",
    borderBottomWidth: 1,
    borderBottomColor: "#eee",
  },
  welcomeText: { fontSize: 26, fontWeight: "bold", color: "#333" },
  subtitle: { fontSize: 14, color: "#777", marginTop: 5 },
  grid: {
    padding: 20,
    flexDirection: "row",
    flexWrap: "wrap",
    justifyContent: "space-between",
  },
  button: {
    width: "48%",
    backgroundColor: "white",
    padding: 20,
    borderRadius: 12,
    marginBottom: 15,
    alignItems: "center",
    justifyContent: "center",
    borderWidth: 2,
    elevation: 3,
  },
  buttonText: { fontWeight: "bold", textAlign: "center", fontSize: 14 },
  infoCard: {
    margin: 20,
    padding: 20,
    backgroundColor: "white",
    borderRadius: 12,
    elevation: 2,
    borderWidth: 1,
    borderColor: "#ddd",
  },
  infoTitle: {
    fontWeight: "bold",
    marginBottom: 15,
    fontSize: 16,
    textAlign: "center",
  },
  statsRow: { flexDirection: "row", justifyContent: "space-around" },
  statBox: { alignItems: "center" },
  statNumber: { fontSize: 22, fontWeight: "bold", color: "#333" },
  statLabel: { fontSize: 12, color: "#666" },
});