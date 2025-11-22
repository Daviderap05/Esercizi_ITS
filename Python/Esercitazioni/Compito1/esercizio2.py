frase: str = input("Inserire una frase: ")
count: int = 0

for i in range(len(frase)):
    
    if frase[i] == " ":
        
        count += 1

print(f"Il numero di spazi è: {count}")