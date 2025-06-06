def check_length(stringa: str) -> str:
    
    if len(stringa) > 10:
        
        print("La stringa inserita ha più di 10 caratteri")
    
    elif len(stringa) < 10:
        
        print("La stringa inserita ha meno di 10 caratteri")
        
    else:
        
        print("La stringa inserita ha 10 caratteri")
        
check_length(input("Inserisci una stringa: "))