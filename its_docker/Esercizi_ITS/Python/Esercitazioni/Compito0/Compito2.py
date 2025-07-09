# def calculate_average(numbers: list[int]) -> float:
    
#     if len(numbers) != 0:
        
#         return sum(numbers) / len(numbers)
    
#     else:
        
#         return 0
    
# print(calculate_average([1, 2, 3, 4, 5]))
# print(calculate_average([]))






# def sum_above_threshold(numbers: list[int], n: int) -> int:
    
#     somma: int = 0
    
#     for i in numbers:
        
#         if i > n:
        
#             somma += i
            
#     return somma


# print(sum_above_threshold([1, 10, 20, 30], 10))
    
# print(sum_above_threshold([15, 5, 25], 20))
    
# print(sum_above_threshold([3, 5, 8], 10))
    
# print(sum_above_threshold([50, 60, 70], 25))
    
# print(sum_above_threshold([2, 5, 1], 1))





# def check_access(username: str, password: str, is_active: bool) -> str:
    
#     if username == "admin" and password == "12345" and is_active == True:
        
#         return "Accesso consentito"
        
#     else:
        
#         return "Accesso negato"
    
# print(check_access("admin", "12345", True))
# print(check_access("admin", "54321", True))



# from typing import Any

# def remove_duplicates(lista: list[Any]) -> list:

    # cont: int = 1
    
    # for i in lista:
        
    #     cont = lista.count(i)
        
    #     while True:
            
    #         if cont != 1:
                
    #             lista.pop(i)
                
    #             cont -= 1
                
    #         else:
                
    #             break
    
#     lista2: list[Any] = []
#     cont: int = 0
    
#     for i in lista:
        
#         if i not in lista2:
            
#             lista2.append(i)
            
#     return lista2

# print(remove_duplicates([1, 2, 3, 1, 2, 4]))
    
    
    
    
    
# def countdown(n: int) -> int:
    
#     while n != -1:
        
#         print(n)
        
#         n -= 1






#(°C × 9/5) + 32 

# def convert_temperature(gradi: int, to_fahrenheit: bool = True) -> float:
    
#     if to_fahrenheit == False:
        
#         return (gradi * 9/5) + 32
    
#     else:
        
#         return (gradi - 32) * 5/9





# def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:

#     set_new = original_set.copy()
    
#     for i in elements_to_remove:
        
#         if i in set_new:
    
#             set_new.remove(i)       
    
#     return set_new



# from typing import Any

# def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    
#     new_dict: dict[Any : Any] = {}
    
#     if dict1 and dict2:
    
#         for key1, value1 in dict1.items():
            
#             for key2, value2 in dict2.items():
                
#                 if key1 == key2:

#                     new_dict.update({key1 : (value1 + value2)})
#                     break
                    
#                 else:
                    
#                     new_dict.update({key1 : value1})
#                     new_dict.update({key2 : value2})
#                     break
         
#     elif not dict1:
        
#         for key2, value2 in dict2.items():
                    
#             new_dict.update({key2 : value2})
            
#     else:
        
#         for key1, value1 in dict1.items():
                    
#             new_dict.update({key1 : value1})
            
#     return new_dict




def check_parentheses(stringa: str) -> bool:
    
    cont: int = 0

    if not stringa or not isinstance(stringa, str):
        raise ValueError ("Inserire una sringa piena.")
        
    for c in stringa:
        
        if c == "(":
            cont += 1
            
        elif c == ")":
            cont -= 1
            
    return True if cont == 0 else False
            
            
            
            
# def check_parentheses(expression: str) -> bool:
#     count = 0  # Contatore per le parentesi aperte

#     for char in expression:
#         if char == "(":
#             count += 1  # Incrementa il contatore per ogni parentesi aperta
#         elif char == ")":
#             count -= 1  # Decrementa il contatore per ogni parentesi chiusa
#             if count < 0:  # Se il contatore diventa negativo, le parentesi non sono bilanciate
#                 return False

#     # Alla fine, il contatore deve essere 0 per essere bilanciato
#     return count == 0

# print(check_parentheses("()()"))
# print(check_parentheses("(()))("))
            
            
            
# def count_isolated(lista: list[int]) -> int:
    
#     cont: int = 0
    
#     if lista:
        
#         for i in range(0, len(lista) + 1):
            
#             if i == 0 and lista[i] != lista[i + 1]:
            
#                 cont += 1
                
#             elif i == (len(lista) - 1) and lista[i] != lista[i - 1]: 
                
#                 cont += 1  
                
#             elif 0 < i < (len(lista) - 1) and lista[i] != lista[i + 1] and lista[i] != lista[i - 1]:
                    
#                     cont += 1
        
#     return cont