def cars(casa: str, modello: str, **info)   ->  dict:
    
    dictionary: dict = {"casa": casa, "modello" : modello}
    
    for key, value in info.items():
        
        dictionary[key] = value
        
    return dictionary