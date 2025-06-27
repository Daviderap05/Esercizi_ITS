num: int = int (input(f"inserisci il numero: "))
primo = True

if num < 2:
    print("Il numero non è primo")
else:
    div: int = 2
    
    while div < num:
        
        if (num % div == 0):
            print("Il numero non è primo")
            
            primo = False
            break
        
        div += 1

if primo:
    print("Il numero è primo")
    