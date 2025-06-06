#prima parte copiata dal precedente esercizio

lista: list[int] = list(range(1, 11))
num: list[int] = []

num = [n ** 3 for n in lista]

print(*num, sep = ", ")

print(f"The first three items in the list are: {lista[0 : 3]}")
print(f"Three items from the middle of the list are: {lista[3 : 6]}")
print(f"The last three items in the list are: {lista[-3 : ]}")