i: int = 1
somma: int = 0
lista: list = []
            
while i <= 7:
    
    try:
        
        n: int = int(input(f"Inserisci la temperatura del {i}° giorno: "))
        print("")
        
        somma += n
        lista.append(n)
        
        if n >= 10 and n <= 30:
        
            print("Temperatura nella norma")
            print("")
            
        elif n >= 5 and n <= 35:
    
            print("Prestare attenzione")
            print("")
            
        else:
            
            print("Allerta temperatura")
            print("")
        
        i += 1
        
    except ValueError:
        
        print("")
        print("Errore. inserire una temperatura (no decimali)")
        print("")   

print(f"La media delle temperature è: {round((somma / 7), 2)}°")
print("")

print(f"Il giorno della temperatura più alta è l' / il {(lista.index(max(lista)) + 1)}")
print("")
print(f"Il giorno della temperatura più bassa è l' / il {(lista.index(min(lista)) + 1)}")
