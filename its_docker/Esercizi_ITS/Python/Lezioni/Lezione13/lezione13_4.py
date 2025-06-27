studenti: list[tuple[str, int]] = [("Luca", 21), ("Anna", 19), ("Marco", 22)]

stu_age: list[tuple[str, int]] = sorted(studenti, key = lambda studenti: studenti[1])

print(stu_age)