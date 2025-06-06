from typing import Any

nome: str = input("Digitare nome dell'utente: ").title()    #rende tutte le iniziali maiuscole

ruolo: str = (input("Digitare ruolo dell'utente: ")).capitalize()   #rende solo le iniziali delle stringhe maiuscole

eta: int = int(input("Digitare l'età dell'utente: "))

persona: dict[str, Any] = {"nome" : nome, "eta" : eta, "ruolo" : ruolo}

match persona: 
    
    case {"nome" : nome, "eta" : eta, "ruolo" : "Admin"}:
        
        print("Acesso completo a tutte le funzionalità.")
    
    case {"nome" : nome, "eta" : eta, "ruolo" : "Moderatore"}:
        
        print(f"Salve {persona['nome']}! Può gestire i contenuti ma non modificare le impostazioni.")
        
    case {"nome" : nome, "eta" : eta, "ruolo" : "Utente adulto"} if eta >= 18:
        
        print("Accesso standard a tutti i servizi.")
        
    case {"nome" : nome, "eta" : eta, "ruolo" : "Utente minorenne"} if eta < 18:
        
        print("Accesso limitato! Alcune funzionalità sono bloccate.")
        
    case {"nome" : nome, "eta" : eta, "ruolo" : "Ospite"}:
        
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    
    case _:
        
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")