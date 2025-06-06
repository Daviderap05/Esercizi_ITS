pari: int = 0
dispari: int = 0
cont: int = 1

while cont <= 10:
    num: int = int (input(f"inserisci il {cont}° numero: "))
    
    if num % 2 == 0:
        pari += 1
    else:
        dispari += 1
    
    cont += 1

print(f"I numeri pari sono: {pari}")
print(f"I numeri dispari sono: {dispari}")

