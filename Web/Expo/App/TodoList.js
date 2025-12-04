import { useState } from "react";
import {
  StyleSheet,
  Text,
  TextInput,
  View,
  Button,
  ScrollView,
  FlatList,
} from "react-native";

export default function App() {
  const [task, setTask] = useState("");
  const [items, setItems] = useState([]);

  function taskInputHandler(enteredTask) {
    setTask(enteredTask);
  }

  function handleClick() {
    if (task.trim()) {
      //il current non è necessario e l'id serve con la flatlist
      setItems((current) => [...current, {task, id: Math.random().toString()}]);
      setTask("");
    }
  }

  return (
    <View style={styles.appContainer}>
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.textInput}
          placeholder="Inserisci task"
          onChangeText={taskInputHandler}
        />
        <Button
          title="Aggiungi"
          onPress={handleClick}
          disabled={task === ""}
        ></Button>
      </View>
      <View style={styles.goalsContainer}>
        <FlatList alwaysBounceVertical={true}
          data={items}
          renderItem={(itemData) => {
            return (
              <View style={styles.taskItem}>
                <Text style={styles.taskText}>{itemData.item.task}</Text>
              </View>
            );
          }}
          keyExtractor={(item, index) => item.id}
        ></FlatList>
        {/* <ScrollView>
          {items.map((item, index) => (
            <View key={index} style={styles.taskItem}>
              <Text style={styles.taskText}>{item}</Text>
            </View>
          ))}
        </ScrollView> */}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    backgroundColor: "#fff",
    paddingTop: 50,
    paddingHorizontal: 16,
  },
  textInput: {
    borderWidth: 1,
    borderColor: "#cccccc",
    width: "70%",
    padding: 8,
  },
  inputContainer: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 24,
    borderBottomWidth: 1,
    borderColor: "#cccccc",
  },
  goalsContainer: {
    flex: 5,
  },
  taskItem: {
    margin: 8,
    padding: 8,
    borderRadius: 6,
    color: "#fff",
    backgroundColor: "#5e0acc",
  },
  taskText: {
    color: "#fff",
  },
});
