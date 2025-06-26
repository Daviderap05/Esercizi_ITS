import random

def genera(dim: int) -> list[list[int]]:

    if dim < 2 or not isinstance(dim, int):
        
        raise ValueError ("Errore... numero inserito non valido o minore di 2.")

    return [random.sample(range(0, 14), dim) for _ in range(dim)]


def printMAT(matrice: list[list[int]]) -> None:
    
    #[print("    ".join(map(str, l)), end="\n\n") for l in matrice] mia versione anche se non è formattata al massimo

    for r in range(len(matrice)):

        for c in range(len(matrice[r])):

            print(f"{matrice[r][c]:<5}", end="")

        print("\n")


def calcolaCarico(matrice: list[list[int]], r: int, c: int):
    
    if not matrice or not isinstance(c, int) or not isinstance(c, int):
        
        raise ValueError ("Errore... indici e/o matrice non valida/i")
    
    somma1: int = 0
    somma2: int = 0

    # for l in range (len(matrice)):    fatta da me          
            
    #     for i in range (len(matrice[l])):
            
    #         if l == r:
                
    #             somma1 += matrice[l][i]
                
    #         if i == c:
                
    #             somma2 += matrice[l][i]
                
                
    somma1 = sum(matrice[r])
    
    for row in range(len(matrice)):
        somma2 += matrice[row][c]
    
    return (somma1 - somma2)
            
            
        
    
print(calcolaCarico([[6, 7, 0, 5], [5, 11, 4, 9], [0, 5, 9, 7], [6, 11, 10, 9]], 1, 3))