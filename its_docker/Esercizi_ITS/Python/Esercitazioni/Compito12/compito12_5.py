def baricentro(v: list[int]) -> int:
    
    if not isinstance(v, list) or not all(isinstance(x, int) for x in v) or not v:
        raise Exception ("Inserire un lista, non vuota, di numeri interi")
    
    v_sum: int = sum(v)
    somma: int = 0
    
    for i, num in enumerate(v):
        somma += num
        v_sum -= num
        
        if v_sum == somma:
            return i
        
    return None
        
        
def printResult(v: list[int]) -> None:
    
    ris: int|None = baricentro(v)
    
    if ris is not None:
        print(f"Esiste il baricentro del vettore v = {v} ed è dato dall'indice i = {ris}!\n")
        
    else:
        print(f"Il baricentro del vettore v = {v} non esiste!\n")   
        
        
def main() -> None:
    
    v1: list[int] = [1, 2, 3, 2, 5, 2, 1]
    v2: list[int] = [2, 0, -1, 4, 6, 3, -1]
    
    printResult(v1)
    printResult(v2)
    
    
if __name__ == "__main__":
    main()