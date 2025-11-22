somma: int = 0
cont: int = 1

while cont <= 5:
    num: int = int (input(f"inserisci il {cont}° numero: "))
    
    if num > 0:
        somma += num
    
    cont += 1

print (f" La somma dei numeri positivi maggiori di 0 è: {somma}")
