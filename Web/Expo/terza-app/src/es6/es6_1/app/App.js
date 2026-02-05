import { StyleSheet, Text, View, Pressable } from "react-native";
import React, { useState } from "react";

import AddTask from "./src/es6/es6_1/src/AddTask";
import ToDo from "./src/es6/es6_1/src/ToDo";
import Finished from "./src/es6/es6_1/src/Finished";

const App = () => {
  const [screen, setScreen] = useState(null);
  return (
    <View style={styles.container}>
      <Pressable style={styles.bottone} onPress={() => setScreen("Add")}>
        <Text style={styles.testo}>AGGIUNGI TASK</Text>
      </Pressable>

      <View style={styles.bottoni}>
        <Pressable style={styles.bottone} onPress={() => setScreen("ToDo")}>
          <Text style={styles.testo}>Da fare</Text>
        </Pressable>

        <Pressable style={styles.bottone} onPress={() => setScreen("Finish")}>
          <Text style={styles.testo}>Fatte</Text>
        </Pressable>
      </View>

      {screen === "Add" && (
        <View style={styles.form}>
          <AddTask></AddTask>
        </View>
      )}

      {screen === "ToDo" && <ToDo></ToDo>}

      {screen === "Finish" && <Finished></Finished>}
    </View>
  );
};

export default App;

const styles = StyleSheet.create({
  container: {
    marginTop: 60,
    padding: 16,
  },
  bottoni: {
    marginTop: 24,
    flexDirection: "row",
    justifyContent: "space-between",
  },
  bottone: {
    borderWidth: 2,
    padding: 16,
    minWidth: 100,
    borderRadius: 8,
    backgroundColor: "#80bdf7",
    alignItems: "center",
  },
  testo: {
    fontSize: 20,
  },
  form: {
    alignContent: "center",
  },
});
