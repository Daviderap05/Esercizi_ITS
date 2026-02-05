import React from "react";
import { View, Text, Pressable, StyleSheet } from "react-native";

export default function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>
        Benvenuto nella mia ToDoApp!
      </Text>

      <Pressable
        style={styles.button}
        onPress={() => navigation.navigate('AddTask')}
      >
        <Text style={styles.buttonText}>
          Aggiungi Task
        </Text>
      </Pressable>

      <Pressable
        style={[styles.button, styles.buttonMargin]}
        onPress={() => navigation.navigate('ViewTasks')}
      >
        <Text style={styles.buttonText}>
          Visualizza Tasks
        </Text>
      </Pressable>

      <Pressable
        style={[styles.button, styles.buttonMargin]}
        onPress={() => navigation.navigate('ViewTasksCompletate')}
      >
        <Text style={styles.buttonText}>
          Visualizza Tasks Completate
        </Text>
      </Pressable>

    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#be7575',
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    fontSize: 18,
    color: '#fff',
    marginBottom: 20,
  },
  button: {
    backgroundColor: '#ffffff',
    paddingVertical: 10,
    paddingHorizontal: 24,
    borderRadius: 4,
  },
  buttonMargin: {
    marginTop: 12,
  },
  buttonText: {
    color: '#be7575',
    fontSize: 16,
  },
});
