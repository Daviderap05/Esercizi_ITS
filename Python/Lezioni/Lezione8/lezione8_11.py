def send_messages(lista: list):
    
    list2: list = []
    
    print(", ".join(lista))
    
    for i in lista:
        
        list2.append(i)
        
    print(*list2, sep=", ", end=" ")

lista: list[str] = ["Ciao", "come", "stai"]

# Chiamare la funzione con una copia della lista
send_messages(lista[:])

# Stampare entrambe le liste per mostrare che la lista originale ha mantenuto i suoi messaggi
print("\nLista originale:", lista)
print("Lista modificata:", lista[:])