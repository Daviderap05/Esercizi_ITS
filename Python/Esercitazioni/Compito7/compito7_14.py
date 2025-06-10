def merge_intervals(intervals: list[list[int]] = []):
    
    if intervals == []:
        
        return intervals
        
    elif len(intervals) == 1:
        
        if len(intervals[0]) == 2:
            
            if intervals[0][0] > intervals[0][1]:
                
                intervals[0][0], intervals[0][1] = intervals[0][1], intervals[0][0]
            
        return intervals
    
    for lis in intervals:
        
        if len(lis) == 2:
        
            if lis[0] > lis[1]:
                
                lis[0], lis[1] = lis[1], lis[0]
                
        else:
            
            raise Exception ("Inserire solo UNA lista contenente SOLO intervalli di due numeri")
            
    intervals.sort(key=lambda x: x[0])
            
    lista_intervalli: list[list[int]] = []
    
    min: int = intervals[0][0]
    max: int = intervals[0][1]
        
    for i in range(1, len(intervals)):

        for j in range(len(intervals[i])):
            
            if min <= intervals[i][j] <= max and intervals[i][j+1] >= max:
                
                min = intervals[i][j]
                max = intervals[i][j+1]
                
                lista_intervalli.append([min, max])
                break
            
            elif intervals[i][j] > max: #ricodati se due liste sono uguali o se il seondo elemento di una è minore del secondo della seconda lista cioè la precedente
            
                min = intervals[i][j]
                max = intervals[i][j+1]
                
                lista_intervalli.append([min, max])
                break
        
        
        
    

intervals: list[list[int]] = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals) # restituisce [[1, 6], [8, 10], [15, 18]]

intervals: list[list[int]] = [[1, 4], [4, 5]]
merge_intervals(intervals) # restituisce [[1, 5]]