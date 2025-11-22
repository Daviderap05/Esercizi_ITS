def recursivePower(n: int = 3, p: int = 4):
    
    if p == 0:
        
        return 1
    
    else:
        
        return int(n *  recursivePower(n, p - 1))
        
print(recursivePower())