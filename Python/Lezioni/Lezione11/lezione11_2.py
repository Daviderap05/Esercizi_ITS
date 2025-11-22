def compoundInterest(m: int, t: int):
    
    if t == 0:
        
        return m
    
    else:
        
        return 1.005 * compoundInterest(m, t - 1)
    
print(compoundInterest(1000, 5))