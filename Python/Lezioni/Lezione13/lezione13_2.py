from typing import Callable

somma: Callable[[int, int], int] = lambda x, y: x + y
print(somma(2, 2))