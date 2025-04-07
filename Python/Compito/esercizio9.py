pi: float = 4.0
count: int = 0
denominatore: int = 3
segno: int = -1

while abs(pi - 3.14) > 0.01:
    
    pi += segno * (4 / denominatore)
    denominatore += 2
    segno *= -1
    count += 1

print(f"Termini necessari per ottenere il valore di π ≈ 3.14: {count}")

pi: float = 4.0
count = 0
denominatore = 3
segno = -1

while abs(pi - 3.141) > 0.001:
    
    pi += segno * (4 / denominatore)
    denominatore += 2
    segno *= -1
    count += 1

print(f"Termini necessari per ottenere il valore di π ≈ 3.141: {count}")

pi: float = 4.0
count = 0
denominatore = 3
segno = -1

while abs(pi - 3.1415) > 0.0001:
    
    pi += segno * (4 / denominatore)
    denominatore += 2
    segno *= -1
    count += 1

print(f"Termini necessari per ottenere il valore di π ≈ 3.1415: {count}")

pi: float = 4.0
count = 0
denominatore = 3
segno = -1

while abs(pi - 3.14159) > 0.00001:
    
    pi += segno * (4 / denominatore)
    denominatore += 2
    segno *= -1
    count += 1

print(f"Termini necessari per ottenere il valore di π ≈ 3.14159: {count}")