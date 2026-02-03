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

import React, { useState, useCallback, useEffect } from "react";
import {
  useRoute,
  useFocusEffect,
  useNavigation,
  useIsFocused,
} from "@react-navigation/native";
import { FIREBASE_ENDPOINTS } from "../../../firebase/firebase";

const DettaglioRestituzione = () => {
  const navigation = useNavigation();
  const route = useRoute();
  const { utente } = route.params;

  const [libri, setLibri] = useState([]);

  const [modalVisible, setModalVisible] = useState(false);
  const [libroSelezionato, setLibroSelezionato] = useState(null);

  const isFocused = useIsFocused();

  async function getLibri() {
    try {
      let resUtente = await fetch(
        FIREBASE_ENDPOINTS.dettaglioUtente(utente.id),
      );

      if (!resUtente.ok) throw new Error("Errore utente");

      let datiUtenteAggiornati = await resUtente.json();
      const affittiReali = datiUtenteAggiornati.affitti || [];

      let response = await fetch(FIREBASE_ENDPOINTS.libri);
      if (!response.ok) throw new Error("Errore libri");

      let datiLibri = await response.json();

      const arrayLibri = Object.keys(datiLibri).map((key) => ({
        id: key,
        ...datiLibri[key],
      }));

      const libriFiltrati = arrayLibri.filter((libro) =>
        affittiReali.includes(libro.id),
      );

      setLibri(libriFiltrati);

      if (libriFiltrati.length === 0) {
        Alert.alert("Info", "Nessun libro da restituire.");
        navigation.goBack();
      }
    } catch (error) {
      console.error("Errore: " + error);
    }
  }

  useFocusEffect(
    useCallback(() => {
      getLibri();
    }, []),
  );

  function gestisciLongPress(libro) {
    setLibroSelezionato(libro); // Salva i dati
    setModalVisible(true); // Apre la modale
  }

  async function eseguiRestituzione(libroId) {
    try {
      const oggi = new Date();

      const affittiPrecedenti = utente.affitti || [];
      const nuoviAffitti = affittiPrecedenti.filter((id) => id !== libroId);

      const promiseLibro = fetch(FIREBASE_ENDPOINTS.dettaglioLibro(libroId), {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ disponibile: true }),
      });

      const promiseUtente = fetch(
        FIREBASE_ENDPOINTS.dettaglioUtente(utente.id),
        {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ affitti: nuoviAffitti }),
        },
      );

      const promiseListaNoleggi = fetch(FIREBASE_ENDPOINTS.noleggi);

      const [resLibro, resUtente, resListaNoleggi] = await Promise.all([
        promiseLibro,
        promiseUtente,
        promiseListaNoleggi,
      ]);

      if (!resLibro.ok) throw new Error("Errore libro");
      if (!resUtente.ok) throw new Error("Errore utente");
      if (!resListaNoleggi.ok) throw new Error("Errore scaricamento noleggi");

      const datiNoleggi = await resListaNoleggi.json();
      let idNoleggioDaChiudere = null;

      if (datiNoleggi) {
        Object.keys(datiNoleggi).forEach((key) => {
          const n = datiNoleggi[key];

          if (n.libroId === libroId && n.stato === "attivo") {
            idNoleggioDaChiudere = key;
          }
        });
      }

      if (idNoleggioDaChiudere) {
        let resChiudi = await fetch(
          FIREBASE_ENDPOINTS.dettaglioNoleggi(idNoleggioDaChiudere),
          {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              dataFine: oggi.toLocaleDateString("it-IT"),
              stato: "terminato",
            }),
          },
        );

        if (!resChiudi.ok) throw new Error("Errore chiusura noleggio");
      }

      Alert.alert("Successo", "Restituzione completata");
      navigation.popToTop();

    } catch (error) {
      console.error("Errore: " + error);
      Alert.alert("Errore", "Operazione fallita.");
    }
  }

  const chiediConferma = (libro) => {
    Alert.alert("Conferma Restituzione", `Vuoi restituire: ${libro.titolo}?`, [
      { text: "Annulla", style: "cancel" },
      { text: "Conferma", onPress: () => eseguiRestituzione(libro.id) },
    ]);
  };

  useEffect(() => {
    if (!isFocused) {
      navigation.popToTop();
    }
  }, [isFocused]);

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
        data={libri}
        keyExtractor={(item) => item.id}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={styles.card}
            onPress={() => chiediConferma(item)}
            onLongPress={() => gestisciLongPress(item)}
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

export default DettaglioRestituzione;

const styles = StyleSheet.create({
  container: {
    flex: 1, // Occupa tutto lo schermo
    backgroundColor: "#f5f5f5",
  },
  card: {
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: "#ccc",
    backgroundColor: "white", // Stesso stile delle altre liste
  },
  titolo: {
    fontSize: 18,
    fontWeight: "bold", // Mette in risalto il titolo del libro
  },
  centeredView: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "rgba(0,0,0,0.5)", // Sfondo scuro semitrasparente
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
  },
  modalTitle: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 15,
  },
});
