import { StyleSheet, Text, View, Pressable } from "react-native";
import React, { useState } from "react";

const MessaggioSegreto = () => {
  const [mostra, setMostra] = useState(false);
  return (
    <View style={styles.container}>
      <Pressable style={styles.bottone} onPress={() => setMostra(!mostra)}>
        <Text style={styles.testoBottone}>
          {mostra ? "Nascondi" : "Mostra"}
        </Text>
      </Pressable>
      {mostra && <Text style={styles.messaggio}>Messaggio segreto</Text>}
    </View>
  );
};

export default MessaggioSegreto;

const styles = StyleSheet.create({
  container: {
    marginTop: 16,
    alignItems: "center",
  },
  bottone: {
    borderWidth: 1,
    padding: 10,
    borderRadius: 8,
    backgroundColor: "#ffffff",
  },
  testoBottone: {
    fontWeight: "bold",
  },
  messaggio: {
    marginTop: 10,
    fontStyle: "italic",
    color: "red",
  },
});
