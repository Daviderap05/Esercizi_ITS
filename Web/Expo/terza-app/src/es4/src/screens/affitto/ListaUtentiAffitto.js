import {
  StyleSheet,
  Text,
  Alert,
  Modal,
  View,
  Pressable,
  TouchableOpacity,
  FlatList,
} from "react-native";

import React, {
  useState,
  useCallback,
  useEffect,
} from "react";

import {
  useRoute,
  useFocusEffect,
  useNavigation,
  useIsFocused,
} from "@react-navigation/native";

import { FIREBASE_ENDPOINTS } from "../../../firebase/firebase";

const ListaUtentiAffitto = () => {
  const navigation = useNavigation();
  const route = useRoute();
  const { libroId } = route.params;

  const [utenti, setUtenti] = useState([]);

  const [modalVisible, setModalVisible] = useState(false);
  const [utenteSelezionato, setUtenteSelezionato] = useState(null);

  const isFocused = useIsFocused();

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

  async function eseguiSalvataggio(utente) {
    try {
      const oggi = new Date();

      // 1. Richiesta Noleggio
      const reqNoleggio = fetch(FIREBASE_ENDPOINTS.noleggi, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          libroId: libroId,
          utenteId: utente.id,
          dataInizio: oggi.toLocaleDateString("it-IT"),
          dataFine: null,
          stato: "attivo",
        }),
      });

      // 2. Richiesta Libro
      const reqLibro = fetch(FIREBASE_ENDPOINTS.dettaglioLibro(libroId), {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ disponibile: false }),
      });

      // 3. Richiesta Utente
      const affittiPrecedenti = utente.affitti || [];
      const nuoviAffitti = [...affittiPrecedenti, libroId];

      const reqUtente = fetch(FIREBASE_ENDPOINTS.dettaglioUtente(utente.id), {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ affitti: nuoviAffitti }),
      });

      const [resAffitto, resLibro, resUtente] = await Promise.all([
        reqNoleggio,
        reqLibro,
        reqUtente,
      ]);

      if (!resAffitto.ok) throw new Error("Errore noleggi");
      if (!resLibro.ok) throw new Error("Errore libro");
      if (!resUtente.ok) throw new Error("Errore utente");

      Alert.alert("Successo", "Affitto completato");
      navigation.popToTop();
    } catch (error) {
      console.error("Errore: " + error);
      Alert.alert("Errore", "Operazione fallita.");
    }
  }

  const chiediConferma = (utente) => {
    Alert.alert(
      "Conferma Affitto",
      `Vuoi assegnare questo libro a ${utente.nome}?`,
      [
        { text: "Annulla", style: "cancel" },
        { text: "Conferma", onPress: () => eseguiSalvataggio(utente) },
      ],
    );
  };

  useEffect(() => {
    if (!isFocused) {
      navigation.popToTop();
    }
  }, [isFocused]);

  return (
    <View style={styles.container}>
      {/* 4. Il blocco della Modale */}
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
            onPress={() => chiediConferma(item)}
            onLongPress={() => gestisciLongPress(item)}
            delayLongPress={500}
            style={styles.card}
            activeOpacity={0.7}
          >
            <Text style={styles.titolo}>
              {item.nome} {item.cognome}
            </Text>
            <Text>{item.mail}</Text>
          </TouchableOpacity>
        )}
      />
    </View>
  );
};

export default ListaUtentiAffitto;

const styles = StyleSheet.create({
  container: { flex: 1 },
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
