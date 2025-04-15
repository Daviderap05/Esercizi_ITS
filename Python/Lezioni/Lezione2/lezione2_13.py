cont = 1
somma: int = 0
lista: list = []

while cont <= 3:
    
    try:
        
        n: int = int(input(f"Inserisci il {cont}° numero: "))
        print("")
        
        if n <= 0:
            
            print("inserire numeri interi positvi maggiori di 0")
            print("")
        
        else:
            
            lista.append(n)
            somma += n
            cont += 1
    
    except ValueError:
        
        print("")
        print("Inserire solo numeri interi positivi")
        print("")
        
if somma % 2 == 0:
    
    if lista[0] % 3 == 0 and lista[1] % 5 == 0 and lista[2] % 7 == 0:
        
        print("Regole rispettate")

else:
    
    print("Regole non rispettate")
    