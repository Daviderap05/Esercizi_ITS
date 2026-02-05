import React, { useCallback, useState } from "react";
import { View, FlatList, Alert, Text, Pressable, StyleSheet } from "react-native";
import { useFocusEffect } from '@react-navigation/native';
import { BASE_URL } from "../firebase/firebaseconfig";

export default function ViewTasksCompletate({ navigation }) {
  const [tasks, setTasks] = useState([]);

  const getTasksComplete = async () => {
    try {
      const response = await fetch(`${BASE_URL}/tasks.json`);
      const data = await response.json();

      if (data) {
        const ArrayTasks = Object.keys(data).map(id => ({
          id,
          ...data[id],
        }));

        const TaskCompletate = ArrayTasks.filter(t => t.complete == true)
        setTasks(TaskCompletate);
      } else {
        Alert.alert("Errore", "Nessuna task presente.");
      }
    } catch (error) {
      Alert.alert("Errore", "Riprova più tardi." + error);
    }
  };

  useFocusEffect(
    useCallback(() => {
      getTasksComplete();
    }, [])
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={tasks}
        keyExtractor={t => t.id}
        renderItem={({ item }) => (

          <View style={styles.card}>
            <Text style={styles.taskText}>
              {item.nome} - {item.descrizione}
            </Text>
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
