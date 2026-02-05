import React, { useState } from "react";
import { View, TextInput, Pressable, Text, StyleSheet } from "react-native";
import { BASE_URL } from "../firebase/firebaseconfig";

export default function EditTask({ route, navigation }) {
  const { task } = route.params;

  const [nome, setNome] = useState(task.nome);
  const [descrizione, setDescrizione] = useState(task.descrizione);

  const patchTask = async (task) => {
    const response = await fetch(`${BASE_URL}/tasks/${task.id}.json`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ 'nome': nome, 'descrizione': descrizione })
    });

    if (response.ok) {
      alert("Task aggiornata!");
      navigation.popToTop();
    } else {
      alert("Errore durante l'aggiornamento");
    }
  }

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Inserisci nome"
        placeholderTextColor="#888"
        value={nome}
        onChangeText={setNome}
      />

      <TextInput
        style={styles.input}
        placeholder="Inserisci breve descrizione"
        placeholderTextColor="#888"
        value={descrizione}
        onChangeText={setDescrizione}
      />

      <Pressable style={styles.button} onPress={() => patchTask(task)}>
        <Text style={styles.buttonText}>Invia</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#be7575',
    padding: 16,
    justifyContent: 'center',
  },
  input: {
    backgroundColor: '#fff',
    color: '#000',
    paddingVertical: 10,
    paddingHorizontal: 12,
    borderRadius: 4,
    marginBottom: 16,
    fontSize: 16,
  },
  button: {
    backgroundColor: '#ffffff',
    paddingVertical: 10,
    paddingHorizontal: 24,
    borderRadius: 4,
    alignItems: 'center',
  },
  buttonText: {
    color: '#be7575',
    fontSize: 16,
  },
});
