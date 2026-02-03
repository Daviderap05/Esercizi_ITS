import {
  StyleSheet,
  Text,
  Alert,
  View,
  Pressable,
  TextInput,
  ScrollView,
} from "react-native";

import React, { useState, useEffect } from "react";

import {
  useRoute,
  useNavigation,
  useIsFocused,
} from "@react-navigation/native";

import { FIREBASE_ENDPOINTS } from "../../../../firebase/firebase";

const FormUtentiMod = () => {
  const navigation = useNavigation();
  const route = useRoute();

  const { utente } = route.params;

  const isFocused = useIsFocused();

  const [nome, setNome] = useState(utente.nome);
  const [cognome, setCognome] = useState(utente.cognome);
  const [mail, setMail] = useState(utente.mail);

  const reg = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;

  async function gestisciModifica() {
    if (!nome.trim() || !cognome.trim() || !mail.trim()) {
      Alert.alert("Errore", "Compilare tutti i campi.");
      return;
    }

    if (!reg.test(mail.trim())) {
      Alert.alert("Errore", "Sintassi email non valida.");
      return;
    }

    try {
      const response = await fetch(
        FIREBASE_ENDPOINTS.dettaglioUtente(utente.id),
        {
          method: "PATCH",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            nome: nome,
            cognome: cognome,
            mail: mail,
          }),
        },
      );

      if (!response.ok) throw new Error("Errore durante il salvataggio");

      Alert.alert("Successo", "Utente modificato correttamente!", [
        { text: "OK", onPress: () => navigation.goBack() },
      ]);
    } catch (error) {
      console.error(error);
      Alert.alert("Errore", "Impossibile salvare le modifiche.");
    }
    }
    
    useEffect(() => {
      if (!isFocused) {
        navigation.popToTop();
      }
    }, [isFocused]);

  return (
    <ScrollView style={styles.container}>
      <Text style={styles.label}>ID Utente (Non modificabile)</Text>
      <View style={styles.readOnlyContainer}>
        <Text style={styles.readOnlyText}>{utente.id}</Text>
      </View>

      <Text style={styles.label}>Libri in possesso (Non modificabile)</Text>
      <View style={styles.readOnlyContainer}>
        <Text style={styles.readOnlyText}>
          {utente.affitti ? utente.affitti.length : 0}
        </Text>
      </View>

      <Text style={styles.label}>Nome</Text>
      <TextInput
        style={styles.input}
        value={nome}
        onChangeText={setNome}
        placeholder="Inserisci nome"
        autoCapitalize="words"
      />

      <Text style={styles.label}>Cognome</Text>
      <TextInput
        style={styles.input}
        value={cognome}
        onChangeText={setCognome}
        placeholder="Inserisci cognome"
        autoCapitalize="words"
      />

      <Text style={styles.label}>Email</Text>
      <TextInput
        style={styles.input}
        value={mail}
        onChangeText={setMail}
        placeholder="Inserisci email"
        keyboardType="email-address"
        autoCapitalize="none"
      />

      <Pressable style={styles.button} onPress={gestisciModifica}>
        <Text style={styles.buttonText}>SALVA MODIFICHE</Text>
      </Pressable>
    </ScrollView>
  );
};

export default FormUtentiMod;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: "#f5f5f5",
  },
  label: {
    fontSize: 14,
    fontWeight: "bold",
    marginBottom: 5,
    color: "#555",
    marginTop: 10,
  },
  input: {
    backgroundColor: "white",
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 8,
    padding: 15,
    fontSize: 16,
    marginBottom: 5,
  },
  readOnlyContainer: {
    backgroundColor: "#e0e0e0",
    padding: 15,
    borderRadius: 8,
    marginBottom: 5,
    borderWidth: 1,
    borderColor: "#ccc",
  },
  readOnlyText: {
    color: "#555",
  },
  button: {
    backgroundColor: "#fd7e14",
    padding: 15,
    borderRadius: 8,
    alignItems: "center",
    marginTop: 30,
    marginBottom: 50,
    elevation: 3,
  },
  buttonText: {
    color: "white",
    fontWeight: "bold",
    fontSize: 16,
  },
});
