#esercizio per rendere super efficente la somma da 1 a n

num: int = int(input("inserire un num: "))

print(f"La somma di tutti i numeri da 1 a {num} è: {int((num + 1) * (num / 2))}")



#modo efficente per ribaltare stringhe
#caso di negativi e positivi

x: int = int(input("inserire un num: "))
s = str(x)  #si trasforma il numero in una stringa

if(s[0] == "-"):
    
    s = s[1:]
    s = "-" + s[::-1]
    print(s)
    
else:
    
    s = s[::-1]
    x = int(s)
    print(x)
    
