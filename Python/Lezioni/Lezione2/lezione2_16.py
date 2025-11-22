cont_positivi: int = 0
cont_negativi: int = 0
cont_maggiori: int = 0
cont_minori: int = 0
cont: int = 1

while cont <= 10:
    
    try:
        
        n: int = int(input(f"Inserisci il {cont}° numero intero: "))
        print("")
        
        if n < 0:
            
            cont_negativi += 1
            
            if n % 2 == 1 or n < -10:
                
                cont_minori += 1           
        
        elif n % 2 == 0 and n > 20:
            
            cont_positivi += 1
            cont_maggiori += 1
            
        else:
            
            cont_positivi += 1
            
        cont += 1
        
    except ValueError:
        
        print("")
        print("Errore. inserimento non valido inserire un numero intero")
        print("")
        
print(f"I numeri positivi sono: {cont_positivi}")
print(f"I numeri negativi sono: {cont_negativi}")
print(f"I numeri positivi, pari e maggiori di 20 sono: {cont_maggiori}")
print(f"I numeri negativi, dispari e / o minori di -10 sono: {cont_minori}")
