cont = 1

nome: str = str (input(f"inserisci il {cont}° nome: "))
vendite: int = int (input(f"inserisci il {cont}° totale di vendita: "))

max_nome: str = nome
max_vendite: int = vendite

min_nome: str = nome
min_vendite: int = vendite

while cont <= 20:
    new_nome: str = str (input(f"inserisci il {cont}° nome: "))
    new_vendite: int = int (input(f"inserisci il {cont}° totale di vendita: "))
    
    if new_vendite > max_vendite:
        max_nome = new_nome
        max_vendite = new_vendite
        
    elif new_vendite < min_vendite:
        min_nome = new_nome
        min_vendite = new_vendite
        
    cont += 1

print (f"Il/la venditore/ venditrice: {max_nome} ha il totale di vendita maggiore e si ammonta a: {max_vendite}")
print (f"Il/la venditore/ venditrice: {min_nome} ha il totale di vendita minore e si ammonta a: {min_nome}")

