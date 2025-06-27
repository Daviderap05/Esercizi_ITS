a: int = int(input(f"Inserire Il primo numero intero positivo: "))
b: int = int(input(f"Inserire il secondo numero intero positivo: "))

if a < b:
    
    if a > 0 and b > 0:
        
        if a % 1 == 0 or b % 1 == 0:
            
            somma: int = 0
            i = a
            
            while i <= b:
                
                somma += i
                i += 1
            
            print(f"La somma è : {somma}")

        else:
            
            print("A e B devono essere interi")
            
    else:
        print("A e B devono essere positivi")

else:
    print("A deve essere minore di B")
    