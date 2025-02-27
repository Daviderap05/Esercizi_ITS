nome: str = input("Inserire il nome: ")

eta: int = int(input("Inserire l'età: "))

ruolo: str = (input("Inserire il ruolo: "))

persona: dict[str : str and int] = {"nome" : nome, "eta" : eta, "ruolo" : ruolo}

match persona: 
    
    case 1:
        
        print("Acesso completo a tutte le funzionalità.")
        
    case _:
        
        print("")