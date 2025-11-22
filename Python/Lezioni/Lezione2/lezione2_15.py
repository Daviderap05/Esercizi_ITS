while True:
    
    try:
        
        n: int = int(input("Inserisci un valore intero positivo maggiore di 0: "))
        print("")
        
        if n < 0:
            
            print("Errore. inserimento di un numero negativo")
            print("")
        
        elif n == 0:
            
            print("Errore. Lo zero non è inseribile")
            print("")
            
        else:
            
            break
        
    except ValueError:
        
        print("")
        print("Errore. inserimento non valido inserire un numero positivo intero")
        print("")

somma: int = 0 

if n > 0 and n <= 100:
    
    for i in range(n + 1): 
        
        if i % 2 == 0:
            
            somma += i
    
else:
    
    for i in range(n + 1):
        
        if i % 2 == 1:
            
            somma += i

print(f"La somma dei numeri è: {somma}")

