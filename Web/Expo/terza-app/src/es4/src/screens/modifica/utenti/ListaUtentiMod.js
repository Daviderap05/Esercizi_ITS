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

const ListaUtentiMod = () => {
  const [utenti, setUtenti] = useState([]);
  const [utenteSelezionato, setUtenteSelezionato] = useState(null);
  const [modalVisible, setModalVisible] = useState(false);

  const navigation = useNavigation(); // Fondamentale per navigare

  async function getUtenti() {
    try {
      let response = await fetch(FIREBASE_ENDPOINTS.utenti);
      if (!response.ok) throw new Error("Errore: " + response.status);

      let dati = await response.json();

      const arrayUtenti = Object.keys(dati).map((key) => ({
        id: key,
        ...dati[key],
      }));

      setUtenti(arrayUtenti);
    } catch (error) {
      console.log("Errore: " + error);
    }
  }

  useFocusEffect(
    useCallback(() => {
      getUtenti();
    }, []),
  );

  function gestisciLongPress(utente) {
    setUtenteSelezionato(utente);
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

      <FlatList
        data={utenti}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <TouchableOpacity
            onPress={() =>
              navigation.navigate("ModificaParametri", { utente: item })
            }
            onLongPress={() => gestisciLongPress(item)}
            style={styles.card}
          >
            <View>
              <Text style={styles.titolo}>
                {item.nome} {item.cognome}
              </Text>
              <Text style={styles.sottotitolo}>{item.mail}</Text>
            </View>

                <Text style={{ color: "#ccc" }}>›</Text>
          </TouchableOpacity>
        )}
      />
    </View>
  );
};

export default ListaUtentiMod;

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
  sottotitolo: {
    color: "#666",
    fontSize: 14,
  },
  modalView: {
    margin: 20,
    backgroundColor: "white",
    borderRadius: 20,
    padding: 35,
    alignItems: "center",
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
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
    backgroundColor: "#fd7e14",
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
