# def blackjack_hand_total(cards: list[int]) -> int:
    
#     somma: int = 0
    
#     for i in range(len(cards)):
    
#         if cards[i] != 11:
            
#             somma += cards[i]
            
#         else:
            
#             somma += cards[i]
            
#             if somma > 21:
                
#                 somma -= 10
                
#     return somma



# def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    
#     new_list: list[int] = x
#     somma: int = 0
#     cont: int = 0
    
#     for i in range(len(y)):
        
#         new_list[i] += y[i]
    
#     return new_list



# def find_disappeared_numbers(nums: list[int]) -> list[int]:
    
#     num: set[int] = set(range(1, len(nums) + 1))
#     nums_set: set[int] = set(nums)
    
#     numeri_mancanti: list[int] = num - nums_set
    
#     return sorted(list(numeri_mancanti))



# def even_odd_pattern(numbers:list[int]) -> list[int]:
    
#     new_list: list[int] = []
#     cont: int = 0
    
#     for i in numbers:
        
#         if i % 2 == 0:
            
#             new_list.insert(cont, i)  
#             cont += 1
            
#         else:
            
#             new_list.append(i)
            
#     return new_list



# def prime_factors(n: int) -> list[int]:
    
#     new_list: list[int] = []
    
#     if n <= 3:
        
#         new_list.append(n)
    
#     else:
        
#         div: int = 2
    
#         while n > 1:
            
#             if (n % div == 0):
                
#                 new_list.append(div)
#                 n //= div
                
#             else:
            
#                 div += 1
    
#     return new_list