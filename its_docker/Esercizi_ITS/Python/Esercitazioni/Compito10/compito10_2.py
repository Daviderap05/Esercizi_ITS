def proDict() -> dict[tuple[int, int], int]:
    
    dizionario: dict[tuple[int, int], int] = {}
    
    for x in range (0, 101):
        
        for y in range (2, 89, 2):
            
            ris = x * y
            dizionario[(x, y)] = ris
        
    return dizionario


def main() -> None:
    
    d: dict[tuple[int, int], int] = proDict()

    print(d[(13, 88)])
    print(d[(83, 56)])
    print(d[(71, 44)])
    

if __name__ == "__main__":
    
    main()