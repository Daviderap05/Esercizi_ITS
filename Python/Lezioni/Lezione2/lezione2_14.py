import random

punteggio: int = 0
    
while punteggio != 100:
    
    d1: int = random.randint(1, 6)
    d2: int = random.randint(1, 6)

    print(f"dado uno = {d1}")
    print("")
    print(f"dado due = {d2}")
    print("")

    somma: int = d1 + d2

    if d1 % 2 == 0 and d2 % 2 == 0 and somma > 8:
        
        punteggio = 100
        print(f"Congratulazione hai vinto. Il tuo punteggio è {punteggio}")
        break
        
    elif d1 == 6 or d2 == 6 or somma == 7:
        
        punteggio += 10
        print("Ottimo risultato il tuo punteggio aumenterà di 10")
        print(f"Il tuo punteggio attuale è {punteggio}")
        print("")
        
    else:
        
        punteggio = 0
        print(f"Che peccato hai perso. Il tuo punteggio è {punteggio}")
        break
        
        