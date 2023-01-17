def search(matrix,e):
    m = len(matrix)
    n = len(matrix[0])
    
    i = 0 
    j = n-1
    
    while 0<= i <m and 0 <= j<n:
        print(i,j)

        if matrix[i][j] == e:
            return True

        elif matrix[i][j] < e:
            i += 1

        elif matrix[i][j] > e:
            j -= 1
        
    return False
        
mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
e = 3
print(search(mat,e))