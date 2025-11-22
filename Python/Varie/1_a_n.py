# #esercizio per rendere super efficente la somma da 1 a n

# num: int = int(input("inserire un num: "))

# print(f"La somma di tutti i numeri da 1 a {num} è: {int((num + 1) * (num / 2))}")



# #modo efficente per ribaltare stringhe
# #caso di negativi e positivi

# x: int = int(input("inserire un num: "))
# s = str(x)  #si trasforma il numero in una stringa

# if(s[0] == "-"):
    
#     s = s[1:]
#     s = "-" + s[::-1]
#     print(s)
    
# else:
    
#     s = s[::-1]
#     x = int(s)
#     print(x)
    
    
#comoda la regex per togliere tutto ciò che non è alfabetico anche spazi    
# import re
# text = "ciao mondo 9 "
# text = re.sub(r'[^a-zA-Z]', '', text).lower() 
# print(text)



#index_c: str = (alphabet.index(letter) + key) % 26   #modulo permette di ricominciare la lista



#text = text.replace(" ", "").lower()   comodo per sostituire a volte per eliminare gli spazi

# per ruotare a destra
# def rotate_right(nums: list[int], k: int) -> list[int]:
    
#     if not nums:
#         return []
    
#     k = k % len(nums)
#     return nums[-k:] + nums[:-k]



#DECORATORI
# import time
# #il decorator prende l'indirizzo di una funzione per decorarla
# def cronometro(fun):
#     def wrapper():
#         start = time.perf_counter()  
#         fun()
#         print(f"{(time.perf_counter() - start):.6f}")
#     return wrapper
 
# @cronometro
# def ciao():
#     print("Hello")
    
# ciao()
#cronometro(ciao()) --> è la stessa cosa



# numeri = [42, 7, 15, 88, 23, 56, 3, 91, 34, 67, 12, 78, 5, 60, 29, 81, 17, 49, 73, 25]
# soglia = 50

# numeri2: list = [n for n in numeri if n > soglia]
# print(", ".join(map(str, numeri2)))
# #or 
# print(", ".join(map(str, [n for n in numeri if n > soglia])))

# s1 = True
# s2 = True
# s3 = True

# if s1 and ((s2 == False or s3 == False)):   
#     print("Attivato")
# else:
#     print("Non attivato")