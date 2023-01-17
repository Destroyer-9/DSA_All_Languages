def generate(self, numRows: int) -> list[list[int]]:
    n = numRows
    result = [[1],[1,1]]
    if n == 1:
        return [[1]]
    if n== 2:
        return result
    
    for i in range(2,n):
        temp = [1]*(i+1)
        
        for j in range(1,i):
            temp[j] = result[i-1][j-1] + result[i-1][j]
            
        result.append(temp)
    
    return result