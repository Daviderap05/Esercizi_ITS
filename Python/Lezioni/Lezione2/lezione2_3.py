max_posti: int = 100
opzione: str = ""

nome_corso: str = str(input("Inserire il nome del corso: "))

print("")

while opzione != "5":
    
    print("1 --> Iscrivi")
    print("2 --> Annulla")
    print("3 --> Visualizza")
    print("4 --> elimina")
    print("5 --> esci dal programma")
    
    print("")
    
    opzione: str = str(input("scegliere il numero dell'operazione da effettuare: "))
    
    print("")


    match opzione:
        
        case "1":
            
            if max_posti > 0:
                max_posti -= 1
            else:
                print("Non ci sono posti disponibili")
                print("")
        
        case "2":
            
            if max_posti < 100:
                max_posti += 1
            else:
                print("Tutti i posti sono già disponibili")
                print("")
        
        case "3":
            
            print(f"I posti liberi sono {max_posti}")
            print(f"I posti occupati sono {100 - max_posti}")
            print("")
            
        case "4":
            
            nome_corso: str = str(input(f"Corso {nome_corso} eliminato. Inserire il nome del nuovo corso: "))
            max_posti = 100
            print("")
        
        case "5":
            
            print("Addio")
        
        case _:
            
            print("Selezione non valida... riprova")
            print("")
            