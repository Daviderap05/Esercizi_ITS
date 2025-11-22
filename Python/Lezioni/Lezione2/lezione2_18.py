valore: bool = True 

while valore != False:
    
    try:
        
        lenght: int = int(input("inserisci la lunghezza della lista: "))
        print("")
        
        if lenght <= 0:
            
            print("Errore. inserimento non valido inserire un numero intero positivo")
            print("")
            
        else:
            
            i: int = 0
            lista: list = []
            somma: int = 0
            
            while i != lenght:
            
                try:
                            
                    n: int = int(input(f"Inserisci il {i + 1}° numero intero: "))
                    print("")
                            
                    if n <= 0:
                    
                        print("Errore. inserimento non valido inserire un numero intero positivo")
                        print("")
                            
                    else: 
                            
                        lista.append(n)
                        somma += n
                        i += 1
                                
                except ValueError:
                
                    print("")
                    print("Errore. inserimento non valido inserire un numero intero")
                    print("")
                    
            if i == lenght:
                
                valore = False
                
    except ValueError:
        
        print("")
        print("Errore. inserimento non valido inserire un numero intero")
        print("")
        
media: float = somma / len(lista)
somma_pari: int = 0
somma_dispari: int = 0

for i in lista:
    
    if i % 2 == 0 and i > media:
        
        somma_pari += i
        
    elif i % 2 == 1 or i < media:
        
        somma_dispari += i
        
print(f"La media dei numeri inseriti è: {media}")
print(f"La somma dei numeri pari e superiori della media è: {somma_pari}")
print(f"La somma dei numeri dispari e / o inferiori della media è: {somma_dispari}")
print("")

if somma_pari > somma_dispari:
    
    print("la somma maggiore è quella dei numeri pari e maggiori della media.")
    
else:
    
    print("la somma maggiore è quella dei dispari e / o inferiori della media.")
    