import re


def Anagram_Checker(text1: str, text2: str) -> bool:
    
    text1 = re.sub(r'[^a-zA-Z]', '', text1).lower()  #comoda la regex per togliere tutto ciò che non è alfabetico anche spazi
    text2 = re.sub(r'[^a-zA-Z]', '', text2).lower()
    
    print(text1, text2)
    
    text1 = ''.join(sorted(text1))
    text2 = ''.join(sorted(text2))
    
    return text1 == text2