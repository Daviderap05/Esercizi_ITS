import math

a: float = float (input(f"Inserisci la misura dell'ipotenusa: "))
b: float = float (input(f"inserisci la misura del cateto minore: "))

if a > b:
    c: float = float (math.sqrt(((a ** a) - (b ** b))))
    print(f"la misura del cateto maggiore è: {c}")
else:
    print("ERRORE")  