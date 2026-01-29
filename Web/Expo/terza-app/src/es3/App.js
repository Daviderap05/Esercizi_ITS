import { StyleSheet, Text, View, ScrollView } from "react-native";
import React from "react";
import Saluto from "./src/es3/Saluto";
import CardUtente from "./src/es3/CardUtente";
import MenuRistorante from "./src/es3/MenuRistorante";
import Termostato from "./src/es3/Termostato";
import CampoRicerca from "./src/es3/CampoRicerca";
import MessaggioSegreto from "./src/es3/MessaggioSegreto";

const App = () => {
  return (
    <View style={styles.container}>
      <Saluto />

      <ScrollView style={{ flexGrow: 0 }}>
        <CardUtente
          nome="Davide Rossi"
          email="davide@test.it"
          imgUrl="https://i.pravatar.cc/150?u=davide"
        />
        <CardUtente
          nome="Mario Neri"
          email="mario@test.it"
          imgUrl="https://i.pravatar.cc/150?u=mario"
        />

        <MenuRistorante />
        
        <View style={styles.termostato}>
          <Termostato />
        </View>

        <View style={styles.ricerca}>
          <CampoRicerca></CampoRicerca>
        </View>

        <MessaggioSegreto></MessaggioSegreto>
      </ScrollView>
    </View>
  );
};

export default App;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f5f5f5",
    paddingTop: 60,
    paddingHorizontal: 20,
    marginBottom: 30,
  },
  termostato: {
    marginTop: 16,
    borderWidth: 1,
    borderColor: "#000000",
    backgroundColor: "#fff",
    borderRadius: 10,
  },
  ricerca: {
    marginTop: 16,
    borderWidth: 1,
    borderRadius: 10,
    padding: 12,
  },
});
