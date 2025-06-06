età: int = int(input("Inserisci la tua età: "))

if età >= 18 and età <= 65:

    print("Puoi partecipare all'attività")

elif età < 18:
    
    print("Non puoi partecipare all'attività perché non hai raggiuto l'età minima richiesta")
    
else:
    
    print("Non puoi partecipare all'attività perché non hai raggiuto l'età massima richiesta")
    