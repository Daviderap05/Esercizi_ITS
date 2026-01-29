import { FlatList, StyleSheet, Text, View } from "react-native";
import React from "react";
import { piatti } from "./data/Piatti";

const MenuRistorante = () => {
  return (
    <View>
      {piatti.map((item) => (
        <View key={item.id} style={styles.riga}>
          <Text style={styles.nome}>{item.nome}</Text>
          <Text style={styles.prezzo}>€{item.prezzo}</Text>
        </View>
      ))}
    </View>
  );
};

export default MenuRistorante;

const styles = StyleSheet.create({
  riga: {
    flexDirection: "row",
    justifyContent: "space-between",
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: "#ccc",
  },
  nome: {
    fontSize: 16,
  },
  prezzo: {
    fontSize: 16,
    fontWeight: "bold",
    color: "darkgreen",
  },
});
