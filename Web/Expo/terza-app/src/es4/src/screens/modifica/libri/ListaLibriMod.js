import {
  FlatList,
  StyleSheet,
  Text,
  View,
  TouchableOpacity,
  Pressable,
  Modal,
} from "react-native";
import React, { useState, useCallback } from "react";
import { useFocusEffect, useNavigation } from "@react-navigation/native";
import { FIREBASE_ENDPOINTS } from "../../../../firebase/firebase";

const ListaLibriMod = () => {
  const [libri, setLibri] = useState([]);
  const [libroSelezionato, setLibroSelezionato] = useState(null);
  const [modalVisible, setModalVisible] = useState(false);

  const navigation = useNavigation();

  async function getLibri() {
    try {
      let response = await fetch(FIREBASE_ENDPOINTS.libri);
      if (!response.ok) throw new Error("Errore: " + response.status);

      let dati = await response.json();

      const arrayLibri = Object.keys(dati).map((key) => ({
        id: key,
        ...dati[key],
      }));

      // Non filtriamo per "disponibile": vogliamo poter modificare TUTTI i libri
      setLibri(arrayLibri);
    } catch (error) {
      console.log("Errore: " + error);
    }
  }

  useFocusEffect(
    useCallback(() => {
      getLibri();
    }, []),
  );

  function gestisciLongPress(libro) {
    setLibroSelezionato(libro);
    setModalVisible(true);
  }

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
                <Text style={styles.modalText}>
                  Stato:{" "}
                  {libroSelezionato.disponibile ? "Disponibile" : "In Prestito"}
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

      <FlatList
        data={libri}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <TouchableOpacity
            onPress={() =>
              // Navighiamo al form di modifica passando il libro
              navigation.navigate("ModificaParametri", { libro: item })
            }
            onLongPress={() => gestisciLongPress(item)}
            style={styles.card}
          >
            <View>
              <Text style={styles.titolo}>{item.titolo}</Text>
              <Text style={styles.autore}>{item.autore}</Text>
            </View>

            {/* Indicatore visivo se cliccabile */}
            <Text style={{ color: "#ccc" }}>›</Text>
          </TouchableOpacity>
        )}
      />
    </View>
  );
};

export default ListaLibriMod;

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
  titolo: {
    fontSize: 18,
    fontWeight: "bold",
    color: "#333",
  },
  autore: {
    fontSize: 14,
    color: "#666",
    fontStyle: "italic",
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
    minWidth: 100,
  },
  buttonClose: {
    backgroundColor: "#fd7e14", // Arancione (Modifica)
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
});
