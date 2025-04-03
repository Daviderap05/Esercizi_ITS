lista_n: list[int] = []
prodotto: int = 1

n1: int = int(input("Inserire primo numero: "))
lista_n.append(n1)

n2: int = int(input("Inserire secondo numero: "))
lista_n.append(n2)

for i in range (min(lista_n), max(lista_n) + 1):
    
    prodotto *= i
    
print(f"Il prodotto tra i numeri inseriti è: {prodotto}")