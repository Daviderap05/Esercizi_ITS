# def cars(casa: str, modello: str, **info)   ->  dict:     commentato per l'esercizio successivo
    
#     dictionary: dict = {"casa": casa, "modello" : modello}
    
#     for key, value in info.items():
        
#         dictionary[key] = value
        
#     return dictionary

from lezione8_15 import cars

print(cars('subaru', 'outback', color = 'blue', tow_package = True))