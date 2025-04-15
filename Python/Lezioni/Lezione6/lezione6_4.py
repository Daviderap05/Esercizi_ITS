oggetti: list[str] = []

for i in range(3):
    
    oggetti.append(input(f"Inserisci il {i + 1}° oggetto: "))

print("")
    
match oggetti:
    
    case _ if "penna" in oggetti and "matita" in oggetti and "quaderno" in oggetti:
        
        print(oggetti)
        print("Materiale scolastico")
        
    case ["pane", "latte", "uova"]:
        
        print(oggetti)
        print("Prodotti alimentari")
        
    case ["sedia", "tavolo", "armadio"]:
        
        print(oggetti)
        print("Mobili")
        
    case ["telefono", "computer", "tablet"]:
        
        print(oggetti)
        print("Dispositivi elettronici")
        
    case _:
        
        print(oggetti)
        print("Categoria sconosciuta")