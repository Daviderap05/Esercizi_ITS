def merge_intervals(intervals: list[list[int]] = []) -> list[list[int]]|list[None]:
    
    if intervals == []:
        
        return intervals
        
    elif len(intervals) == 1:
        
        for lis in intervals:
        
            if lis[0] > lis[1]:
                
                lis[0], lis[1] = lis[1], lis[0]
            
        return intervals
    
    intervals.sort(key=lambda x: x[0])
    
    for lis in intervals:
        
        if lis[0] > lis[1]:
            
            lis[0], lis[1] = lis[1], lis[0]
    
    lista_intervalli: list[list[int]] = []
    
    max: int = intervals[0][0][0]
    min: int = intervals[0][0][1]
    
    # for i in range(1, len(intervals)):
        
    #     if intervals[0][i][0] > min:
            
    #         min = intervals[0][i][0]
            
    #     elif intervals[0][i][0] > min
            
            
        
    

intervals: list[list[int]] = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals) # restituisce [[1, 6], [8, 10], [15, 18]]

intervals: list[list[int]] = [[1, 4], [4, 5]]
merge_intervals(intervals) # restituisce [[1, 5]]