# def dedup_stable(nums: list[int]):
    
#     lista_n: list[int] = []

#     for i, n in enumerate(nums):
        
#         if i != len(nums)-1:
#             if n != nums[i+1]:
#                 lista_n.append(n)
                
#     lista_n.append(nums[-1])

#     return lista_n

# lista = [5, 4, 2, 2, 2]
# print(dedup_stable(lista))


# def chunk(lst: list[int], size: int) -> list[list[int]]:
    
#     lst3 = []
#     lst2 = []
#     cont = 0
    
#     for n in lst:
        
#         lst2.append(n)
#         cont += 1
        
#         if cont == size:
#             lst3.append(lst2)
#             lst2 = []
#             cont = 0
            
#     if lst2:
#         lst3.append(lst2)
        
#     return lst3

# lista = [5, 2, 7, 9, 3, 2, 4, 1]
# print(chunk(lista, 3))

# def flatten_once(nested: list[list[int]]) -> list[int]:
    
#     lst = []
    
#     for i in nested:
#         for j in i:
#             lst.append(j)
            
#     return lst

# def get_or_default(d: dict, k, default=None):
    
#     if k not in d:
#         return default
    
#     return d[k]

# def merge_overwrite(a: dict, b: dict) -> dict:
    
    
#     for key, value in b.items():
#         if key not in a:
#             a[key] = value
#         else:
#             a[key] = value
            
#     return a

# def invert_unique(d: dict) -> dict:
    
#     d2 = {}
    
#     for key, value in d.items():
#         d2[value] = key
        
#     return d2

def letter_count(text: str) -> dict[str,int]:
    
    d = {}
    
    if not text:
        return d
    
    parole = text.lower().split()
    
    for p in parole:
        
        if p not in d and p.isalpha():
            d[p] = parole.count(p)
            
    return d    

mia_stringa = "Questa è una frase di esempio è 9"
print(letter_count(mia_stringa))
