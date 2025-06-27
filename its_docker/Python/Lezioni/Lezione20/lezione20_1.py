from matplotlib import pyplot as plt

def collatz(n: float)   -> list[float]:
    
    numeri: list[float] = [n]
    
    while n != 1:
        
        if n % 2 == 0:
            
            n /= 2
            
        else:
            
            n = (3 * n) + 1
            
        numeri.append(n)
        
    return numeri
            
numeri:list[float] = collatz(24)

plt.plot(numeri)
plt.show()