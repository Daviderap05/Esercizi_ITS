def s2N (s: str):
    base: int = 1
    n: int = 0
    
    for c in s:
        n = n + base * ord(c)
        base *= 256
        # n = n << 8
        # n = n | ord(c)
        
    
    return n

msg: str = "ciao"
print(s2N(msg))

print((2**2)**3)
print((2**3)**2)