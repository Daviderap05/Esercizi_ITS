def produttoria(pi: int):
    
    if pi == 1:
        
        return (pi ** 3)
    
    else:
        
        return (pi ** 3) * produttoria(pi - 1)
    
print(produttoria(5))