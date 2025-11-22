import sys

while True:
    
    try:
        
        x = float(input("Inserire SOLO un numero positivo: "))
        print("")
        
        if x < 0:
            
            print("Errore. inserimento di un numero negativo")
            sys.exit()
        
        elif x == 0:
            
            print ("Errore Numero 0 non valido")
            sys.exit()
            
        else:
            
            break
        
    except ValueError:
        
        print("")
        print("Errore. inserire un numero positivo")
        print("")
    
somma: int = 0
    
for i in range (10):
    
    while True:
        
        try:
            
            n = float(input(f"Inserire il {i + 1}° numero: "))
            
            if x % 2 == 0:
        
                if n > (x / 2):
            
                    somma += n
            
            elif n < x:
        
                somma += n
            
            break
        
        except ValueError as e:
            
            print("")
            print("Errore. inserire un numero positivo o negativo")
            print("")
            #print(f"{e}")                
    
print(f"La somma è: {somma}")
