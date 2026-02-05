import React, { useState } from "react";
import { TextInput, View, StyleSheet, Pressable, Text, Alert } from "react-native";
import { BASE_URL } from "../firebase/firebaseconfig";

export default function AddTask({ navigation }) {

  const[nome, setNome] = useState('');
  const[descrizione, setDescrizione] = useState('');

  const createTask = async () => {
    
    const task = {
      'nome': nome,
      'descrizione': descrizione,
      'complete': false
    }
  
    try {
      const response = await fetch(`${BASE_URL}/tasks.json`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'}, 
        body: JSON.stringify(task)
    });

    if (response.ok) {
      Alert.alert("Successo", "Task inserita con successo")
      navigation.popToTop();
    } else {
      Alert.alert("Errore", "Errore durante l'inserimento")
    }
  } catch (error) {
    Alert.alert("Errore", "Riprova più tardi" + error)
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

      <Pressable style={styles.button} onPress={() => createTask()}>
        <Text style={styles.buttonText}> Invia </Text>
      </Pressable>

    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#be7575',
    padding: 20,
    justifyContent: 'center',
  },
  input: {
    backgroundColor: '#fff',
    color: '#000',
    paddingVertical: 10,
    paddingHorizontal: 12,
    borderRadius: 4,
    marginBottom: 15,
    fontSize: 16,
  },
  button: {
    backgroundColor: '#ffffff',
    paddingVertical: 10,
    paddingHorizontal: 24,
    borderRadius: 4
  },
  buttonText: {
    color: '#be7575',
    fontSize: 16,
    alignSelf: 'center'
  },
});
