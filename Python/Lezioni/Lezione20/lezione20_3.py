#ordinare una lista non ordinata senza sort o sorted, creare l'algoritmo

lista_n: list[int] = [15, 3, 8, 20, 1, 12, 7, 18, 5, 10, 2, 14, 6, 19, 4, 11, 9, 17, 13, 16]
temp: int = 0

for i in range(len(lista_n)):
    
    for j in range(len(lista_n)):
        
        if lista_n[j] > lista_n[i]:
        
            temp = lista_n[i]
            lista_n[i] = lista_n[j]
            lista_n[j] = temp
            
print(lista_n)

#corretto 

for i in range(len(lista_n)):
    
    for j in range(len(lista_n) - 1 - i):  # Confronta solo elementi adiacenti
        
        if lista_n[j] > lista_n[j + 1]:  # Se l'elemento corrente è maggiore del successivo
            
            # Scambia gli elementi
            lista_n[j], lista_n[j + 1] = lista_n[j + 1], lista_n[j]

print(lista_n)