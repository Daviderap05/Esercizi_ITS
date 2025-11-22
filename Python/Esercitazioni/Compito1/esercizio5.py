n: float = float(input(f"Inserisci quanti soldi possiedi per le barrette (€1): "))
print("")

if int(n) <= 0:
    
    print(f"Non hai soldi per le barrette")
    
elif int(n) < 6:
    
    print(f"Il numero massimo di barrette acquistabili è {int(n)}")
    print(f"Barrette mancanti per il buono sconto: {6 - int(n)}")

else:
    
    barrette_avanzate: int = 0
    buoni: int = 0

    while True:
        
        if int(n) % 6 == 0:
            
            buoni = int(n) / 6
            break
        
        else:
            
            n -= 1
            barrette_avanzate += 1
    
    print(f"Il numero massimo di barrette acquistabili (con i buoni) è {int(n + buoni + barrette_avanzate)}")
    print(f"I buoni sconto che avanzano sono: {barrette_avanzate}")