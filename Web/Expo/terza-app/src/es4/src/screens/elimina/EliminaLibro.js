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

const EliminaLibro = () => {
  const [libri, setLibri] = useState([]);
  const [libriDaEliminare, setlibriDaEliminare] = useState([]);

  const [modalVisible, setModalVisible] = useState(false);
  const [libroSelezionato, setLibroSelezionato] = useState(null);

  async function getLibri() {
    try {
      let response = await fetch(FIREBASE_ENDPOINTS.libri);
      if (!response.ok) throw new Error("Errore: " + response.status);

      let dati = await response.json();

      const arrayLibri = Object.keys(dati).map((key) => ({
        id: key,
        ...dati[key],
      }));

      const arrayLibriFiltrato = arrayLibri.filter(
        (libro) => libro.disponibile === true,
      );
      setLibri(arrayLibriFiltrato);
    } catch (error) {
      console.log("Errore: " + error);
    }
  }

  useFocusEffect(
    useCallback(() => {
      getLibri();
      setlibriDaEliminare([]);
    }, []),
  );

  function scelteEliminazione(id) {
    if (libriDaEliminare.includes(id)) {
      setlibriDaEliminare(libriDaEliminare.filter((itemId) => itemId !== id));
    } else {
      setlibriDaEliminare([...libriDaEliminare, id]);
    }
  }

  async function cancella() {
    if (libriDaEliminare.length === 0) return;

    try {
      const libriE = libriDaEliminare.map((id) => {
        return fetch(FIREBASE_ENDPOINTS.dettaglioLibro(id), {
          method: "DELETE",
        });
      });

      await Promise.all(libriE);

      Alert.alert("Successo", "Libri eliminati correttamente.");

      getLibri();
      setlibriDaEliminare([]);
    } catch (error) {
      console.log("Errore: " + error);
      Alert.alert("Errore", "Qualcosa è andato storto durante l'eliminazione.");
    }
  }

  const chiediConferma = () => {
    Alert.alert(
      "Conferma Eliminazione",
      `Vuoi eliminare definitivamente ${libriDaEliminare.length} libri?`,
      [
        { text: "Annulla", style: "cancel" },
        { text: "ELIMINA", style: "destructive", onPress: cancella },
      ],
    );
  };

  function gestisciLongPress(libro) {
    setLibroSelezionato(libro); // Salvo i dati del libro premuto
    setModalVisible(true); // Mostro la finestra
  }

  const selezionaTutto = () => {
    if (libriDaEliminare.length === libri.length) {
      // Se sono già tutti selezionati, svuota l'array
      setlibriDaEliminare([]);
    } else {
      // Altrimenti, crea un array con tutti gli ID presenti nella lista
      const tuttiId = libri.map((item) => item.id);
      setlibriDaEliminare(tuttiId);
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
            {libroSelezionato && (
              <>
                <Text style={styles.modalTitle}>Dettagli Libro</Text>
                <Text style={styles.modalText}>
                  Titolo: {libroSelezionato.titolo}
                </Text>
                <Text style={styles.modalText}>
                  Autore: {libroSelezionato.autore}
                </Text>
                <Text style={styles.modalText}>
                  Categoria: {libroSelezionato.categoria}
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

      {libri.length > 0 && (
        <TouchableOpacity
          style={styles.selectAllButton}
          onPress={selezionaTutto}
        >
          <Text style={styles.selectAllText}>
            {libriDaEliminare.length === libri.length
              ? "DESELEZIONA TUTTO"
              : "SELEZIONA TUTTO"}
          </Text>
        </TouchableOpacity>
      )}

      <FlatList
        data={libri}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => {
          const isSelected = libriDaEliminare.includes(item.id);

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
                  {item.titolo}
                </Text>
                <Text style={isSelected && styles.textSelected}>
                  {item.autore}
                </Text>
              </View>

              {isSelected && <Text style={styles.checkMark}>✓</Text>}
            </TouchableOpacity>
          );
        }}
      />

      {libriDaEliminare.length > 0 && (
        <View style={styles.footer}>
          <Pressable style={styles.deleteButton} onPress={chiediConferma}>
            <Text style={styles.deleteButtonText}>
              ELIMINA {libriDaEliminare.length} ELEMENTI
            </Text>
          </Pressable>
        </View>
      )}
    </View>
  );
};

export default EliminaLibro;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f5f5f5",
  },
  centeredView: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "rgba(0,0,0,0.5)", // Sfondo scuro semitrasparente
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
  // Stile speciale quando selezionato
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
  // Footer col bottone
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
    backgroundColor: "#d32f2f", // Rosso eliminazione
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
