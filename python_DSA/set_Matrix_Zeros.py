def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    
    row = set()
    col = set()
    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                row.add(r)
                col.add(c)
    
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in row or c in col:
                matrix[r][c] = 0
                
    return None

def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = 1
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            if matrix[i][0] == 0:
                col = 0
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(m-1,-1,-1):
            for j in range(n-1,0,-1):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
            if not col:
                matrix[i][0] = 0
            
        return None
        