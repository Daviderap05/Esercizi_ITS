soglia: int = int (input("inserisci la soglia massima: "))

cont: int = 1
lista: list = []

while cont <= 7:
    num: int = int (input(f"inserisci il {cont}°: "))
    
    if num > soglia:
        lista.append(num)
    
    cont += 1

if lista:
    print(f"I numeri che superano la soglia sono: {lista}")
else:
    print("non ci sono numeri che superano la soglia")
    