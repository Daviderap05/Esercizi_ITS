import random, time

l: list[int] = [random.randint(0, 100000) for _ in range(0, 100)]

start = time.time()

if 7 in l:
    print(True)
else:
    print(False)
    
end = time.time()

print(f"Tempo di esecuzione: {round((end - start), 6)} secondi")

start = time.time()

if 7 in sorted(l):
    print(True)
else:
    print(False)
    
end = time.time()

print(f"Tempo di esecuzione: {round((end - start), 6)} secondi")