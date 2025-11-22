import math

def safe_sqrt(number: int):
    
    try:
    
        print(math.sqrt(number))

    except ValueError:
        
        print("\nERRORE... inserimento numero negativo")
    
    
try:
    
    n: int = int(input("Inserisci un numero positivo: "))

except ValueError:
    
    print("\nERRORE... inserimento valore non valido")
    
else:
    
    safe_sqrt(n)