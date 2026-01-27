import { StatusBar } from "expo-status-bar";
import { useEffect, useState } from "react";
import {
  StyleSheet,
  Text,
  View,
  TextInput,
  Pressable,
  Alert,
} from "react-native";

export default function App() {
  const [nome, setNome] = useState("");
  const [email, setEmail] = useState("");
  const [messaggio, setMessaggio] = useState("");

  const [isValid, setIsValid] = useState(false);

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  function handleClick() {
    if (!nome || !email || !messaggio || !emailRegex.test(email)) {
      Alert.alert("Errore Inserimento dati", "Campi mal formati");
    } else {
      Alert.alert("Inserimento dati completato", "Campi Inviati");
      setNome("");
      setEmail("");
      setMessaggio("");
    }
  }

  useEffect(() => {
    if (nome && emailRegex.test(email) && messaggio) {
      setIsValid(true);
    } else {
      setIsValid(false);
    }
  }, [nome, email, messaggio]);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Contattaci</Text>

      <TextInput
        style={styles.riga}
        placeholder="Nome"
        value={nome}
        onChangeText={(text) => setNome(text)}
      />
      <TextInput
        style={styles.riga}
        placeholder="Email"
        keyboardType="email-address"
        value={email}
        onChangeText={(text) => setEmail(text)}
      />
      <TextInput
        style={[styles.riga, { height: 100 }]}
        placeholder="Messaggio"
        multiline
        value={messaggio}
        onChangeText={(text) => setMessaggio(text)}
      />

      <Pressable
        onPress={handleClick}
        disabled={!isValid}
        style={({ pressed }) => [
          styles.button,
          {
            backgroundColor: isValid
              ? pressed
                ? "#005bb5"
                : "#007AFF"
              : "#999",
          },
        ]}
      >
        <Text style={styles.buttonText}>Invia</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f5f5f5",
    alignItems: "center",
    justifyContent: "center",
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 20,
    color: "#333",
  },
  riga: {
    backgroundColor: "#fff",
    borderWidth: 1,
    borderColor: "#ddd",
    padding: 12,
    borderRadius: 8,
    width: "100%",
    marginBottom: 15,
  },
  button: {
    width: "100%",
    padding: 15,
    borderRadius: 8,
    alignItems: "center",
    marginTop: 10,
  },
  buttonText: {
    color: "#fff",
    fontWeight: "bold",
    fontSize: 16,
  },
});
