import React, { useState } from "react";
import {
  StyleSheet,
  TextInput,
  View,
  Button,
  Modal,
  Image,
} from "react-native";

export default function TaskInput({ visible, onAddTask, onCancel }) {
  const [text, setText] = useState("");

  function changeHandler(value) {
    setText(value);
  }

  function addHandler() {
    const trimmed = text.trim();
    if (!trimmed) return;

    onAddTask(trimmed);
    setText("");
    onCancel();
  }

  function cancelHandler() {
    setText("");
    onCancel();
  }

  return (
    <Modal visible={visible} animationType="slide">
      <View style={styles.inputContainer}>
        <Image
          style={styles.image}
          source={{
            uri: "https://www.dropbox.com/scl/fi/2z78bc6kybcbktiazwn9p/goal.png?rlkey=fhww8krf0rwg4rurigo7ht3i6&dl=1",
          }}
        />

        <TextInput
          style={styles.textInput}
          placeholder="Inserisci task"
          placeholderTextColor="#cfc7ff"
          onChangeText={changeHandler}
          value={text}
        />

        <View style={styles.buttonContainer}>
          <View style={styles.button}>
            <Button
              title="Aggiungi"
              onPress={addHandler}
              color="#f31282"
              disabled={text.trim() === ""}
            />
          </View>

          <View style={styles.button}>
            <Button title="Annulla" onPress={cancelHandler} color="#b180f0" />
          </View>
        </View>
      </View>
    </Modal>
  );
}

const styles = StyleSheet.create({
  inputContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 16,
    gap: 16,
    backgroundColor: "#311b6b",
  },
  textInput: {
    borderWidth: 1,
    borderColor: "#cfc7ff",
    color: "white",
    width: "75%",
    padding: 10,
    borderRadius: 8,
  },
  image: {
    height: 100,
    width: 100,
    marginBottom: 12,
  },
  buttonContainer: {
    flexDirection: "row",
    marginTop: 8,
  },
  button: {
    marginHorizontal: 8,
    minWidth: 120,
  },
});
