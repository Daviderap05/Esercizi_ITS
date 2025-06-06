def check_each(lst_n: list[int]) -> str:
    
    for a in lst_n:
        
        if a < 5:
        
            print("smaller")
        
        elif a > 5:
            
            print("bigger")
            
        else:
            
            print("equal")
            
lista: list[int] = [1, 4, 6, 3, 5]

check_each(lista)