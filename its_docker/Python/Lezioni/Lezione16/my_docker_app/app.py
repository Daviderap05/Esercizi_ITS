import numpy as np

def main():
    
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    print("Matrice di partenza:")
    print(matrix)
    
    print("\n\nMatrice trasposta:")
    transported_matrix = matrix.T
    print(transported_matrix)
    
if __name__ == "__main__":
    
    main()