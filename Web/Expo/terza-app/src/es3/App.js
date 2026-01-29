import {
  StyleSheet,
  View,
  ScrollView,
} from "react-native";
import React from "react";
import Saluto from "./src/es3/Saluto";
import CardUtente from "./src/es2/CardUtente";

const App = () => {
  return (
    <View style={styles.container}>
      <Saluto></Saluto>
      <ScrollView>
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
  },
});
