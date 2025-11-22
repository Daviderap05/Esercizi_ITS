from typing import Callable

square: Callable[[int], int] = lambda x: x ** 2
print(square(2))