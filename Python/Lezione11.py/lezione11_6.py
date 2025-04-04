def produttoria(pi: int):
    
    if pi == 0:
        
        return (pi + 2)
    
    else:
        
        return (pi + 2) * produttoria(pi - 1)
    
print(produttoria(7))