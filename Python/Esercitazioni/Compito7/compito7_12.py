def sum_primary_diagonal(matrix: list[list[int]]) -> int:
    
    somma: int = 0
    
    for i in range(len(matrix)):
        
        somma += matrix[i][i]
        
    return somma


def sum_secondary_diagonal(matrix: list[list[int]]) -> int:
    
    somma: int = 0
    
    for i in range(len(matrix)):
        
        somma += matrix[i][(len(matrix)-1)-i]
        
    return somma


mat1: list[list[int]] = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
]

print(sum_primary_diagonal(mat1)) # restituisce 1 + 5 + 9 = 15
print(sum_secondary_diagonal(mat1)) # restituisce 3 + 5 + 7 = 15