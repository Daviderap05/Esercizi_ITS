a: list[int] = [1, 2, 3, 4]
b: list[int] = [5, 6, 7, 8]
c: list[int] = []

somma: int = 0

for i in range(len(a)):
    
    somma = a[i] + b[len(a) - 1 - i]
    c.append(somma)
    
print(c)