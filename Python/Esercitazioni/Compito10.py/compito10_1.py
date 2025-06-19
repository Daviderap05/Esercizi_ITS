def isDNA(dna_s: str) ->bool:
    
    for d_s in dna_s.upper():
        
        if d_s != "A" or d_s != "C" or d_s != "G" or d_s != "T":
            
            return False
        
    return True