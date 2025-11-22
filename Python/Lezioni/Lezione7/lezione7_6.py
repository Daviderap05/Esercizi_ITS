def add_one(a: int) -> int:
    
    a += 1
    
    return a

def add_one_to_list(lst_n: list[int])   -> str:
    
    new_list: list[int] = []
    
    for i in lst_n:
        
        new_list.append(add_one(i))
        
    print(*new_list, sep = ", ", end = ".")
    
lista: list[int] = [1, 4, 6, 3, 5]

add_one_to_list(lista)