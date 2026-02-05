import React, { useCallback, useState } from "react";
import { View, FlatList, Alert, Text, Pressable, StyleSheet } from "react-native";
import { useFocusEffect } from '@react-navigation/native';
import { BASE_URL } from "../firebase/firebaseconfig";

export default function ViewTasks({ navigation }) {
  const [tasks, setTasks] = useState([]);

  const getTasks = async () => {
    try {
      const response = await fetch(`${BASE_URL}/tasks.json`);
      const data = await response.json();

      if (data) {
        const ArrayTasks = Object.keys(data).map(id => ({
          id,
          ...data[id],
        }));

        const TasksIncomplete = ArrayTasks.filter(t => t.complete == false)
        setTasks(TasksIncomplete);
      } else {
        Alert.alert("Errore", "Nessuna task presente.");
      }
    } catch (error) {
      Alert.alert("Errore", "Riprova più tardi." + error);
    }
  };

  const deleteTask = async (task) => {

    try {
        const response = await fetch(`${BASE_URL}/tasks/${task.id}.json`, {
            method: 'DELETE'
        })
        
        if (response.ok) {
            Alert.alert("Successo", "Task eliminata con successo");
            navigation.popToTop();
        } else {
            Alert.alert("Errore", "Impossibile eliminare task.");
        }
    } catch (error) {
        Alert.alert("Errore", "Riprova più tardi" + error)
    }
  }

    const completeTask = async (task) => {
    try {
        const response = await fetch(`${BASE_URL}/tasks/${task.id}.json`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ complete: true })
        });

        if (response.ok) {
        alert("Task completata!");
        navigation.popToTop();
        } else {
        alert("Errore: impossibile completare la task.");
        }
    } catch (error) {
        alert("Errore: riprova più tardi. " + error);
    }
    }

  useFocusEffect(
    useCallback(() => {
      getTasks();
    }, [])
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={tasks}
        keyExtractor={t => t.id}
        renderItem={({ item }) => (
          <View style={styles.card}>

            <Pressable onPress={() => {completeTask(item)}}>
                <Text style={styles.taskText}>
                    {item.nome} - {item.descrizione}
                </Text>
            </Pressable>

            <View style={styles.buttonRow}>
              <Pressable style={styles.button} onPress={() => navigation.navigate("EditTask", {task: item})}>
                <Text style={styles.buttonText}>Modifica</Text>
              </Pressable>

              <Pressable style={[styles.button, styles.deleteButton]} onPress={() => deleteTask(item)}>
                <Text style={styles.buttonText}>Elimina</Text>
              </Pressable>
            </View>
          </View>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#be7575',
    padding: 16,
  },
  card: {
    backgroundColor: '#fff',
    padding: 12,
    borderRadius: 6,
    marginBottom: 12,
  },
  taskText: {
    fontSize: 16,
    marginBottom: 8,
    color: '#000',
  },
  buttonRow: {
    flexDirection: 'row',
    justifyContent: 'flex-start',
  },
  button: {
    backgroundColor: '#be7575',
    paddingVertical: 6,
    paddingHorizontal: 12,
    borderRadius: 4,
    marginRight: 8,
  },
  deleteButton: {
    backgroundColor: '#ff4d4d',
  },
  buttonText: {
    color: '#fff',
    fontSize: 14,
  },
});
