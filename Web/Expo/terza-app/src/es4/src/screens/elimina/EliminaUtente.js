import {
  FlatList,
  StyleSheet,
  Text,
  View,
  Alert,
  TouchableOpacity,
  Pressable,
  Modal,
} from "react-native";
import React, { useState, useCallback } from "react";
import { useFocusEffect } from "@react-navigation/native";
import { FIREBASE_ENDPOINTS } from "../../../firebase/firebase";

const EliminaUtente = () => {
  const [utenti, setUtenti] = useState([]);
  const [utentiDaEliminare, setUtentiDaEliminare] = useState([]);

  const [modalVisible, setModalVisible] = useState(false);
  const [utenteSelezionato, setUtenteSelezionato] = useState(null);

  async function getUtenti() {
    try {
      let response = await fetch(FIREBASE_ENDPOINTS.utenti);
      if (!response.ok) throw new Error("Errore: " + response.status);

      let dati = await response.json();

      const arrayUtenti = Object.keys(dati).map((key) => ({
        id: key,
        ...dati[key],
      }));

      const utentiEliminabili = arrayUtenti.filter(
        (utente) => !utente.affitti || utente.affitti.length === 0,
      );

      setUtenti(utentiEliminabili);
    } catch (error) {
      console.log("Errore: " + error);
    }
  }

  useFocusEffect(
    useCallback(() => {
      getUtenti();
      setUtentiDaEliminare([]);
    }, []),
  );

  function scelteEliminazione(id) {
    if (utentiDaEliminare.includes(id)) {
      setUtentiDaEliminare(utentiDaEliminare.filter((itemId) => itemId !== id));
    } else {
      setUtentiDaEliminare([...utentiDaEliminare, id]);
    }
  }

  async function cancella() {
    if (utentiDaEliminare.length === 0) return;

    try {
      const utentiE = utentiDaEliminare.map((id) => {
        return fetch(FIREBASE_ENDPOINTS.dettaglioUtente(id), {
          method: "DELETE",
        });
      });

      await Promise.all(utentiE);

      Alert.alert("Successo", "Utenti eliminati correttamente.");

      getUtenti();
      setUtentiDaEliminare([]);
    } catch (error) {
      console.log("Errore: " + error);
      Alert.alert("Errore", "Qualcosa è andato storto durante l'eliminazione.");
    }
  }

  const chiediConferma = () => {
    Alert.alert(
      "Conferma Eliminazione",
      `Vuoi eliminare definitivamente ${utentiDaEliminare.length} Utenti?`,
      [
        { text: "Annulla", style: "cancel" },
        { text: "ELIMINA", style: "destructive", onPress: cancella },
      ],
    );
  };

  function gestisciLongPress(utente) {
    setUtenteSelezionato(utente);
    setModalVisible(true);
  }

  const selezionaTutto = () => {
    if (utentiDaEliminare.length === utenti.length) {
      // Se sono già tutti selezionati, svuota l'array
      setUtentiDaEliminare([]);
    } else {
      // Altrimenti, crea un array con tutti gli ID presenti nella lista
      const tuttiId = utenti.map((item) => item.id);
      setUtentiDaEliminare(tuttiId);
    }
  };

  return (
    <View style={styles.container}>
      <Modal
        animationType="slide"
        transparent={true}
        visible={modalVisible}
        onRequestClose={() => setModalVisible(false)}
      >
        <View style={styles.centeredView}>
          <View style={styles.modalView}>
            {utenteSelezionato && (
              <>
                <Text style={styles.modalTitle}>Dettagli Utente</Text>
                <Text style={styles.modalText}>
                  Nome: {utenteSelezionato.nome}
                </Text>
                <Text style={styles.modalText}>
                  Cognome: {utenteSelezionato.cognome}
                </Text>
                <Text style={styles.modalText}>
                  Email: {utenteSelezionato.mail}
                </Text>
              </>
            )}
            <Pressable
              style={[styles.button, styles.buttonClose]}
              onPress={() => setModalVisible(false)}
            >
              <Text style={styles.textStyle}>Chiudi</Text>
            </Pressable>
          </View>
        </View>
      </Modal>

      {utenti.length > 0 && (
        <TouchableOpacity
          style={styles.selectAllButton}
          onPress={selezionaTutto}
        >
          <Text style={styles.selectAllText}>
            {utentiDaEliminare.length === utenti.length
              ? "DESELEZIONA TUTTO"
              : "SELEZIONA TUTTO"}
          </Text>
        </TouchableOpacity>
      )}

      <FlatList
        data={utenti}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => {
          const isSelected = utentiDaEliminare.includes(item.id);

          return (
            <TouchableOpacity
              onPress={() => scelteEliminazione(item.id)}
              onLongPress={() => gestisciLongPress(item)}
              style={[styles.card, isSelected && styles.cardSelected]}
            >
              <View>
                <Text
                  style={[styles.titolo, isSelected && styles.textSelected]}
                >
                  {item.nome} {item.cognome}
                </Text>
                <Text style={isSelected && styles.textSelected}>
                  {item.mail}
                </Text>
              </View>

              {isSelected && <Text style={styles.checkMark}>✓</Text>}
            </TouchableOpacity>
          );
        }}
      />

      {utentiDaEliminare.length > 0 && (
        <View style={styles.footer}>
          <Pressable style={styles.deleteButton} onPress={chiediConferma}>
            <Text style={styles.deleteButtonText}>
              ELIMINA {utentiDaEliminare.length} ELEMENTI
            </Text>
          </Pressable>
        </View>
      )}
    </View>
  );
};

export default EliminaUtente;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f5f5f5",
  },
  centeredView: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "rgba(0,0,0,0.5)",
  },
  card: {
    padding: 20,
    backgroundColor: "white",
    borderBottomWidth: 1,
    borderBottomColor: "#eee",
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  cardSelected: {
    backgroundColor: "#ffebee",
    borderColor: "#ff4444",
  },
  titolo: {
    fontSize: 18,
    fontWeight: "bold",
  },
  textSelected: {
    color: "#d32f2f",
  },
  checkMark: {
    fontSize: 24,
    color: "#d32f2f",
    fontWeight: "bold",
  },
  footer: {
    padding: 20,
    backgroundColor: "white",
    borderTopWidth: 1,
    borderTopColor: "#ccc",
  },
  deleteButton: {
    backgroundColor: "#d32f2f",
    padding: 15,
    borderRadius: 10,
    alignItems: "center",
  },
  deleteButtonText: {
    color: "white",
    fontWeight: "bold",
    fontSize: 16,
  },
  modalView: {
    margin: 20,
    backgroundColor: "white",
    borderRadius: 20,
    padding: 35,
    alignItems: "center",
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 4,
    elevation: 5,
  },
  button: {
    borderRadius: 20,
    padding: 10,
    elevation: 2,
    marginTop: 15,
  },
  buttonClose: {
    backgroundColor: "#d32f2f",
  },
  textStyle: {
    color: "white",
    fontWeight: "bold",
    textAlign: "center",
  },
  modalText: {
    marginBottom: 15,
    textAlign: "center",
    fontSize: 16,
  },
  modalTitle: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 15,
    color: "#333",
  },
  selectAllButton: {
    padding: 10,
    backgroundColor: "white",
    alignItems: "flex-end",
    paddingRight: 20,
    borderBottomWidth: 1,
    borderBottomColor: "#eee",
  },
  selectAllText: {
    color: "#d32f2f",
    fontWeight: "bold",
    fontSize: 13,
  },
});
