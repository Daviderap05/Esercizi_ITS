#ordinare una lista non ordinata senza sort o sorted, creare l'algoritmo

lista_n: list[int] = [2, 7, 6, 3, 9, 12, 1]
lista_o: list[int] = []

for i in range(len(lista_n)):
    
    for j in range(len(lista_n)):
        
        if lista_n[j] - lista_n[i]:
        
