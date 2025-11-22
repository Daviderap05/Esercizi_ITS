def merge_intervals(intervals: list[list[int]] = []) -> list[list[int]]|Exception:
    
    if intervals == []:
        
        return intervals

    for interval in intervals:
        
        if len(interval) != 2 or not isinstance(interval[0], int) or not isinstance(interval[1], int):
            
            raise Exception("Inserire solo intervalli di due numeri.")
        
        if interval[0] > interval[1]:
            
            interval[0], interval[1] = interval[1], interval[0]

    intervals.sort(key=lambda x: x[0])

    lista_intervalli: list[list[int]] = []
    interval_c: list[int] = intervals[0]

    for interval in intervals[1:]:  
        
        if interval[0] <= interval_c[1]:
            
            interval_c[1] = max(interval_c[1], interval[1])
            
        else:
            
            lista_intervalli.append(interval_c)
            interval_c = interval

    lista_intervalli.append(interval_c)
    return lista_intervalli



intervals: list[list[int]] = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals)) # restituisce [[1, 6], [8, 10], [15, 18]]

intervals: list[list[int]] = [[1, 4], [4, 5]]
print(merge_intervals(intervals)) # restituisce [[1, 5]] 

intervals: list[list[int]] = [[1, 3], [1, 3],[1,2],[1,5],[2,5],[2,3], [2,2], [8,10]]
print(merge_intervals(intervals))