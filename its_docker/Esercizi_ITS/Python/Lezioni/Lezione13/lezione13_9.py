def moltiplicatore(n: int):
    
    return lambda x: x * n

per_due = moltiplicatore(2)
print(per_due(10))