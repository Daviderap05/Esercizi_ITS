import { StyleSheet, Text, View, Button } from "react-native";
import React from "react";
import { useNavigation } from "@react-navigation/native";

const Home = () => {
  const navigate = useNavigation();
  return (
    <>
      <View style={{ marginBottom: 20 }}>
        <Button title="Aggiungi" onPress={() => navigate.navigate("Add")} />
      </View>

      <View style={{ marginBottom: 20 }}>
        <Button title="ToDo" onPress={() => navigate.navigate("ToDo")} />
      </View>

      <View style={{ marginBottom: 20 }}>
        <Button title="Finite" onPress={() => navigate.navigate("Finished")} />
      </View>
    </>
  );
};

export default Home;

const styles = StyleSheet.create({});
