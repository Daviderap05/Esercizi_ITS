import { useState, useEffect } from "react";
import { StyleSheet, View, Button, FlatList } from "react-native";

import TaskItem from "./App/components/TodoList/TaskItem";
import TaskInput from "./App/components/TodoList/TaskInput";

const URL =
  "https://todoapp-50614-default-rtdb.europe-west1.firebasedatabase.app/tasks";

export default function App() {
  const [tasks, setTasks] = useState([]);
  const [modalVisible, setModalVisible] = useState(false);
  const [filter, setFilter] = useState("todo");

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
    } catch (error) {
      console.error("Errore: " + error);
    }
  }

  async function updateTask(id) {
    const task = tasks.find((t) => t.id === id);
    try {
      const response = await fetch(`${URL}/${id}.json`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ done: !task.done }),
      });

      if (!response.ok) {
        throw new Error("Errore: " + response.status);
      }

      await loadTasks();
    } catch (error) {
      console.error("Errore: " + error);
    }
  }

  function handlePressDone() {
    setFilter("done");
  }

  function handlePressToDo() {
    setFilter("todo");
  }

  const visibleTasks =
    filter === "done"
      ? tasks.filter((t) => t.done)
      : tasks.filter((t) => !t.done);

  return (
    <View style={styles.appContainer}>
      <Button title="Add New Task" color="#5e0acc" onPress={startAddTask} />
      <View style={{ flexDirection: "row", gap: 8, marginVertical: 16 }}>
        <View style={{ flex: 1 }}>
          <Button title="Done" onPress={handlePressDone} />
        </View>

        <View style={{ flex: 1 }}>
          <Button title="To do" onPress={handlePressToDo} />
        </View>
      </View>

      <TaskInput
        visible={modalVisible}
        onAddTask={addTaskHandler}
        onCancel={endAddTask}
      />

      <View style={styles.listContainer}>
        <FlatList
          data={visibleTasks}
          keyExtractor={(item) => item.id}
          renderItem={({ item }) => (
            <TaskItem
              taskItem={item}
              patchItem={updateTask}
              deleteTask={deleteTask}
            />
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
