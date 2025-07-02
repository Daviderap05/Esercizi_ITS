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
import re
text = "ciao mondo 9 "
text = re.sub(r'[^a-zA-Z]', '', text).lower() 
print(text)



#index_c: str = (alphabet.index(letter) + key) % 26   #modulo permette di ricominciare la lista



#text = text.replace(" ", "").lower()   comodo per sostituire a volte per eliminare gli spazi