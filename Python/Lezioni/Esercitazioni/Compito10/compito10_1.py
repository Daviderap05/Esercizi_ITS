def isDNA(dna_s: str) ->bool:
    
    for d_s in dna_s.upper():
        
        if d_s not in ["A", "C", "G", "T"]:
            
            return False
        
    return True


def fusionDNA(s1: str, s2: str) -> str:
    
    if not isDNA(s1) or not isDNA(s2):
        raise ValueError ("Errore")
    
    print("")
    
    for i in s1[0:]:
        print(i, end="")
        
    print("")
    
    for j in s2[-1::-1]:
        print(j, end="")
        
    print("\n")
    
    
fusionDNA("AAGCTTACG", "ACGTTCGA")