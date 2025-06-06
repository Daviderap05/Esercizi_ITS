count_n: int = 1
count_i: int = 0
numeri: list[float] = []
somma: int = 0

while True:
    
    numero: float = float(input(f"inserire il {count_n}° numero reale positivo: "))
    
    if numero > 0:
        
        numeri.append(numero)
        
        if numero.is_integer():
            
            somma += numero
            count_i += 1
        
    else:
        
        print("")
        break
    
    count_n += 1

print(f"La media dei numeri interi è: {somma / count_i}\n")  
print(f"Il numero maggiore tra quelli inseriti è: {max(numeri)}\n")
print(f"Il numero minore tra quelli inseriti è: {min(numeri)}\n")