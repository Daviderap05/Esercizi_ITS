#parte iniziale presa dal precedente

lista: list[str] = ["admin", "Jaden", "Davide"]
#lista.clear()  utilizzo della funzione clear per eliminare tutto dalla lista

if lista:   #if per capire se la lista è vuota o meno
    
    for i in lista:
        
        if i == "admin":
            
            print("Ciao " + i + " vuoi un rapporto sullo stato?")
            
        else:
            
            print(f"ciao {i}, grazie per esserti collegato")
            
else:
    
    print("Abbiamo bisogno di nuovi utenti")