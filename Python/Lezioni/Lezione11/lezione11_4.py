def recursiveDigitCounter(n: int):
    if abs(n) < 10:
        
        return 1
    else:
        
        return 1 + recursiveDigitCounter(n // 10)

print(recursiveDigitCounter(500))