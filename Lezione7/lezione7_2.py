def check_value(a: int) -> str:
    
    if a < 5:
        
        print(f"{a} è minore di 5")
        
    elif a > 5:
        
        print(f"{a} è maggiore di 5")
        
    else:
        
        print(f"{a} è uguale a 5")
        
check_value(int(input("Inserisci un numero: ")))