import sys

while True:
    
    try:
        
        n: int = int(input("Inserisci un valore intero positivo maggiore di 0: "))
        print("")
        
        if n < 0:
            
            print("Errore. inserimento di un numero negativo")
            sys.exit()
        
        elif n == 0:
            
            print("Errore. Lo zero non è inseribile")
            print("")
            
        else:
            
            break
        
    except ValueError:
        
        print("")
        print("Errore. inserimento non valido inserire un numero positivo intero")
        print("")

ris: int = 1

if n % 2 == 0:

    for i in range(n + 1):
        
        if i % 4 == 0:
            
            ris += i
    
    print(f"La somma dei numeri è: {ris - 1}")

else:
    
    for i in range(n + 1):
        
        if i % 2 == 1:
            
            ris *= i
    
    print(f"Il prodotto tra i numeri è: {ris}")
    