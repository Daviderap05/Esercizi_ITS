from typing import Callable

p_d: Callable[[int], str] = lambda x: "Pari" if x % 2 == 0 else "Dispari"

print(p_d(2))