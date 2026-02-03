import {
  StyleSheet,
  Text,
  Modal,
  View,
  Pressable,
  TouchableOpacity,
  FlatList,
} from "react-native";

import React, { useState, useCallback } from "react";
import { useFocusEffect, useNavigation } from "@react-navigation/native";
import { FIREBASE_ENDPOINTS } from "../../../firebase/firebase";

const ListaNoleggiAttivi = () => {
  const navigation = useNavigation();

  const [utenti, setUtenti] = useState([]);

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

      const filtrati = arrayUtenti.filter(
        (utente) => utente.affitti && utente.affitti.length > 0,
      );

      setUtenti(filtrati);
    } catch (error) {
      console.error("Errore: " + error);
    }
  }

  useFocusEffect(
    useCallback(() => {
      getUtenti();
    }, []),
  );

  function gestisciLongPress(utente) {
    setUtenteSelezionato(utente); // Salva i dati
    setModalVisible(true); // Apre la modale
  }

  return (
    <View style={styles.container}>
      {/* Il blocco della Modale */}
      <Modal
        animationType="fade"
        transparent={true}
        visible={modalVisible}
        onRequestClose={() => setModalVisible(false)}
      >
        <View style={styles.centeredView}>
          <View style={styles.modalView}>
            {utenteSelezionato && (
              <>
                <Text style={styles.modalTitle}>Info Utente</Text>
                <Text style={styles.modalText}>
                  Nome: {utenteSelezionato.nome}
                </Text>
                <Text style={styles.modalText}>
                  Cognome: {utenteSelezionato.cognome}
                </Text>
                <Text style={styles.modalText}>
                  Email: {utenteSelezionato.mail}
                </Text>
                <Text style={styles.modalText}>
                  Libri in possesso:{" "}
                  {utenteSelezionato.affitti
                    ? utenteSelezionato.affitti.length
                    : 0}
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
              navigation.navigate("SelezionaLibro", { utente: item })
            }
            onLongPress={() => gestisciLongPress(item)}
            delayLongPress={500}
            style={styles.card}
            activeOpacity={0.7}
          >
            <View>
              <Text style={styles.titolo}>
                {item.nome} {item.cognome}
              </Text>

              <Text>{item.mail}</Text>
            </View>

            <Text style={{ color: "#ccc" }}>›</Text>
          </TouchableOpacity>
        )}
      />
    </View>
  );
};

export default ListaNoleggiAttivi;

const styles = StyleSheet.create({
  container: { flex: 1 },
  card: {
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: "#ccc",
    backgroundColor: "white",
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  titolo: {
    fontSize: 18,
    fontWeight: "bold",
  },
  // Stili per la Modale
  centeredView: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "rgba(0,0,0,0.5)",
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
    backgroundColor: "#2196F3",
  },
  textStyle: {
    color: "white",
    fontWeight: "bold",
    textAlign: "center",
  },
  modalText: {
    marginBottom: 10,
    textAlign: "center",
    fontSize: 16,
  },
  modalTitle: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 15,
  },
});
