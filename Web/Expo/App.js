import { useState, useEffect } from "react";
import { StyleSheet, View, Button, FlatList } from "react-native";

import TaskItem from "./App/components/TodoList/TaskItem";
import TaskInput from "./App/components/TodoList/TaskInput";

const URL =
  "https://todoapp-50614-default-rtdb.europe-west1.firebasedatabase.app/tasks";

export default function App() {
  const [tasks, setTasks] = useState([]);
  const [modalVisible, setModalVisible] = useState(false);

  useEffect(() => {
    loadTasks();
  }, []);

  async function loadTasks() {
    try {
      let response = await fetch(URL + ".json");

      if (!response.ok) {
        throw new Error("Errore: " + response.status);
      }

      let dati = await response.json();

      if (!dati) {
        setTasks([]);
        return;
      }

      const items = Object.keys(dati).map((id) => ({
        id,
        task: dati[id].text,
        done: dati[id].done,
      }));

      setTasks(items);
    } catch (error) {
      console.error("Errore: " + error);
    }
  }

  function startAddTask() {
    setModalVisible(true);
  }

  function endAddTask() {
    setModalVisible(false);
  }

  async function addTaskHandler(taskText) {
    try {
      const newTask = { text: taskText, done: false };

      const response = await fetch(URL + ".json", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newTask),
      });

      if (!response.ok) {
        throw new Error("Errore: " + response.status);
      }

      endAddTask();
      await loadTasks();
    } catch (error) {
      console.error("Errore: " + error);
    }
  }

  async function deleteTask(id) {
    try {
      const response = await fetch(`${URL}/${id}.json`, {
        method: "DELETE",
      });

      if (!response.ok) {
        throw new Error("Errore: " + response.status);
      }

      await loadTasks();
    } catch (e) {
      console.error(e);
    }
  }

  return (
    <View style={styles.appContainer}>
      <Button title="Add New Task" color="#5e0acc" onPress={startAddTask} />

      <TaskInput
        visible={modalVisible}
        onAddTask={addTaskHandler}
        onCancel={endAddTask}
      />

      <View style={styles.listContainer}>
        <FlatList
          data={tasks}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <TaskItem taskItem={item} onDelete={deleteTask} />
          )}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    paddingTop: 50,
    paddingHorizontal: 16,
    backgroundColor: "#fff",
  },
  listContainer: {
    flex: 1,
    marginTop: 12,
  },
});
