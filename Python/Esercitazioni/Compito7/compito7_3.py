# 3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
# restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
# con i prezzi aumentati del 10% e arrotondati a due cifre decimali.


def function3(diz: dict) -> dict:

    diz2: dict[str, float] = {}
    
    for key, value in diz.items():
        
        if value <= 50.0:
            
            diz2[key] = round((value * 1.1), 2)
            
    return diz2
    
dizionario = {"maglietta" : 11.5, "felpa" : 12.5, "cappello" : 52}

print(function3(dizionario))