import {
  StyleSheet,
  Text,
  Alert,
  View,
  Pressable,
  TextInput,
  ScrollView,
} from "react-native";
import React, { useState, useEffect } from "react";
import {
  useRoute,
  useNavigation,
  useIsFocused,
} from "@react-navigation/native";
import { FIREBASE_ENDPOINTS } from "../../../../firebase/firebase";

const FormLibriMod = () => {
  const navigation = useNavigation();
  const route = useRoute();

  const { libro } = route.params;

  const isFocused = useIsFocused();

  const [titolo, setTitolo] = useState(libro.titolo);
  const [autore, setAutore] = useState(libro.autore);
  const [categoria, setCategoria] = useState(libro.categoria);

  async function gestisciModifica() {
    if (!titolo?.trim() || !autore?.trim() || !categoria?.trim()) {
      Alert.alert("Errore", "I campi non possono essere vuoti.");
      return;
    }

    try {
      const response = await fetch(
        FIREBASE_ENDPOINTS.dettaglioLibro(libro.id),
        {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            titolo: titolo,
            autore: autore,
            categoria: categoria,
          }),
        },
      );

      if (!response.ok) throw new Error("Errore durante il salvataggio");

      Alert.alert("Successo", "Libro modificato correttamente!", [
        { text: "OK", onPress: () => navigation.goBack() },
      ]);
    } catch (error) {
      console.error(error);
      Alert.alert("Errore", "Impossibile salvare le modifiche.");
    }
  }

  useEffect(() => {
    if (!isFocused) {
      navigation.popToTop();
    }
  }, [isFocused]);

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.label}>ID Libro (Non modificabile)</Text>
      <View style={styles.readOnlyContainer}>
        <Text style={styles.readOnlyText}>{libro.id}</Text>
      </View>

      <Text style={styles.label}>Titolo</Text>
      <TextInput
        style={styles.input}
        value={titolo}
        onChangeText={setTitolo}
        placeholder="Inserisci titolo"
      />

      <Text style={styles.label}>Autore</Text>
      <TextInput
        style={styles.input}
        value={autore}
        onChangeText={setAutore}
        placeholder="Inserisci autore"
      />

      <Text style={styles.label}>Categoria</Text>
      <TextInput
        style={styles.input}
        value={categoria}
        onChangeText={setCategoria}
        placeholder="Inserisci categoria"
      />

      <Pressable style={styles.button} onPress={gestisciModifica}>
        <Text style={styles.buttonText}>SALVA MODIFICHE</Text>
      </Pressable>
    </ScrollView>
  );
};

export default FormLibriMod;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: "#f5f5f5",
  },
  label: {
    fontSize: 14,
    fontWeight: "bold",
    marginBottom: 5,
    color: "#555",
    marginTop: 10,
  },
  input: {
    backgroundColor: "white",
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 15,
    fontSize: 16,
    marginBottom: 5,
  },
  readOnlyContainer: {
    backgroundColor: "#e0e0e0",
    padding: 15,
    borderRadius: 8,
    marginBottom: 5,
    borderWidth: 1,
    borderColor: "#ccc",
  },
  readOnlyText: {
    color: "#555",
  },
  button: {
    backgroundColor: "#fd7e14",
    padding: 15,
    borderRadius: 8,
    alignItems: "center",
    marginTop: 30,
    marginBottom: 50,
    elevation: 3,
  },
  buttonText: {
    color: "white",
    fontWeight: "bold",
    fontSize: 16,
  },
});
