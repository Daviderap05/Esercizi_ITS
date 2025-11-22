def ricerca_binaria(num: int, lista_n: list[int] = []) -> None|str:
    
    if num is None or not isinstance(num, int):
        
        raise ValueError("Errore... Inserire un numero intero da cercare.")
    
    if lista_n == []:
        
        raise ValueError("Errore... la lista di numeri è vuota o non inserita.")
    
    if len(lista_n) == 1:
        
        if num == lista_n[0]:
            
            return f"Il numero {num} è presente nella lista."
        
        else:
            
            return f"Il numero {num} non è presente nella lista."
        
    lista_n.sort()   
    i_max: int = len(lista_n)-1
    i_min: int = 0
    i_centro: int = 0
    
    while lista_n[i_centro] != num:
        
        i_centro: int = int((i_max + i_min)/2)  #va bene anche la divisione intera //
        
        if lista_n[i_centro] == num:
            
            return f"Il numero {num} è presente nella lista."
        
        elif (i_max - i_min) == 2:  
            
            if lista_n[i_centro + 1] == num:
            
                return f"Il numero {num} è presente nella lista." 
            
            else:
                
                return f"Il numero {num} non è presente nella lista."
        
        elif lista_n[i_centro] < num:
            
            i_min = i_centro
            
        else:
            
            i_max = i_centro
            
        
        
lista1: list[int] = [15, 3, 8, 20, 1, 12, 7, 18, 5, 10, 2, 14, 6, 19, 4, 11, 9, 17, 13, 16]
print(ricerca_binaria(2, lista1))