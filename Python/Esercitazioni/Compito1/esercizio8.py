lista_n: list[int] = []
count: int = 1

while len(lista_n) <= 4:
    
    try:
        
        n: int = int(input(f"Inserire il {count}° numero: "))
        
        if n >= 1 and n <= 30:
            
            lista_n.append(n)
            count += 1
            
        else:
            
            print("Il numero inserio non è compreso tra 1 e 30... riprovare\n")
            
    except ValueError:
        
        print("Inserimento non valido inserire numeri interi compresi tra 1 e 30\n")

for i in range(len(lista_n)):
            
    print("")
            
    for j in range(lista_n[i]):
                
        print("*", end = "")