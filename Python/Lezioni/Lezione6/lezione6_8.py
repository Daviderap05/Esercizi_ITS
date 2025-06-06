#esercizio preso da lezione6_5
from typing import Any

#variabile per contenere la categoria dell'animale scelto

animal_type: str

#dizionario delle categorie animali e dei vari habitat

animali: dict[str, Any] = {
    
    "categoria" : {
        
        "mammiferi" : ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"],
        
        "rettili" : ["serpente", "lucertola", "tartaruga", "coccodrillo"],
        
        "uccelli" : ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"],
        
        "pesci" : ["squalo", "trota", "salmone", "carpa"]

    },
    
    "habitat" : ["acqua", "aria", "terra"]
    
}

#input per inserire il nome dell'animale

nome_animale: str = input("Digita il nome di un animale: ").lower()

#inserimento del possibile habitat dell'animale

habitat_animale: str = input(f"Digita l'habitat in cui vive l'animale '{nome_animale}': ").lower()

#separazione tra input e output

print("")

#inizio dei casi per il nome

match nome_animale:
    
    #mammiferi
    
    case nome_animale if nome_animale in animali["categoria"]["mammiferi"]:
        
        animal_type = "mammiferi"
        print(f"{nome_animale.title()} appartiene alla categoria dei mammiferi!")
    
    #rettili
    
    case nome_animale if nome_animale in animali["categoria"]["rettili"]:
        
        animal_type = "rettili"        
        print(f"{nome_animale.title()} appartiene alla categoria dei rettili!")
    
    #uccelli
    
    case nome_animale if nome_animale in animali["categoria"]["uccelli"]:
        
        animal_type = "uccelli"
        print(f"{nome_animale.title()} appartiene alla categoria degli uccelli!")
    
    #pesci
    
    case nome_animale if nome_animale in animali["categoria"]["pesci"]:
        
        animal_type = "pesci"
        print(f"{nome_animale.title()} appartiene alla categoria dei pesci!")
    
    #default
    
    case _:
        
        animal_type = "unknown"
        print(f"Non so dire in quale categoria classificare l'animale '{nome_animale}'")

#creazione dizionario per contenere le informazioni delle scelte fatte fino a questo momento

scelte: dict[str, str] = {
    
    "nome_animale" : nome_animale,
    
    "animal_type" : animal_type,
    
    "habitat_animale" : habitat_animale
    
}

#inizio dei casi per l'habitat

match scelte:
    
    #mammiferi
    
    case {"nome_animale" : nome_animale, "animal_type" : "mammiferi", "habitat_animale" : "terra"} if nome_animale not in animali["categoria"]["mammiferi"][-2 : ]:

        print(f"L'animale '{nome_animale}' è uno dei {animal_type} che può vivere sulla {habitat_animale}!")       
        
    case {"nome_animale" : nome_animale, "animal_type" : "mammiferi", "habitat_animale" : "acqua"} if nome_animale in animali["categoria"]["mammiferi"][-2 : ]:
        
        print(f"L'animale '{nome_animale}' è uno dei {animal_type} che può vivere in {habitat_animale}!")
        
    case {"nome_animale" : nome_animale, "animal_type" : "mammiferi", "habitat_animale" : habitat_animale} if habitat_animale in animali["habitat"]:
        
        print(f"Non ho mai visto l'animale '{nome_animale}' vivere nell'habitat '{habitat_animale}'")
    
    #rettili
    
    case {"nome_animale" : nome_animale, "animal_type" : "rettili", "habitat_animale" : "terra"}:

        print(f"L'animale '{nome_animale}' è uno dei {animal_type} che può vivere sulla {habitat_animale}!")
        
    case {"nome_animale" : nome_animale, "animal_type" : "rettili", "habitat_animale" : "acqua"} if nome_animale in animali["categoria"]["rettili"][-1]:

        print(f"L'animale '{nome_animale}' è uno dei {animal_type} che può vivere in {habitat_animale}!")
        
    case {"nome_animale" : nome_animale, "animal_type" : "rettili", "habitat_animale" : habitat_animale} if habitat_animale in animali["habitat"]:

        print(f"Non ho mai visto l'animale '{nome_animale}' vivere nell'habitat '{habitat_animale}'")
    
    #pesci
    
    case {"nome_animale" : nome_animale, "animal_type" : "pesci", "habitat_animale" : "acqua"}:

        print(f"L'animale '{nome_animale}' è uno dei {animal_type} che può vivere in {habitat_animale}!")
        
    case {"nome_animale" : nome_animale, "animal_type" : "pesci", "habitat_animale" : habitat_animale} if habitat_animale in animali["habitat"]:

        print(f"Non ho mai visto l'animale '{nome_animale}' vivere nell'habitat '{habitat_animale}'")
    
    #uccelli
    
    case {"nome_animale" : nome_animale, "animal_type" : "uccelli", "habitat_animale" : "aria"} if nome_animale in animali["categoria"]["uccelli"][ : 4]:

        print(f"L'animale '{nome_animale}' è uno degli {animal_type} che può vivere in {habitat_animale}!")
        
    case {"nome_animale" : nome_animale, "animal_type" : "uccelli", "habitat_animale" : "terra"} if nome_animale in animali["categoria"]["uccelli"][-4 : ]:

        print(f"L'animale '{nome_animale}' è uno degli {animal_type} che può vivere sulla {habitat_animale}!")
        
    case {"nome_animale" : nome_animale, "animal_type" : "uccelli", "habitat_animale" : "acqua"} if nome_animale in animali["categoria"]["uccelli"][4 : 6]:

        print(f"L'animale '{nome_animale}' è uno degli {animal_type} che può vivere sull'{habitat_animale}!")
        
    case {"nome_animale" : nome_animale, "animal_type" : "uccelli", "habitat_animale" : habitat_animale} if habitat_animale in animali["habitat"]:

        print(f"Non ho mai visto l'animale '{nome_animale}' vivere nell'habitat '{habitat_animale}'")
    
    #default
    
    case _:
        
        print(f"Non sono in grado di fornire informazioni sull'habitat '{habitat_animale}'")