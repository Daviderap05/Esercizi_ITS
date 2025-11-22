posti_max: int = int(input("Inserire il numero massimo di posti disponibili nel parcheggio: "))
posti_liberi: int = posti_max
opzione: str = ""

while opzione != "4":
    
    print("1 --> Ingresso")
    print("2 --> Uscita")
    print("3 --> Stato")
    print("4 --> esci dal programma")
    
    print("")
    
    opzione: str = str(input("scegliere il numero dell'operazione da effettuare: "))
    
    print("")


    match opzione:
        case "1":
            
            if posti_liberi > 0:
                posti_liberi -= 1
            else:
                print("Il parcheggio è pieno")
                print("")
        case "2":
            
            if posti_liberi < posti_max:
                posti_liberi += 1
            else:
                print("Il parcheggio è già vuoto")
                print("")
        case "3":
            
            print(f"I posti liberi sono {posti_liberi}")
            print(f"I posti occupati sono {posti_max - posti_liberi}")
            print("")
            
        case "4":
            
            print("Addio")
            break
        
        case _:
            
            print("Selezione non valida... riprova")
            print("")
            