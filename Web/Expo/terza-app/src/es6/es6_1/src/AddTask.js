import {
  StyleSheet,
  Text,
  View,
  Pressable,
  TextInput,
  Alert,
} from "react-native";
import React, { useState } from "react";
import { FIREBASE_ENDPOINTS } from "../firebase/firebase";

const AddTask = () => {
  const [task, setTask] = useState("");

  async function addTask() {
    try {
      if (!task.trim()) {
        Alert.alert("Inserisci un Task");
        return;
      }

      let response = await fetch(FIREBASE_ENDPOINTS.tasks, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          task: task,
          complete: false,
        }),
      });

      if (!response.ok) throw new Error("Errore");
      Alert.alert("Inserimento completato");
      setTask("");
    } catch (error) {
      Alert.alert("Errore: " + error);
      console.error("Errore: " + error);
    }
  }
  return (
    <View style={styles.form}>
      <TextInput
        style={styles.input}
        placeholder="inserisci task"
        value={task}
        onChangeText={(text) => setTask(text)}
      />
      <Pressable onPress={() => addTask()} style={styles.bottone}>
        <Text style={styles.testoBottone}>AGGIUNGI</Text>
      </Pressable>
    </View>
  );
};

export default AddTask;

const styles = StyleSheet.create({
  form: { marginTop: 100, alignItems: "center" },
  input: {
    fontSize: 20,
    borderWidth: 2,
    borderRadius: 8,
    padding: 16,
    width: 300,
    borderColor: "#000000",
  },
  bottone: {
    marginTop: 20,
  },
  testoBottone: { fontSize: 20, color: "red", borderRadius: 8 },
});
