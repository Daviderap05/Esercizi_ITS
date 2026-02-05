import {
  StyleSheet,
  Text,
  View,
  Pressable,
  Alert,
  FlatList,
} from "react-native";
import React, { useState, useEffect } from "react";
import { FIREBASE_ENDPOINTS } from "../firebase/firebase";

const Finished = () => {
  const [finished, setFinished] = useState([]);

  async function getTasks() {
    try {
      let response = await fetch(FIREBASE_ENDPOINTS.tasks);

      if (!response.ok) throw new Error("Errore: " + response.status);

      let data = await response.json();

      // il --> || {} serve nel caso il database sia vuoto e quindi data === null
      let data2 = Object.keys(data || {}).map((key) => ({
        id: key,
        ...data[key],
      }));

      setFinished(data2.filter((t) => t.complete === true));
    } catch (error) {
      Alert.alert("Errore: " + error);
      console.error("Errore: " + error);
    }
  }

  async function modStato(itemId) {
    try {
      let response = await fetch(FIREBASE_ENDPOINTS.dettaglioTasks(itemId), {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          complete: false,
        }),
      });

      if (!response.ok) throw new Error("Errore: " + response.status);

      getTasks();
    } catch (error) {
      Alert.alert("Errore: " + error);
      console.error("Errore: " + error);
    }
  }

  async function deleteTask(itemId) {
    try {
      let response = await fetch(FIREBASE_ENDPOINTS.dettaglioTasks(itemId), {
        method: "DELETE",
      });

      if (!response.ok) throw new Error("Errore: " + response.status);

      getTasks();
    } catch (error) {
      Alert.alert("Errore: " + error);
      console.error("Errore: " + error);
    }
  }

  function chiediConferma(item) {
    Alert.alert(
      "Conferma Eliminazione",
      `Vuoi eliminare definitivamente ${item.task}?`,
      [
        { text: "Annulla", style: "cancel" },
        {
          text: "ELIMINA",
          style: "destructive",
          onPress: () => deleteTask(item.id),
        },
      ],
    );
  }

  useEffect(() => {
    getTasks();
  }, []);

  return (
    <FlatList
      data={finished}
      keyExtractor={(item) => item.id}
      style={styles.lista}
      renderItem={({ item }) => {
        return (
          <Pressable
            onPress={() => modStato(item.id)}
            onLongPress={() => chiediConferma(item)}
          >
            <View style={styles.card}>
              <Text style={styles.testo}>{item.task}</Text>
            </View>
          </Pressable>
        );
      }}
    />
  );
};

export default Finished;

const styles = StyleSheet.create({
  testo: {
    fontSize: 20,
  },
  card: {
    borderBottomWidth: 1,
    padding: 25,
  },
});
