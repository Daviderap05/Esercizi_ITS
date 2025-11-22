while True:
    
    try:
        
        n: int = int(input("Inserisci quante volte vuoi inserire x e y: "))
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
    

for i in range(n):
    
    while True:
    
        try:
            
            x: int = int(input("Inserisci x: "))
            y: int = int(input("Inserisci y: "))
            print("")
            
            if x > 0 and y > 0:
                
                print(f"Il prodotto di x e y è: {x * y}")
                print("")
            
            elif  x < 0 and y < 0:
                
                print("Errore.")
                
            else:
                
                print(f"La sottrazione tra x e y è: {x - y}")
            
            break
            
        except ValueError:
            
            print("")
            print("Errore. inserimento non valido inserire un numero positivo intero")
            print("")
            