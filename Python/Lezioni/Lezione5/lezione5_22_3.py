glossary: dict[str, str] = {
    "variabile": "Una variabile è un nome che rappresenta un valore memorizzato in memoria.",
    "funzione": "Una funzione è un blocco di codice che esegue un'operazione specifica e può essere richiamato quando necessario.",
    "loop": "Un loop è una struttura di controllo che permette di eseguire ripetutamente un blocco di codice.",
    "dizionario": "Un dizionario è una struttura dati che memorizza coppie chiave-valore.",
    "lista": "Una lista è una collezione ordinata di elementi che può contenere valori duplicati."
}
for word, meaning in glossary.items():
    
    print(f"{word.title()}: {meaning}\n")