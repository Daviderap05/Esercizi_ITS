import { StyleSheet, Text, View, TextInput } from "react-native";
import React, { useEffect, useState } from "react";

const CampoRicerca = () => {
  const [testoRicerca, setTestoRicerca] = useState("");
  return (
    <View>
      <TextInput
        placeholder="Inserisci testo"
        value={testoRicerca}
        onChangeText={(text) => setTestoRicerca(text)}
      ></TextInput>
      <Text>Stai cercando: {testoRicerca}</Text>
    </View>
  );
};

export default CampoRicerca;

const styles = StyleSheet.create({});
