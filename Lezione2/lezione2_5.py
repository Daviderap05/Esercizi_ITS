while True:
    
    try:
        
        num = int(input("Inserire un numero intero maggiore di 0: "))
        print("")
        
        if num <= 0:
            
            print("Errore. inserire un numero intero positivo")
            print("")
            
        else:
            
            break
        
    except ValueError:
        
        print("Errore. inserire un numero intero positivo")
        print("")

somma: int = 0

for i in range(num + 1):
    somma += i * i
    
print (f"La somma di tutti i numeri al quadrato di {num} compreso lo stesso è: {somma}")
