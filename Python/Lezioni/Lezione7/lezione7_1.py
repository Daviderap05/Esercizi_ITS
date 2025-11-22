'''FUNZIONI'''

# somma: int = 0
# for i in range (1, 11):
    
#     somma += i
    
# print(f"Sum of integers from 1 to 10 is {somma}\n")     #oppure: print("Sum of integers from 1 to 10 is ", somma, "\n")

# somma = 0
# for i in range (20, 38):
    
#     somma += i
    
# print(f"Sum of integers from 20 to 37 is {somma}\n")

# somma = 0
# for i in range (35, 50):
    
#     somma += i
    
# print(f"Sum of integers from 35 to 49 is {somma}")


#esercizio con le funzioni


# def somma(a: int, b: int):
    
#     ris: int = 0
#     for i in range(a, (b + 1)):
        
#         ris += i
        
#     return ris

# print(f"Sum of integers from 1 to 10 is {somma(1, 10)}\n")

# print(f"Sum of integers from 20 to 37 is {somma(20, 37)}\n")

# print(f"Sum of integers from 35 to 49 is {somma(35, 49)}")

# #oppure

# #mia_somma: int = somma(35, 49)
# #print(f"Sum of integers from 35 to 49 is {mia_somma}")


#prova con input


# def somma(a: int, b: int):
    
#     ris: int = 0
#     for i in range(a, (b + 1)):
        
#         ris += i
        
#     print("")
        
#     return ris

# print(f'Sum is {somma(int(input("Inserisci il primo numero: ")), int(input("Inserisci il secondo numero: ")))}')


#Esercizio sottrazione


# def subtract(a: int, b: int):
    
#     ris: int = a - b
    
#     return ris

# print("Facciamo la sottrazione tra due numeri! \n")

# print(f'\nLa differenza tra i 2 numeri è: {subtract(int(input("Inserisci il primo numero: ")), int(input("Inserisci il secondo numero: ")))}')


#definizione funzione senz return


# def greet(name:str) -> None:
    
#     print(f"Hello {name}!")

# greet("Angela")


# define a function returning multiple values(returning a tuple)


# def operations(a: int, b: int) -> tuple[int, int]:
    
#     sum_result: int = a + b
    
#     diff_result: int = a - b
    
#     # Returns a tuple with two values
    
#     return sum_result, diff_result

# # Assigns values to two variables

# sum_value, diff_value = operations(10, 5)

# print("Sum:", sum_value) # Output: Sum: 15

# print("Difference:", diff_value) # Output: Difference: 5

# print(type(operations(10,5)))