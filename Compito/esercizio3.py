frase: str = input("Inserire una frase: ")
frase_invertita: str = ""

for i in range(len(frase) - 1, -1, -1):
    
    frase_invertita += frase[i]

print(f"La stringa inverita è: {frase_invertita}")