valore: bool = False

num: int = int (input(f"inserisci il numero: "))

if num < 0 and valore == False:
    while valore != True:
        num: int = int (input(f"inserisci solo numeri positivi maggiori di 0: "))
    
        if num > 0:
            valore = True

fattoriale: int = 1

i: int = 1

while i <= num:
    fattoriale *= i
    
    i += 1

print (f"Il fattoriale del numero {num} è: {fattoriale}")
