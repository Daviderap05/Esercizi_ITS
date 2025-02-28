#esercizio preso da lezione6_5
from typing import Any

animal_type: str = ""

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

#inizio dei casi

match nome_animale:
    
    case nome_animale if nome_animale in animali["animal_type" ]["mammiferi"]:
        
        animal_type = "mammiferi"
        print(f"{nome_animale.title()} appartiene alla categoria dei Mammiferi!")
    
    case nome_animale if nome_animale in animali["animal_type" ]["rettili"]:
        
        animal_type = "rettili"        
        print(f"{nome_animale.title()} appartiene alla categoria dei Rettili!")
        
    case nome_animale if nome_animale in animali["animal_type" ]["uccelli"]:
        
        animal_type = "uccelli"
        print(f"{nome_animale.title()} appartiene alla categoria dei Uccelli!")
        
    case nome_animale if nome_animale in animali["animal_type" ]["pesci"]:
        
        animal_type = "pesci"
        print(f"{nome_animale.title()} appartiene alla categoria dei Pesci!")
        
    case _:
        
        print(f"Non so dire in quale categoria classificare l'animale '{nome_animale.title()}'")
        
# match habitat_animale:
    
#     case habitat_animale if animal_type == "uccelli":
        
        