import { StyleSheet, Text, View, Pressable } from "react-native";
import React, { useState } from "react";

const Termostato = () => {
  const [temp, setTemp] = useState(20);
  return (
    <View style={styles.riga}>
      <Text style={styles.nome}>Termostato: {temp}°</Text>
      <View style={styles.pulsanti}>
        <Pressable style={styles.tasto} onPress={() => setTemp(temp + 1)}>
          <Text style={styles.testoTasto}>+</Text>
        </Pressable>
        <Pressable style={styles.tasto} onPress={() => setTemp(temp - 1)}>
          <Text style={styles.testoTasto}>-</Text>
        </Pressable>
      </View>
    </View>
  );
};

export default Termostato;

const styles = StyleSheet.create({
  riga: {
    padding: 16,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  nome: {
    fontSize: 18,
    fontWeight: "bold",
  },
  pulsanti: {
    flexDirection: "row",
    gap: 16,
  },
  tasto: {
    backgroundColor: "#007AFF",
    width: 40,
    height: 40,
    borderRadius: 20,
    justifyContent: "center",
    alignItems: "center",
  },
  testoTasto: {
    color: "white",
    fontSize: 20,
    fontWeight: "bold",
  }
});