sequenza_n: list[int] = []
cont: int = 0
prima_x: int = 0
i_seconda_x: int = 0
somma: int = 0

while True:
    
    try:
        
        x: int = int(input("Inserire un numero intero positivo, il primo sarà il valore x (0 interrompe): "))    
    
        print("")
        
        if x < 0:
            
            print("Errore. inserire un numero intero positivo")
            print("")
            
        if cont == 0:
            
            prima_x = x
            cont += 1
            continue  
        
        sequenza_n.append(x)
        
        if x == 0:
            
            print("; ".join(map(str, sequenza_n)))
            break
        
        if x == prima_x:
            
            if cont == 1:
                
                i_seconda_x = len(sequenza_n)-1
                cont += 1
            
        else:
            
            somma += x
        
    except ValueError:
        
        print("Errore. inserire un numero intero positivo")
        print("")

             
print(f"Il numero {prima_x} compare {sequenza_n.count(prima_x)} {'volta' if sequenza_n.count(prima_x) == 1 else 'volte'} nella sequenza")
print(f"Il numero {prima_x} compare per la prima volta in posizione {i_seconda_x} nella sequenza")
print(f"La somma dei valori della sequenza diversi da {prima_x} è {somma}")