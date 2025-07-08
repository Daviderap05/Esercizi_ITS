nomi: list[str] = []
cont: int = 1

while True:
    
    try:
        nome: str = input(f"Inserisci il {cont}° nome (quando inserirai un ononimo si interromperà): ").capitalize()
        
        if nome == "" or len(nome) > 20 or not nome.isalpha():
            raise ValueError ("Non hai inserito un nome valido (stringa di max 20 caratteri)... riprova.\n")
        
        if nome not in nomi and len(nomi) <= 30:
            nomi.append(nome)
            
        else:
            break
        
        cont += 1
        
    except ValueError as e:
        print (e)
        
        
print(f"\nHai inserito {len(nomi)} nomi distinti.")

nome_len_max = nomi[0]

for nome in nomi:
    if len(nome) > len(nome_len_max):
      nome_len_max = nome

print(f"Il più lungo è {nome_len_max} con {len(nome_len_max)} caratteri.")  