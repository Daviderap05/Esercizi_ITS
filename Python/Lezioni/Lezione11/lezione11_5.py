def armonica(n: int):
    
    if n == 1:
        
        return 1
    
    else:
        
        return (1 / n) * armonica(n - 1)

print(round(armonica(6), 6))