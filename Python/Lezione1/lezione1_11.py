posti_liberi: int = 20
opzione: int = 0

while opzione != 4:
    
    print("1 --> prenota un posto ")
    print("2 --> libera un posto")
    print("3 --> visualizza posti occupati e non")
    print("4 --> esci dal programma")
    
    print("")
    
    opzione: int = int(input("scegliere il numero dell'operazione da effettuare: "))
    
    print("")


    match opzione:
        case 1:
            
            if posti_liberi > 0:
                posti_liberi -= 1
            else:
                print("Non ci sono posti disponibili")
                print("")
        case 2:
            
            if posti_liberi < 20:
                posti_liberi += 1
            else:
                print("Tutti i posti sono già disponibili")
                print("")
        case 3:
            
            print(f"I posti liberi sono {posti_liberi}")
            print(f"I posti occupati sono {20 - posti_liberi}")
            print("")
        case 4:
            
            print("Addio")
        case _:
            
            print("Numero non valido... riprova")
            print("")
            