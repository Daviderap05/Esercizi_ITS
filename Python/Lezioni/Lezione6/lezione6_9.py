#Inizializzazione la lista dei risultatie e la variabile contatore

lista_risultati: list[str] = []

#Ciclo per far inserire i valori t o c

while len(lista_risultati) < 8:
    
    risultato: str = input(f"Lancio {len(lista_risultati) + 1}: ").lower()
    
    match risultato:
        
        case "c":
            
            lista_risultati.append(risultato)
            
        case "t":
            
            lista_risultati.append(risultato)
            
        case _:
            
            print("Inserimento non valido. Inserire solo 'c' / 'C' o 't' / 'T'\n")
            
print("")

#output probabilità testa

print(f"Totale 'testa': {lista_risultati.count('t')}")

print(f"Percentuale 'testa': {((lista_risultati.count('t') / 8) * 100):.2f}%\n")

#output probabilità croce

print(f"Totale 'croce': {lista_risultati.count('c')}")

print(f"Percentuale 'croce': {((lista_risultati.count('c') / 8) * 100):.2f}%")