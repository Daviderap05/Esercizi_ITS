import sympy as sp
from secrets import randbelow

# 1. Genero un numero primo
p = sp.randprime(1, 500)
# 2. Trovo un generatore
g = sp.primitive_root(p)

# 3. Ogni partecipante sceglie la sua chiave privata
a = randbelow(p - 2) + 2
b = randbelow(p - 2) + 2

# 4. Calcolo delle chiavi pubbliche
A_pub = pow(g, a, p)
B_pub = pow(g, b, p)

# 5. Segreto condiviso
sA = pow(B_pub, a, p)
sB = pow(A_pub, b, p)

print(f"p = {p}, g = {g}")
print(f"A_pub = {A_pub}, B_pub = {B_pub}")
print(f"Segreto condiviso A = {sA}, B = {sB}")
print("OK!" if sA == sB else "Errore!")
