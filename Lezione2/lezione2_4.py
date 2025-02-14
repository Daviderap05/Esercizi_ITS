n_tutor: int = 10
attesa: int = 0

while n_tutor != 0 or attesa < 20:
    
    studente: str = str(input(f"Inserire il nome dello/a studente/ssa: "))
    print("")
    
    if n_tutor > 0:
        
        n_tutor -= 1
        print("Tutor assegnato con successo")
        print("")
        
    else:
        
        attesa += 1
        print("Studente in attesa")
        print("")
        
print("Limite raggiunto nella lista d'attesa")
