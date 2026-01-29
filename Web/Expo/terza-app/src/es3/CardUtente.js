import { StyleSheet, Text, View, Image } from "react-native";
import React from "react";

const CardUtente = (props) => {
  return (
    <View style={styles.card}>
      {/* Per le immagini da URL è OBBLIGATORIO definire larghezza e altezza */}
      <Image source={{ uri: props.imgUrl }} style={styles.avatar} />
      <View style={styles.info}>
        <Text style={styles.nome}>{props.nome}</Text>
        <Text style={styles.email}>{props.email}</Text>
      </View>
    </View>
  );
};

export default CardUtente;

const styles = StyleSheet.create({
  card: {
    flexDirection: "row", // Mette immagine e testi sulla stessa riga
    backgroundColor: "#fff",
    padding: 15,
    borderRadius: 10,
    marginBottom: 15,
    alignItems: "center",
    borderWidth: 1,
    borderColor: "#000000",
  },
  avatar: {
    width: 60,
    height: 60,
    borderRadius: 30, // Cerchio perfetto
    marginRight: 15,
  },
  nome: {
    fontSize: 18,
    fontWeight: "bold",
  },
  email: {
    color: "#666",
  },
});
