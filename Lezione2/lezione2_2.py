num_NS: int = int (input("inserisci numero macchine direzione Nord-Sud: "))

num_EO: int = int (input("inserisci numero macchine direzione Est_Ovest: "))

print("")

soglia: int = int (input("Inserire la soglia massima di auto: "))

print("")

tempo_priorità: int = int (input("Inserire il tempo minimo da garantire al superamento della soglia in percentuale: % "))

print("")

if num_NS > soglia:
    
    if num_EO > soglia:
        
        tempo_NS: int = 50
        tempo_EO: int = 50
        
    else:
        
        tempo_NS: int = tempo_priorità
        tempo_EO: int = 100 - tempo_priorità
        
elif num_EO > soglia:
    
    tempo_NS: int = 100 - tempo_priorità
    tempo_EO: int = tempo_priorità
    
else:
    
    veicoli_tot: int = num_NS + num_EO
    tempo_NS: int = (num_NS / veicoli_tot) * 100
    tempo_EO: int = 100 - tempo_NS
    
print(f"Il tempo assegnato alla direzione Nord_Sud è il: {tempo_NS}%")

print(f"Il tempo assegnato alla direzione Est-Ovest è il: {tempo_EO}%")
