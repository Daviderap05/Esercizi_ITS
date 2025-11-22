while True:
    
    try:
        
        x = int(input("Inserire un numero positivo intero: "))
        print("")
            
        break
        
    except ValueError:
        
        print("")
        print("Errore. inserimento non valido reinserire un numero intero")
        print("")
    
if x % 2 == 0 and x > 10:
    
    print("Numero valido")
    
else: 
    
    print("Numero non valido")
    