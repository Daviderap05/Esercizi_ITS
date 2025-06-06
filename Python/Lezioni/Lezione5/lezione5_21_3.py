people: dict[str : int] = {
    
    "Matteo" : 3, 
    "Gabriele" : 7, 
    "Tommaso" : 12,
    "Davide" : 25
    
}

for key, value in people.items():
    
    print(f"Il numero preferito di {key} è: {value}")