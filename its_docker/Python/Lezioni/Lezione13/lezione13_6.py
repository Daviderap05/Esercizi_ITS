from functools import reduce
from typing import Callable

numeri: list[int] = [2, 3, 4]

prodotto: Callable[[list[int]], int] = reduce(lambda x, y: x * y, numeri)

print(prodotto)