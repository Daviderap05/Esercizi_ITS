pet1: dict[str, str] = {
    "razza": "cane",
    "proprietario": "Alessandro"
}

pet2: dict[str, str] = {
    "razza": "gatto",
    "proprietario": "Bianca"
}

pet3: dict[str, str] = {
    "razza": "coniglio",
    "proprietario": "Carlo"
}

pet4: dict[str, str] = {
    "razza": "pappagallo",
    "proprietario": "Diana"
}

pet5: dict[str, str] = {
    "razza": "criceto",
    "proprietario": "Elena"
}

pets: list[dict[str, str]] = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    
    for key, value in pet.items():
        
        print(f"{key.title()}: {value}")
        
    print("")