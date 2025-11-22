nome = input("Inserisci il tuo nome: ")
genere = input("Inserisci il tuo genere (m per maschio, f per femmina): ")

match genere.lower():
    
    case "m":
        
        print(f"Nome: {nome}\nGenere: Maschio")
        
    case "f":
        
        print(f"Nome: {nome}\nGenere: Femmina")
        
    case _:
        
        print("Errore: genere non valido. Non è possibile generare un documento di identità.")