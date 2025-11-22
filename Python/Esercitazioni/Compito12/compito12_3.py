def recursivePalindrome(phrase: str) -> bool:
    
    if not isinstance(phrase, str):
        raise Exception("La frase/parola inserita non è valida")
    
    phrase = phrase.replace(" ", "").lower()
    
    if len(phrase) == 0 or len(phrase) == 1:
        return True

    if phrase[0] == phrase[-1]:
        return recursivePalindrome(phrase[1:-1])
    
    else:
        return False
    
    
parola1: str = "radar"
parola2: str = "Anna"
parola3: str = "I topi non avevano nipoti"
parola4: str = "casa"
parola5: str = "Marta"
parola6: str = "Roma e Amore"

print(recursivePalindrome(parola1))
print(recursivePalindrome(parola2))
print(recursivePalindrome(parola3))
print(recursivePalindrome(parola4))
print(recursivePalindrome(parola5))
print(recursivePalindrome(parola6))