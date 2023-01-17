def merge(intervals: list[list[int]]) -> list[list[int]]:
    
    # Sort intervals By their starting points
    intervals.sort(key = lambda x : x[0])
    print("Sorted intervals:{}".format(intervals))
    
    i = 0
    l = len(intervals)
    
    while i < len(intervals)-1:
        
        # Start of current pair is equal to start of next pair
        if intervals[i][0] == intervals[i+1][0]:
            # If end of current pair < end of next pair add [s1 , e2]
            if intervals[i][1] < intervals[i+1][1]:
                intervals[i][1] = intervals[i+1][1]
                intervals.pop(i+1)
                # i will remain where it was as next element was removed 
            # If end of current pair == end of next pair only next pair is removed and i remains as it is
            elif intervals[i][1] == intervals[i+1][1]:
                intervals.pop(i+1)
        
            # If end of current pair > end of next pair then end only next pair is removed and i remains as it is
            elif intervals[i][1] > intervals[i+1][1]:
                intervals.pop(i+1)
        # if start of current pair is less than start of next pair
        elif intervals[i][0] < intervals[i+1][0]:
            
            # If end of current pair < start of next pair
            # then we will keep both intervals and move i by 1
            if intervals[i][1] < intervals[i+1][0]:
                i += 1
            
            # If end of current pair == start of next pair 
            # then we will merge the intervals as [s1,e2] and remove next pair keeping i 
            # as it is
            elif intervals[i][1] == intervals[i+1][0]:
                intervals[i][1] = intervals[i+1][1]
                intervals.pop(i+1)
                # i remain as it is
            # If end of current pair > start of next pair
            elif intervals[i][1] > intervals[i+1][0]:
                # we will further check is end of current pair > end of next pair or
                # not
                if intervals[i][1] > intervals[i+1][1]:
                    intervals.pop(i+1)
                elif intervals[i][1] == intervals[i+1][1]:
                    intervals.pop(i+1)
                elif intervals[i][1] < intervals[i+1][1]:
                    intervals[i][1] = intervals[i+1][1]
                    intervals.pop(i+1)
        print(intervals,i)
    return intervals
            
if __name__ == '__main__':
    ar = [[1,3],[2,6],[8,10],[15,18]]
    ar = [[1,4],[2,7],[6,10]]
    print(ar)
    merge(ar)
    print(ar)

                
                        
                
                
                
                
                
                
                
                
        
        
        