import React from "react";
import { Text, View, StyleSheet, Pressable } from "react-native";

export default function TaskItem({ taskItem, onDelete }) {
  function pressHandler() {
    onDelete(taskItem.id);
  }

  return (
    <View style={styles.taskItem}>
      <Pressable
        android_ripple={{ color: "#210644" }}
        onPress={pressHandler}
        style={({ pressed }) => [styles.pressable, pressed && styles.pressed]}
      >
        <Text style={styles.taskText}>{taskItem.task}</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  taskItem: {
    marginVertical: 6,
    borderRadius: 8,
    overflow: "hidden", // importante per ripple dentro bordi arrotondati
    backgroundColor: "#5e0acc",
  },
  pressable: {
    padding: 12,
  },
  pressed: {
    opacity: 0.6,
  },
  taskText: {
    color: "#fff",
    fontSize: 16,
  },
});
