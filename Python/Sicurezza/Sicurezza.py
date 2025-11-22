from functools import reduce


xor: int = 57
stringa: str = "Nel mezzo del cammin di nostra vita"

#con comprehension
lista_crip: list[int] = [ord(cha) ^ xor for cha in stringa]
lista_decrip: list[int] = [chr(n ^ xor) for n in lista_crip]

print(lista_crip, end="\n\n") 
print("".join(map(str, lista_decrip)))

# con i for:
# for cha in stringa:
#     lista.append(ord(cha) ^ x)
        
# print(lista, end="\n\n") 
 
# for n in lista:
#     print(chr(n ^ x), end="")

#professore  
print(reduce(lambda x,y: x+y, map(lambda x : chr(x ^ xor), map(lambda c: ord(c) ^ xor, list(stringa))), ""))