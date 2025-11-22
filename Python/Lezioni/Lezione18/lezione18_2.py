import random

def guess_the_number() -> None:
    
    attempts: int = 10
    choise: int = -1
    
    while True:
        
        try:
            
            a: int = int(input("Inserisci il primo numero: "))
            
            if a < 0:
                
                print("Attenzione... inserire solo numeri interi maggiori o uguali a 0, riprova\n")
                
            else:
                
                break
            
        except ValueError:
            
            print("Attenzione... inserire solo numeri interi maggiori o uguali a 0, riprova\n")
    
    print("")  
    
    while True:
        
        try:
            
            b: int = int(input("Inserisci il secondo numero: "))
                
            if b <= a:
                
                print("Attenzione... il secondo numero deve essere più grande del primo, riprova\n")
            
            else:
                
                break
            
        except ValueError:
            
            print("Attenzione... inserire solo numeri interi e maggiori del primo, riprova\n")
                
    range: int = random.randint(a, b)
        
    print("")  
        
    while True:
        
        try:
            
            choise: int = int(input(f"Indovina il numero nel range scelto ({a}, {b}): "))
            
            if choise < a or choise > b:
                
                print("Attenzione... inserire solo numeri compresi nel range, riprova\n")
                
            elif choise < range:
                
                print("Numero più basso dell'obiettivo, riprova\n")
                attempts -= 1
                
            elif choise > range :
                
                print("Numero più alto dell'obiettivo, riprova\n")
                attempts -= 1
                
            else:
                
                print("\nNumero corretto, hai vinto!")
                break
                
        except ValueError:
            
            print("Attenzione... inserire solo numeri interi compresi nel range, riprova\n")
        
        if attempts > 0:
            
            print(f"Tentativi rimanenti: {attempts}")
            
        else:
            
            print("Hai perso, tentativi esauriti")
            break
        
    print("\nAddio")
                
guess_the_number()            