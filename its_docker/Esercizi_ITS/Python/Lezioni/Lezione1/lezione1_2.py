max: int = int (input("inserisci il 1° numero: "))

cont: int = 2

while cont < 5:
    num: int = int (input(f"inserisci il {cont}° numero: "))
    
    if (num > max):
        max = num
    
    cont += 1

print(f"Il numero massimo è: {max}")
