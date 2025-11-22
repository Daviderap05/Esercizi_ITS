import random
import os


_log_matrice = None

def check_matrice(matrice: list[list[int]]) -> None:
    
    global _log_matrice
    
    if _log_matrice != matrice:
        
        if not isinstance(matrice, list) or not matrice or not all(isinstance(row, list) and row for row in matrice):
            
            raise ValueError("Errore... matrice non valida o vuota.")
        
        if any(len(row) != len(matrice) for row in matrice):
            
            raise ValueError("Errore... la matrice deve essere quadrata.")
        
        _log_matrice = matrice


def pulisci_terminale() -> None:
    
  """Pulisce il terminale."""
  
  if os.name == 'nt': # Se il sistema operativo è Windows
      
    os.system('cls')
    
  else: # Se il sistema operativo è Unix-like
      
    os.system('clear')
    
    
def genera() -> list[list[int]]:

    while True:
        
        try:
            
            dim: int = int(input("Inserisci un numero intero >= 2: "))
            
            if dim < 2:
                
                raise ValueError ("Errore... numero inserito non valido o minore di 2, riprova.\n")
            
            break
            
        except ValueError:
            
            print("Errore... numero inserito non valido o minore di 2, riprova.\n")

    #return [random.sample(range(0, dim), dim) for _ in range(dim)] metodo fatto da me ma non è preciso per la traccia
    
    mat: list[list[int]] = []
    
    for r in range(dim):
        
        row: list[int] = []
        
        for c in range(dim):
            
            while True:
                
                x: int = random.randint(0, dim)
                
                if c == 0:
                    
                    row.append(x)
                    break
                
                if x != row[0]:
                    
                    row.append(x)
                    break
                
        mat.append(row)
        
    return mat


def printMAT(matrice: list[list[int]]) -> None:
    
    check_matrice(matrice)
    
    #[print("    ".join(map(str, l)), end="\n\n") for l in matrice] mia versione anche se non è formattata perfettamente con gli spazi

    for r in range(len(matrice)):

        for c in range(len(matrice[r])):

            print(f"{matrice[r][c]:<5}", end="")

        print("\n")


def calcolaCarico(matrice: list[list[int]], r: int, c: int) -> int:
    
    check_matrice(matrice)
    
    if not isinstance(r, int) or not isinstance(c, int):
        
        raise ValueError("Errore... indici non interi.")
    
    if not (0 <= r < len(matrice)) or not (0 <= c < len(matrice)):
        
        raise ValueError("Errore... indici fuori dai limiti della matrice.")
    
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
            
            
def caricoNullo(matrice: list[list[int]]) -> list[tuple[int, int]]|str:
    
    check_matrice(matrice)
    
    lista_nulli: list[tuple[int, int]] = []
    
    for row in range(len(matrice)):
        
        for col in range(len(matrice)):
            
            if calcolaCarico(matrice, row, col) == 0:
                
                lista_nulli.append((row, col))
                
    return lista_nulli if lista_nulli else "Non sono presenti coppie riga-colonna con valore 0."
   
   
def caricoMax(matrice: list[list[int]]) -> tuple[int, int]:

    check_matrice(matrice)
    
    max_carico: int = calcolaCarico(matrice, 0, 0)
    tupla_max: tuple[int, int] = (0, 0)
    
    for row in range(len(matrice)):
        
        for col in range(len(matrice)):
            
            ris: int = calcolaCarico(matrice, row, col)
            
            if ris > max_carico:
                
                max_carico = ris
                tupla_max = (row, col)
                
    print(f"Il carico massimo è: {max_carico}.")
    return tupla_max
                
    
def caricoMin(matrice: list[list[int]]) -> tuple[int, int]:

    check_matrice(matrice)
    
    min_carico: int = calcolaCarico(matrice, 0, 0)
    tupla_min: tuple[int, int] = (0, 0)
    
    for row in range(len(matrice)):
        
        for col in range(len(matrice)):
            
            ris: int = calcolaCarico(matrice, row, col)
            
            if ris < min_carico:
                
                min_carico = ris
                tupla_min = (row, col)
                
    print(f"Il carico minimo è: {min_carico}.")
    return tupla_min            
                
   
def main() -> None:
    
    pulisci_terminale()
    
    matrice: list[list[int]] = genera()
    
    print("\n" + "-" * 40, end="\n\n")
    
    print("Matrice generata:", end="\n\n")
    printMAT(matrice)
    
    print("-" * 40, end="\n\n")
    
    print("Coordinate a carico nullo:")
    print(caricoNullo(matrice), end="\n\n")
    
    print("-" * 40, end="\n\n")
    
    max_pos: tuple[int, int] = caricoMax(matrice)
    print(f"Coordinate con carico massimo: {max_pos}, Valore: {calcolaCarico(matrice, *max_pos)}", end="\n\n")

    print("-" * 40, end="\n\n")

    min_pos: tuple[int, int] = caricoMin(matrice)
    print(f"Coordinate con carico minimo: {min_pos}, Valore: {calcolaCarico(matrice, *min_pos)}", end="\n\n")


if __name__ == "__main__":
    
    main()