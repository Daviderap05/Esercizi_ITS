from typing import Callable

parole: list[str] = ["cane", "gatto", "elefante", "ratto", "orso"]

parols: Callable[[list[str]], list[str]] = list(filter(lambda x: len(x) > 4, parole))

print(parols)