check: bool = False

while check != True:
    
    try:
        
        giorno:int = int(input("Inserisci il giorno: "))
        mese:int = int(input("Inserisci il mese: "))
        
        if 0 < giorno <= 31 and 0 < mese <= 12:
        
            if mese == 2 and not 0 < giorno <= 28:
            
                print("Febbraio ha solo 28 giorni... riprova\n")
                
                continue
                
            check = True
                
        else:
            
            print("Inserire un giorno e mese valido mediante un numero\n")
            
        
    except ValueError:
        
        print("Inserire un giorno e mese valido mediante un numero\n")
        
data: tuple = (giorno, mese)

print("")

match data:
    
    case (1, 1):
        
        print("Il 1/1 è capodanno!")
        
    case (14, 2):
        
        print("Il 14/2 è San Valentino!")
        
    case (2, 6):
        
        print("Il 2/6 è la festa della Repubblica Italiana!")
        
    case (15, 8):
        
        print("Il 15/8 è Ferragosto!")
        
    case (31, 10):
        
        print("Il 31/10 è Halloween!")
        
    case (25, 12):
        
        print("Il 25/12 è Natale!")
        
    case _:
        
        print("Nessuna festività importante in questa data.")