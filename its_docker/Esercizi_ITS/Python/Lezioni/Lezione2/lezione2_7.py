cont: int = 0
somma: int = 0
media: float = 0
opzione: str = ""

print ("Inserimento di voti per il calcolo della media")
print("")

while True:

    opzione: str = input("Proseguire? y  / n: ")
    print("")
    
    match opzione:
        
        case "y":
            
            while True:
                
                try:
                    
                    voto: int = int(input(f"Inserire il {cont + 1}° voto: "))
                    print("")
                    
                    if voto > 0:
                            
                        cont += 1
                        somma += voto
                            
                        break
                            
                    else:
                        
                        print("Voto non valido... reinserire")
                        print("")
                            
                except ValueError:
                    
                    print("")
                    print("Errore. inserire un numero")
                    print("")
                    
        case "n":
                
                if cont == 0:
                    
                    print("Addio")
                    break
                    
                else:
                    
                    media = somma / cont
                    print(f"La media è: {media}")
                    print("")
                    break
            
        case _:
            
            print("Inserire SOLO y / n")
            print("")
            
print(f"Il voto arrotondato è: {round(media, 0)}")
