# 5) Scrivi una funzione che moltiplica tutti i numeri interi di una lista che sono minori di un
# dato valore intero definito threshold.


def function5(lista_n: list) -> int:
    
    threshold: int = 5
    prodotto: int = 1
    
    for n in lista_n:
        
        if n < threshold:
            
            prodotto *= n
            
    return prodotto
    
lista_n: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(function5(lista_n))