def school_grading(name:str, scores: list[int]) -> str:
    
    average: float = 0.0
    
    for score in scores:
        
        average += score
        
    average /= len(scores)
    
    if average >= 60:
        
        return f"{name} pass the exam with an average of {average:.2f}"
        
    else:
        
        return f"{name} fail the exam with an average of {average:.2f}"
    
    
students: list[(str, list[int])] = [
    
    ("Alice", [70, 80, 90]),
    ("Bob", [50, 40, 55]),
    ("Charlie", [60, 65, 70])
    
]

for name, scores in students:
    
    result: str = school_grading(name, scores)
    print(result)