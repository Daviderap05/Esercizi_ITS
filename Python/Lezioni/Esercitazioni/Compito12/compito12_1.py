import math

def calculateCharges(ore: float|int) -> float:
    
    if not (ore and isinstance(ore, float|int)):
        raise ValueError ("Numero di ore non valido.")
    
    if ore <= 3:
        return 2.00
    
    elif ore >= 24:
        return 10.00
    
    else:
        
        if ore % 1 != 0:
            ore = math.ceil(ore)
        charge: float = (2 + ((ore - 3) * 0.5))
        
    return charge



hours: list[float, int] = [1.5, 4.0, 5.50, 24.24]
total_h: float|int = sum(hours)

charges: list[float] = [calculateCharges(i) for i in hours]
total_c: float = sum(charges)

print(f"{'Cars':<10}{'Hours':<10}{'Charges':<}")

for i in range(len(hours)):
    print(f" {i + 1:<9}{hours[i]:<10}{charges[i]:<.2f}$")
    
print(f"{'TOTAL':<10}{total_h:<10.2f}{total_c:<.2f}$")