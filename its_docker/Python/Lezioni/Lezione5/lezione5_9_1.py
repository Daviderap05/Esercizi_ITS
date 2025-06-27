lista: list[int] = list(range(1, 11))
num: list[int] = []

num = [n ** 3 for n in lista]

print(*num, sep = ", ")

#Il sep aiuta a dividere tutti gli elementi della lista sep = ", " quando la stampi per intero
#l'end aiuta a dividere gli elementi che vengono passati nel print durante un for o while