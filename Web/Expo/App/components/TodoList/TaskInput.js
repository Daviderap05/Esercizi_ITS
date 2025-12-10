import React, { useState } from "react";
import {
  StyleSheet,
  TextInput,
  View,
  Button,
  Modal,
  Image,
} from "react-native";
const TaskInput = (props) => {
  const [task, setTask] = useState("");
  function taskInputHandler(enteredTask) {
    console.log(enteredTask);
    setTask(enteredTask);
  }
  function addTask() {
    props.onAddTask(task);
    setTask("");
    props.onCancel();
  }
  function annulla() {
    setTask("");
    props.onCancel();
  }
  return (
    <Modal visible={props.visible} animationType="slide">
      {" "}
      <View style={styles.inputContainer}>
        {" "}
        <Image
          style={styles.image}
          source={{
            uri: "https://www.dropbox.com/scl/fi/2z78bc6kybcbktiazwn9p/goal.png?rlkey=fhww8krf0rwg4rurigo7ht3i6&dl=0",
          }}
        ></Image>{" "}
        <TextInput
          style={styles.textInput}
          placeholder="Inserisci task"
          onChangeText={taskInputHandler}
          value={task}
        />{" "}
        <View style={styles.buttonContainer}>
          {" "}
          <View style={styles.button}>
            {" "}
            <Button
              title="Aggiungi"
              onPress={addTask}
              color="#f31282"
              disabled={task === ""}
            ></Button>{" "}
          </View>{" "}
          <View style={styles.button}>
            {" "}
            <Button
              title="Annulla"
              onPress={annulla}
              color="#b180f0"
            ></Button>{" "}
          </View>{" "}
        </View>{" "}
      </View>{" "}
    </Modal>
  );
};
const styles = StyleSheet.create({
  textInput: {
    borderWidth: 1,
    borderColor: "#cccccc",
    width: "70%",
    padding: 8,
  },
  image: { height: 100, width: 100, margin: 20 },
  inputContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    marginBottom: 24,
    borderBottomWidth: 1,
    borderBottomColor: "#cccccc",
    gap: 16,
    backgroundColor: "#311b6b",
  },
  buttonContainer: { flexDirection: "row" },
  button: { marginHorizontal: 8 },
});
export default TaskInput;
