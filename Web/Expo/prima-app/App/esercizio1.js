import { useState } from "react";
import {
  Button,
  FlatList,
  Modal,
  StyleSheet,
  Text,
  TextInput,
  View,
} from "react-native";

export default function App() {
  const [messaggio, setMessaggio] = useState("Ciao");
  const [visible, setVisible] = useState(false);
  const [nome, setNome] = useState("");
  const [openModal, setOpenModal] = useState(false);
  const [contatore, setContatore] = useState(0);
  const [num1, setNum1] = useState(0);
  const [num2, setNum2] = useState(0);

  const dati = [
    { id: "1", nome: "Mario" },
    { id: "2", nome: "Rob" },
    { id: "3", nome: "Gino" },
  ];
  return (
    <View style={styles.container}>
      <Text>{nome}</Text>
      {visible && <Text>{messaggio}</Text>}
      <TextInput
        placeholder="Inserisci testo"
        onChangeText={setNome}
        style={styles.inputText}
        value={nome}
      ></TextInput>
      <Button
        title="Cambia testo"
        onPress={() => setMessaggio("Ho premuto il pulsante")}
      />
      <Button
        title={visible ? "Nascondi" : "Visualizza"}
        onPress={() => setVisible(!visible)}
      />
      <View style={styles.containerList}>
        <FlatList
          data={dati}
          renderItem={(dato) => <Text>{dato.item.nome}</Text>}
          keyExtractor={(item) => item.id}
        />
      </View>
      <View>
        <Button title="Apri" onPress={() => setOpenModal(true)}></Button>
        <Modal visible={openModal} animationType="slide">
          <View>
            <Text>Sono una moda</Text>
            <Button title="Chiudi" onPress={() => setOpenModal(false)}></Button>
          </View>
        </Modal>
      </View>
      <View>
        <Text>Contatore: {contatore}</Text>
        <Button
          title="Incrementa"
          onPress={() => setContatore(contatore + 1)}
        ></Button>
        <Button
          title="Diminuisci"
          onPress={() => setContatore(contatore - 1)}
        ></Button>
      </View>
      <View>
        <TextInput
          style={styles.inputText}
          inputMode="numeric"
          placeholder="Inserisci num1"
          onChangeText={setNum1}
          value={num1}
        ></TextInput>
        <TextInput
          style={styles.inputText}
          inputMode="numeric"
          placeholder="Inserisci num2:"
          onChangeText={setNum2}
          value={num2}
        ></TextInput>
        <Text>La somma è: {parseInt(num1) + parseInt(num2)}</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
    paddingHorizontal: 46,
    padding: 50,
  },
  containerList: {
    flex: 3,
    backgroundColor: "#fff",
    alignItems: "center",
    justifyContent: "center",
  },
  inputText: {
    borderWidth: 1,
    padding: 10,
  },
});
