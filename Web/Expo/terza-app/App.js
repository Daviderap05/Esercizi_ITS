import "react-native-gesture-handler";
import { StyleSheet } from "react-native";
import React from "react";

import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { createDrawerNavigator } from "@react-navigation/drawer";
import { NavigationContainer } from "@react-navigation/native";

// Schermate principali
import AggiungiLibro from "./src/es4/src/screens/AggiungiLibro";
import AggiungiUtente from "./src/es4/src/screens/AggiungiUtente";

// Stack Affitto
import ListaLibriAffitto from "./src/es4/src/screens/affitto/ListaLibriAffitto";
import ListaUtentiAffitto from "./src/es4/src/screens/affitto/ListaUtentiAffitto";

// Stack Restituzione
import ListaNoleggiAttivi from "./src/es4/src/screens/restituzione/ListaNoleggiAttivi";
import DettaglioRestituzione from "./src/es4/src/screens/restituzione/DettaglioRestituzione";

// Stack Elimina
import EliminaLibro from "./src/es4/src/screens/elimina/EliminaLibro";
import EliminaUtente from "./src/es4/src/screens/elimina/EliminaUtente";

const Drawer = createDrawerNavigator();
const StackAffitto = createNativeStackNavigator();
const StackRestituzione = createNativeStackNavigator();

function AffittoStack() {
  return (
    <StackAffitto.Navigator>
      <StackAffitto.Screen
        name="SelezionaLibro"
        component={ListaLibriAffitto}
      />
      <StackAffitto.Screen
        name="SelezionaUtente"
        component={ListaUtentiAffitto}
      />
    </StackAffitto.Navigator>
  );
}

function RestituzioneStack() {
  return (
    <StackRestituzione.Navigator>
      <StackRestituzione.Screen
        name="SelezionaUtente"
        component={ListaNoleggiAttivi}
      />
      <StackRestituzione.Screen
        name="SelezionaLibro"
        component={DettaglioRestituzione}
      />
    </StackRestituzione.Navigator>
  );
}

const App = () => {
  return (
    <NavigationContainer>
      <Drawer.Navigator screenOptions={{ unmountOnBlur: true }}>
        <Drawer.Screen name="Aggiungi Libro" component={AggiungiLibro} />
        <Drawer.Screen name="Aggiungi Utente" component={AggiungiUtente} />
        <Drawer.Screen name="Affitta Libro" component={AffittoStack} />
        <Drawer.Screen name="Restituisci Libro" component={RestituzioneStack} />
        <Drawer.Screen
          name="Elimina Libro"
          component={EliminaLibro}
          options={{
            drawerActiveTintColor: "red",
            drawerActiveBackgroundColor: "#ffebee",
            drawerInactiveTintColor: "gray",
            unmountOnBlur: true,
          }}
        />
        <Drawer.Screen
          name="Elimina Utente"
          component={EliminaUtente}
          options={{
            drawerActiveTintColor: "red",
            drawerActiveBackgroundColor: "#ffebee",
            drawerInactiveTintColor: "gray",
            unmountOnBlur: true,
          }}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  );
};

export default App;

const styles = StyleSheet.create({});
