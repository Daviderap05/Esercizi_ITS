import { StyleSheet, Text, View, Pressable, Alert } from "react-native";
import React, { useState } from "react";
import { TextInput } from "react-native-gesture-handler";
import { FIREBASE_ENDPOINTS } from "../../firebase/firebase";

const AggiungiLibro = () => {
  const [titolo, setTitolo] = useState("");
  const [autore, setAutore] = useState("");
  const [categoria, setCategoria] = useState("");

  async function gestisciSalvataggio() {
    if (!titolo?.trim() || !autore?.trim() || !categoria?.trim()) {
      Alert.alert("Errore", "Compilare tutti i campi.");
      return;
    }

    const nuovoLibro = {
      titolo: titolo,
      autore: autore,
      categoria: categoria,
      disponibile: true,
    };

    try {
      const response = await fetch(FIREBASE_ENDPOINTS.libri, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(nuovoLibro),
      });

      if (response.ok) {
        Alert.alert("Successo", "Libro aggiunto correttamente!");
        setTitolo("");
        setAutore("");
        setCategoria("");
      } else {
        throw new Error("Risposta del server non valida");
      }
    } catch (error) {
      Alert.alert("Errore", "Impossibile salvare il libro.");
      console.error(error);
    }
  }

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Titolo"
        autoCapitalize="words"
        autoCorrect={false}
        value={titolo}
        onChangeText={(text) => setTitolo(text)}
      ></TextInput>

      <TextInput
        style={styles.input}
        placeholder="Autore"
        autoCapitalize="words"
        autoCorrect={false}
        value={autore}
        onChangeText={(text) => setAutore(text)}
      ></TextInput>

      <TextInput
        style={styles.input}
        placeholder="Categoria"
        autoCapitalize="words"
        autoCorrect={false}
        value={categoria}
        onChangeText={(text) => setCategoria(text)}
      ></TextInput>

      <Pressable style={styles.button} onPress={gestisciSalvataggio}>
        <Text style={styles.buttonText}>AGGIUNGI LIBRO</Text>
      </Pressable>
    </View>
  );
};

export default AggiungiLibro;

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
