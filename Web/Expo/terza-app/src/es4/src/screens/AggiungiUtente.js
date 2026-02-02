import {
  StyleSheet,
  Text,
  View,
  Pressable,
  Alert,
  TextInput,
} from "react-native";
import React, { useState } from "react";
import { FIREBASE_ENDPOINTS } from "../../firebase/firebase";

const AggiungiUtente = () => {
  const [nome, setNome] = useState("");
  const [cognome, setCognome] = useState("");
  const [mail, setMail] = useState("");

  async function gestisciSalvataggio() {
    if (!nome || !cognome || !mail) {
      Alert.alert("Errore", "Compilare tutti i campi.");
      return;
    }

    const nuovoUtente = {
      nome: nome,
      cognome: cognome,
      mail: mail,
      affitti: [],
    };

    try {
      const response = await fetch(FIREBASE_ENDPOINTS.utenti, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(nuovoUtente),
      });

      if (response.ok) {
        Alert.alert("Successo", "Utente aggiunto correttamente!");
        setNome("");
        setCognome("");
        setMail("");
      } else {
        throw new Error("Risposta del server non valida");
      }
    } catch (error) {
      Alert.alert("Errore", "Impossibile salvare l'utente.");
      console.error(error);
    }
  }

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Nome"
        value={nome}
        onChangeText={(text) => setNome(text)}
      ></TextInput>

      <TextInput
        style={styles.input}
        placeholder="Cognome"
        value={cognome}
        onChangeText={(text) => setCognome(text)}
      ></TextInput>

      <TextInput
        style={styles.input}
        placeholder="Email"
        value={mail}
        onChangeText={(text) => setMail(text)}
      ></TextInput>

      <Pressable style={styles.button} onPress={gestisciSalvataggio}>
        <Text style={styles.buttonText}>AGGIUNGI UTENTE</Text>
      </Pressable>
    </View>
  );
};

export default AggiungiUtente;

const styles = StyleSheet.create({
  container: { padding: 20, marginTop: 50 },
  input: {
    height: 50,
    borderColor: "#ccc",
    borderWidth: 1,
    marginBottom: 15,
    paddingHorizontal: 10,
    borderRadius: 8,
  },
  button: {
    backgroundColor: "#007bff",
    padding: 15,
    borderRadius: 8,
    alignItems: "center",
  },
  buttonText: { color: "white", fontWeight: "bold" },
});
