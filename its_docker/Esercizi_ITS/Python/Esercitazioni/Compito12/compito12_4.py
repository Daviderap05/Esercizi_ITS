nomi: list[str] = []
cont: int = 0

while True:
    
    try:
        nome: str = input(f"Inserisci il {cont + 1}° nome (quando inserirai un ononimo si interromperà): ").capitalize()
        
        if nome == "" or len(nome) > 20:
            raise ValueError ("Non hai inserito un nome valido (stringa di max 20 caratteri)... riprova.\n")
        
        if nome not in nomi or len(nomi) <= 30:
            nomi.append(nome)
            
        else:
            break
        
    except ValueError as e:
        print (e)
        
        
print(f"Hai inserito {len(nomi)} nomi distinti.")

nome_len_max = nomi[0]

for nome in nomi:
    if len(nome) > len(stringa_piu_lunga):
      stringa_piu_lunga = nome

print(f"Il più lungo è {nome_len_max} con {len(nome_len_max)} caratteri.")  