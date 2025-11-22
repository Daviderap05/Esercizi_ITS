while True:
    
    try:
        
        x = int(input("Inserire un numero positivo intero: "))
        print("")
        
        if x < 0:
            
            print("Errore. inserimento di un numero negativo")
            print("")
        
        elif x == 0:
            
            print("Errore. Lo zero non è inseribile")
            print("")
            
        else:
            
            break
        
    except ValueError:
        
        print("")
        print("Errore. inserimento non valido reinserire un numero positivo intero")
        print("")
    
somma: int = 0
cont: int = 0
    
for i in range (10):
    
    while True:
        
        try:
            
            n = int(input(f"Inserire il {i + 1}° numero: "))
            
            if n % 1 == 1:
            
                print("Errore. inserire un numero intero")
                print("")
                
                break
            
            elif x % n == 0:
            
                cont += 1
                
                break
                
            else:
                
                break
        
        except ValueError as e:
            
            print("")
            print("Errore. inserire un numero intero")
            print("")
            #print(f"{e}")                

print("")  
print(f"Il conteggio dei numeri divisibili per {x} è: {cont}")              
