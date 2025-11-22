def recursiveFactorial(n: int):
    
    if n == 0:
        
        return 1
    
    elif n == 1:
        
        return n
    
    else:
        
        return n * recursiveFactorial(n - 1)
    
print(recursiveFactorial(1))