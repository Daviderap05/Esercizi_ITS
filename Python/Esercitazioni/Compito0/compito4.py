# def transform(x: int) -> int:
#     if x % 2 == 0:
#         return x / 2
#     else:
#         return (x * 3) - 1



# def calcola_stipendio(ore_lavorate: int) -> float:
    
#     if ore_lavorate <= 40:
        
#         return ore_lavorate * 10
    
#     else:
        
#         return 400 + ((ore_lavorate - 40) * 15)



# def print_seq(): 
    
#     print("Sequenza a):")
#     # SCRIVI QUI IL TUO CICLO
#     for i in range(1, 8):
#         print(i)
        
#     print("")

#     print("Sequenza b):")
#     # SCRIVI QUI IL TUO CICLO
#     for i in range(3, 24, 5):
#         print(i)

#     print("")

#     print("Sequenza c):")
#     # SCRIVI QUI IL TUO CICLO
#     for i in range(20, -11, -6):
#         print(i)

#     print("")
    
#     print("Sequenza d):")
#     # SCRIVI QUI IL TUO CICLO
#     for i in range(19, 52, 8):
#         print(i)



# def integerPower(base: int, esponente: int):
    
#     if type(base) == int and (type(esponente) == int) and esponente > 0:
        
#         return base ** esponente


# import math
# def hypotenuse(l1: float, l2: float):
    
#     return float(math.sqrt((l1 ** 2) + (l2 ** 2)))



# def check_access(username: str, password: str, is_active: bool) -> str:
    
#     if username == "admin" and password == "12345" and is_active == True:
        
#         return "Accesso consentito"
    
#     else:
        
#         return "Accesso negato"



# def seconds_since_noon(ore, minuti, secondi):
    
#     return ((ore * 3600) +( minuti * 60) + secondi)

# def time_difference(ore, minuti, secondi, ore2, minuti2, secondi2):
    
#     if (seconds_since_noon(ore, minuti, secondi) - seconds_since_noon(ore2, minuti2, secondi2)) >= 0:
        
#         return seconds_since_noon(ore, minuti, secondi) - seconds_since_noon(ore2, minuti2, secondi2)
    
#     else:
        
#         return seconds_since_noon(ore2, minuti2, secondi2) - seconds_since_noon(ore, minuti, secondi)



# def rimbalzo() -> None:
    
#     tempo: int = 0
#     altezza: float = 0.0
#     velocità: float = 100.0
#     rimbalzi: int = 0

#     while rimbalzi != 5:
        
#         if altezza >= 0.0:
            
#             print(f"Tempo: {tempo} Altezza: {altezza}")
#             altezza += velocità
#             velocità -= 96
        
#         else:
            
#             print(f"Tempo: {tempo} Rimbalzo!")
#             altezza *= -0.5 
#             velocità *= -0.5
#             rimbalzi += 1
        
#         tempo += 1



# def memorizza_file(files: list[int]) -> None:
    
#     spazio_totale_blocchi = 1000  # Spazio totale disponibile in blocchi
    
#     for i in files:
        
#         j = i * 0.8
        
#         if (spazio_totale_blocchi - round((j / 512), 0)) >= 0:
            
#             spazio_totale_blocchi -= round((j / 512), 0)
            
#             print(f"File di {i} byte compresso in {j} byte e memorizzato. Blocchi usati: {int(round((j / 512), 0))}. Blocchi rimanenti: {int(spazio_totale_blocchi)}.")
            
#         else:
            
#             print(f"Non è possibile memorizzare il file di {i} byte. Spazio insufficiente.")
#             break