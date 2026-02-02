import {
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
  Modal,
  Pressable,
  FlatList,
} from "react-native";
import React, { useState, useCallback } from "react";
import { FIREBASE_ENDPOINTS } from "../../../firebase/firebase";
import { useFocusEffect, useNavigation } from "@react-navigation/native";

const ListaLibriAffitto = () => {
  const navigation = useNavigation();
  const [libriDisp, setLibriDisp] = useState([]);

  const [modalVisible, setModalVisible] = useState(false);
  const [libroSelezionato, setLibroSelezionato] = useState(null);

  async function getLibriDisp() {
    try {
      let response = await fetch(FIREBASE_ENDPOINTS.libri);
      if (!response.ok) throw new Error("Errore: " + response.status);

      let dati = await response.json();

      const arrayLibri = Object.keys(dati).map((key) => ({
        id: key,
        ...dati[key],
      }));

      setLibriDisp(arrayLibri.filter((libro) => libro.disponibile === true));
    } catch (error) {
      console.error("Errore: " + error);
    }
  }

  useFocusEffect(
    useCallback(() => {
      getLibriDisp();
    }, []),
  );

  function gestisciLongPress (libro) {
    setLibroSelezionato(libro); // Salvo i dati del libro premuto
    setModalVisible(true); // Mostro la finestra
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

      <FlatList
        data={libriDisp}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <TouchableOpacity
            onPress={() =>
              navigation.navigate("SelezionaUtente", { libroId: item.id })
            }
            onLongPress={() => gestisciLongPress(item)}
            style={styles.card}
            delayLongPress={500}
          >
            <Text style={styles.titolo}>{item.titolo}</Text>
            <Text>{item.autore}</Text>
          </TouchableOpacity>
        )}
      />
    </View>
  );
};

export default ListaLibriAffitto;

// 4. STILI PER LA MODALE (Fondamentali per vederla bene)
const styles = StyleSheet.create({
  container: {
    flex: 1, // Importante per occupare tutto lo schermo
  },
  card: {
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: "#ccc",
    backgroundColor: "white",
  },
  titolo: {
    fontSize: 18,
    fontWeight: "bold",
  },
  // Stili Modale
  centeredView: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    marginTop: 22,
    backgroundColor: "rgba(0,0,0,0.5)", // Sfondo semitrasparente scuro
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
    backgroundColor: "#2196F3",
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
