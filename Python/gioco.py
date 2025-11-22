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

print("--------------------------------------------------------------------------------------------")

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

print("--------------------------------------------------------------------------------------------")

# def flatten_once(nested: list[list[int]]) -> list[int]:
    
#     lst = []
    
#     for i in nested:
#         for j in i:
#             lst.append(j)
            
#     return lst

print("--------------------------------------------------------------------------------------------")

# def get_or_default(d: dict, k, default=None):
    
#     if k not in d:
#         return default
    
#     return d[k]

print("--------------------------------------------------------------------------------------------")

# def merge_overwrite(a: dict, b: dict) -> dict:
    
    
#     for key, value in b.items():
#         if key not in a:
#             a[key] = value
#         else:
#             a[key] = value
            
#     return a

print("--------------------------------------------------------------------------------------------")

# def invert_unique(d: dict) -> dict:
    
#     d2 = {}
    
#     for key, value in d.items():
#         d2[value] = key
        
#     return d2

print("--------------------------------------------------------------------------------------------")

# def letter_count(text: str) -> dict[str,int]:
    
#     d = {}
    
#     if not text:
#         return d
    
#     text = text.lower()
    
#     for l in text:
        
#         if l not in d and l.isalpha():
#             d[l] = text.count(l)
            
#     return d    

# mia_stringa = "Questa è una frase di esempio è 9"
# print(letter_count(mia_stringa))

print("--------------------------------------------------------------------------------------------")

# Per aprire l'armeria, percorri istruzioni annidate fino all'arma esatta. 
# Usa `deep_get(d, path, default)` seguendo chiavi e indici `path` tra dizionari e liste `d`; 
# restituisci il tragitto, ma se si interrompe, restituisci `default`. Mantieni la firma e vinci i test

# def deep_get(d: dict | list, path: list, default=None):
    
    # if not d or not path:
    #     return default
    
    # d_c: dict | list = d
    # for key in path:
    #     if isinstance(d_c, dict | list):
    #         d_c = d_c[key]
    #     # elif isinstance(d_c, list):
    #     #     d_c = d_c[key]
    #     else:
    #         return None
    # return d_c             
            
print("--------------------------------------------------------------------------------------------")

# def first_duplicate(nums: list[int]) -> int | None:
    
#     if not nums:
#         return None
    
#     lst = []
    
#     for n in nums:
#         if n not in lst:
#             lst.append(n)
#         else:
#             return n
#     return None

print("--------------------------------------------------------------------------------------------")

# def unique_count(nums: list[int]) -> int:
    
#     lst = []
    
#     for n in nums:
#         if n not in lst:
#             lst.append(n)
            
#     return len(lst)

print("--------------------------------------------------------------------------------------------")

# def intersection_sorted(a: list[int], b: list[int]) -> list[int]:

#     lst = []

#     for n in a:
#         if n in b and n not in lst :
#             lst.append(n)
           
#     lst.sort()
#     return lst

print("--------------------------------------------------------------------------------------------")

# def symdiff_sorted(a: list[int], b: list[int]) -> list[int]:
    
#     lst = []
        
#     for n in a:
#         if n not in b and n not in lst :
#             lst.append(n)
#     for n in b:
#         if n not in a and n not in lst :
#             lst.append(n)
           
#     lst.sort()
#     return lst

# lista1 = [5, 2, 7, 9]
# lista2 = [5, 7, 9, 3, 4, 1]

# print(symdiff_sorted(lista1, lista2))

print("--------------------------------------------------------------------------------------------")

# def are_anagrams(a: str, b: str) -> bool:
    
#     a = sorted(a.lower().replace(" ", ""))
#     b = sorted(b.lower().replace(" ", ""))
    
#     print(a)
#     print(b)
    
#     if a == b:
#         return True
#     return False

# print(are_anagrams("oss O", "osso"))

print("--------------------------------------------------------------------------------------------")

# def powerset_size(n: int) -> int:
#     return (2 ** n) - 1

print("--------------------------------------------------------------------------------------------")

# def chunk(lst: list[int], size: int) -> list[list[int]]:
    
#     lst4 = []
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
        
#     for i in lst3:
#         lst4.append(sum(i))
        
#     return lst4

# lista = [5, 2, 7, 9, 3, 2, 4, 1]
# print(chunk(lista, 3))
    
print("--------------------------------------------------------------------------------------------")
    
# Nella sala delle cronache devi annotare combo ripetute in forma compatta: implementa `rle(s)` 
# restituendo tuple `(carattere, conteggio)` in ordine; se non c'è nulla da contare, `[]`.

# def rle(s: str) -> list[tuple[str,int]]:
    
#     if not s or s == "":
#         return []
    
#     lista: list = []
#     lista2: list[tuple[str,int]] = []
    
#     s = s.lower()
#     for c in s:
        
#         if c not in lista and c.isalpha():
            
#             count = s.count(c)
#             lista.append(c)
#             lista2.append((c, count))
            
#     return lista2
            
            
# print(rle("Ciao come stai"))

print("--------------------------------------------------------------------------------------------")

# def sign(n: int) -> int:
    
#     if n < 0:
#         return -1
    
#     elif n == 0:
#         return 0
    
#     else:
#         return 1

print("--------------------------------------------------------------------------------------------")

# def rotate_right(nums: list[int], k: int) -> list[int]:
    
#     if not nums:
#         return []
    
#     k = k % len(nums)
#     return nums[-k:] + nums[:-k]

# print(rotate_right([1, 2, 3], 7))

print("--------------------------------------------------------------------------------------------")

# Per l’Offerta d’Onore, servi l’esatto ammontare col minor numero di pezzi. 
# Usa `min_coins(amount, coins)`: minimo numero di monete, oppure `1000000000` 
# se non è possibile. Mantieni la firma e vinci i test.


# def min_coins(amount: int = 0, coins: list[int] = [1, 2, 3]) -> int:
#     INF = 1_000_000_000

#     if amount == 0:
#         return 0
#     if not coins:
#         return INF

#     # filtra tagli non validi
#     denoms = [c for c in coins if isinstance(c, int) and c > 0]

#     dp = [INF] * (amount + 1)
#     dp[0] = 0

#     # UNBOUNDED: aggiorna in ordine crescente per consentire il riuso
#     for c in denoms:
#         for s in range(c, amount + 1):
#             if dp[s - c] != INF:
#                 cand = dp[s - c] + 1
#                 if cand < dp[s]:
#                     dp[s] = cand

#     return dp[amount] if dp[amount] != INF else INF

print("--------------------------------------------------------------------------------------------")


def write_and_read(lines: list[str]) -> list[str]:
    
    filename = "textio_write_and_read.txt"

    with open(filename, "w", encoding="utf-8", newline="\n") as f:
        for s in lines:
            if s.endswith("\n"):
                f.write(s)
            else:
                f.write(s + "\n")

    out = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            out.append(line.rstrip("\n"))

    return out

def count_lines(lines: list[str]) -> int:
    
    filename = 'textio_count.txt'
    
    with open(filename, "w", encoding="utf-8", newline="\n") as f:
        for s in lines:
            if s.endswith("\n"):
                f.write(s)
            else:
                f.write(s + "\n")
                
    with open(filename, "r", encoding="utf-8") as f:
        return count