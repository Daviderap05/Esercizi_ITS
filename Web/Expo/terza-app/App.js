import "react-native-gesture-handler";

import { StyleSheet } from "react-native";
import React from "react";

import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { createDrawerNavigator } from "@react-navigation/drawer";
import { NavigationContainer } from "@react-navigation/native";

//Stack Home
import Home from "./src/es4/src/screens/home/Home";

// Stack Aggiunte
import AggiungiLibro from "./src/es4/src/screens/aggiungi/AggiungiLibro";
import AggiungiUtente from "./src/es4/src/screens/aggiungi/AggiungiUtente";

// Stack Affitto
import ListaLibriAffitto from "./src/es4/src/screens/affitto/ListaLibriAffitto";
import ListaUtentiAffitto from "./src/es4/src/screens/affitto/ListaUtentiAffitto";

// Stack Restituzione
import ListaNoleggiAttivi from "./src/es4/src/screens/restituzione/ListaNoleggiAttivi";
import DettaglioRestituzione from "./src/es4/src/screens/restituzione/DettaglioRestituzione";

// Stack Modifica Libri
import ListaLibriMod from "./src/es4/src/screens/modifica/libri/ListaLibriMod";
import FormLibriMod from "./src/es4/src/screens/modifica/libri/FormLibriMod";

// Stack Modifica Utenti
import ListaUtentiMod from "./src/es4/src/screens/modifica/utenti/ListaUtentiMod";
import FormUtentiMod from "./src/es4/src/screens/modifica/utenti/FormUtentiMod";

// Stack Elimina
import EliminaLibro from "./src/es4/src/screens/elimina/EliminaLibro";
import EliminaUtente from "./src/es4/src/screens/elimina/EliminaUtente";

const Drawer = createDrawerNavigator();

const StackAffitto = createNativeStackNavigator();
const StackRestituzione = createNativeStackNavigator();

const StackLibMod = createNativeStackNavigator();
const StackUsrMod = createNativeStackNavigator();

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

function ModLib() {
  return (
    <StackLibMod.Navigator>
      <StackLibMod.Screen name="SelezionaLibro" component={ListaLibriMod} />
      <StackLibMod.Screen name="ModificaParametri" component={FormLibriMod} />
    </StackLibMod.Navigator>
  );
}

function ModUsr() {
  return (
    <StackUsrMod.Navigator>
      <StackUsrMod.Screen name="SelezionaUtente" component={ListaUtentiMod} />
      <StackUsrMod.Screen name="ModificaParametri" component={FormUtentiMod} />
    </StackUsrMod.Navigator>
  );
}

const App = () => {
  return (
    <NavigationContainer>
      <Drawer.Navigator screenOptions={{ unmountOnBlur: true }}>
        <Drawer.Screen
          name="Home"
          component={Home}
          options={{
            drawerActiveTintColor: "green",
            drawerActiveBackgroundColor: "#e8f5e9",
            drawerInactiveTintColor: "gray",
          }}
        />
        <Drawer.Screen name="Aggiungi Libro" component={AggiungiLibro} />
        <Drawer.Screen name="Aggiungi Utente" component={AggiungiUtente} />
        <Drawer.Screen name="Affitta Libro" component={AffittoStack} />
        <Drawer.Screen name="Restituisci Libro" component={RestituzioneStack} />
        <Drawer.Screen
          name="Modifica Libro"
          component={ModLib}
          options={{
            drawerActiveTintColor: "#E65100", // Arancione scuro
            drawerActiveBackgroundColor: "#FFF3E0", // Arancione chiarissimo
            drawerInactiveTintColor: "gray",
          }}
        />
        <Drawer.Screen
          name="Modifica Utente"
          component={ModUsr}
          options={{
            drawerActiveTintColor: "#E65100",
            drawerActiveBackgroundColor: "#FFF3E0",
            drawerInactiveTintColor: "gray",
          }}
        />
        <Drawer.Screen
          name="Elimina Libro"
          component={EliminaLibro}
          options={{
            drawerActiveTintColor: "red",
            drawerActiveBackgroundColor: "#ffebee",
            drawerInactiveTintColor: "gray",
          }}
        />
        <Drawer.Screen
          name="Elimina Utente"
          component={EliminaUtente}
          options={{
            drawerActiveTintColor: "red",
            drawerActiveBackgroundColor: "#ffebee",
            drawerInactiveTintColor: "gray",
          }}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  );
};

export default App;

const styles = StyleSheet.create({});