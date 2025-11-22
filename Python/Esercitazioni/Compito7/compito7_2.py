# 2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
# classifichi i numeri in liste separate per numeri positivi e negativi.


def function2(lista_n: list) -> dict:

    diz: dict[str, list[int]] = {"Positivi" : [], "Negativi" : []}
    
    for n in lista_n:
        
        if n >= 0:
            
            diz["Positivi"].append(n)
            
        else:
            
            diz["Negativi"].append(n)

    return diz
    
lista_n: list= [1, -2, 3, -4, 5]
print(function2(lista_n))