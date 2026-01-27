import { useState } from "react";
import { StyleSheet, Text, View, FlatList, Pressable } from "react-native";

export default function App() {
  const [products, setProducts] = useState([]);

  const PRODUCTS = [
    { id: "p1", name: "Olio Motore 5W-30", price: 19.9 },
    { id: "p2", name: "Additivo Pulizia Iniettori", price: 14.5 },
    { id: "p3", name: "Liquido Freni DOT4", price: 8.99 },
    { id: "p4", name: "Filtro Aria", price: 12.0 },
    { id: "p5", name: "Trattamento Antiattrito", price: 24.9 },
    { id: "p6", name: "Additivo Pulizia FAP/DPF", price: 21.5 },
    { id: "p7", name: "Olio Cambio Automatico ATF", price: 16.9 },
    { id: "p8", name: "Spray Detergente Freni", price: 6.5 },
  ];

  function handleCarrels(id) {
    if (products.includes(id)) {
      setProducts(products.filter((item) => item !== id));
    } else {
      setProducts([...products, id]);
    }
  }

  const totale = PRODUCTS.reduce((acc, item) => {
    return products.includes(item.id) ? acc + item.price : acc;
  }, 0);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Carrello Ricambi</Text>

      <FlatList
        data={PRODUCTS}
        keyExtractor={(item) => item.id}
        style={styles.list}
        renderItem={({ item }) => {
          
          const isSelected = products.includes(item.id);
          return (
            <Pressable
              onPress={() => handleCarrels(item.id)}
              style={[styles.item, isSelected && styles.itemSelected]}
            >
              <Text style={styles.itemName}>{item.name}</Text>
              <Text style={styles.itemPrice}>{item.price.toFixed(2)} €</Text>
            </Pressable>
          );
        }}
      />

      <View style={styles.footer}>
        <Text style={styles.totalLabel}>Totale Selezione:</Text>
        <Text style={styles.totalValue}>{totale.toFixed(2)} €</Text>

        {products.length > 0 && (
          <Pressable style={styles.clearButton} onPress={() => setProducts([])}>
            <Text style={styles.clearButtonText}>Svuota Selezione</Text>
          </Pressable>
        )}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f5f5f5",
    paddingTop: 60,
    paddingHorizontal: 20,
  },
  title: {
    fontSize: 26,
    fontWeight: "bold",
    marginBottom: 20,
    color: "#333",
    textAlign: "center",
  },
  list: {
    flex: 1,
  },
  item: {
    backgroundColor: "#fff",
    padding: 18,
    marginVertical: 6,
    borderRadius: 12,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    borderWidth: 1,
    borderColor: "#e0e0e0",
    // Ombra per iOS e Android
    elevation: 2,
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 2,
  },
  itemSelected: {
    backgroundColor: "#e3f2fd",
    borderColor: "#2196f3",
    borderWidth: 2,
  },
  itemName: {
    fontSize: 16,
    color: "#444",
    flex: 1,
  },
  itemPrice: {
    fontSize: 16,
    fontWeight: "bold",
    color: "#2e7d32",
  },
  footer: {
    borderTopWidth: 1,
    borderTopColor: "#ddd",
    paddingVertical: 20,
    alignItems: "center",
    backgroundColor: "#f5f5f5",
  },
  totalLabel: {
    fontSize: 16,
    color: "#666",
  },
  totalValue: {
    fontSize: 32,
    fontWeight: "bold",
    color: "#333",
    marginVertical: 5,
  },
  clearButton: {
    marginTop: 10,
    padding: 10,
  },
  clearButtonText: {
    color: "#d32f2f",
    fontWeight: "600",
    textDecorationLine: "underline",
  },
});
