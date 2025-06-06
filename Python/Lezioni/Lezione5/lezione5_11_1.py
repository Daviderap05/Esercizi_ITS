#prima parte copiata dall'esercizio 5_1

pizzas: list[str] = ["Margherita", "Boscaiola", "Bufala"]

# for i in pizzas:
    
#     print(i)

# for i in range(len(pizzas)):
    
#     print(f"La mia {i + 1}° pizza preferita è: {pizzas[i]}")
    
# print(f"A me piace la {pizzas[0]}")
# print(f"A me piace la {pizzas[1]}")
# print(f"A me piace la {pizzas[2]}")

# print(f"A me piace tanto la pizza!")

friend_pizzas: list[str] = pizzas[ : ]
#friend_pizzas: list[str] = list(pizzas)    metodo alternativo

pizzas.append("Vegetariana")
friend_pizzas.append("Capricciosa")

print("Le mie pizze preferite sono: " + ", ".join(pizzas))
print("Le pizze preferite del mio amico sono: " + ", ".join(friend_pizzas))

#uso join piuttosto che un ciclo per unire (essendoci delle stringhe nella lista) gli
#elementi delle liste al print (list comprehension)