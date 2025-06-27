lista_n: list[int] = []
numeri_piu_frequenti: list[int] = []
somma_p: int = 0
somma_d: int = 0
count_d: int = 0
max_freq: int = 0

while True:
    
    try:
        
        n: int = int(input(f"Inserisci un numero (0 per terminare): "))
        
        if n == 0:
            
            break
            
        else:
            
            lista_n.append(n)
            
    except ValueError:
        
        print("Errore inserire solo numeri interi... Riprovare\n")

print("")

if len(lista_n) != 0:
       
    for i in lista_n:
        
        if i % 2 == 0:
            
            somma_p += i
            
        else:
        
            somma_d += i
            count_d += 1

    for num in lista_n:
        
        freq = lista_n.count(num)
        
        if freq > max_freq:
            
            max_freq = freq
            numeri_piu_frequenti = [num]
        
        elif freq == max_freq and num not in numeri_piu_frequenti:
            
            numeri_piu_frequenti.append(num)
            
    print(f"Somma dei numeri pari: {somma_p}")

    if count_d > 0:
        
        print(f"Media dei numeri dispari: {somma_d / count_d}")

    else:
        
        print("Nessun numero disparo inserito")

    print(f"Numero/i più frequente/i: {', '.join(map(str, numeri_piu_frequenti))} ({max_freq} volte)")

else:
    
    print("Non hai inserito alcun numero... addio")