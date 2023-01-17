def merge(a,b,m,n):
    i = j  = 0
    temp = []

    while i < m and j < n:
        
        if a[i] < b[j]:
            #a[i] is smaller hence it will remain there and i will be incremented
            temp.append(a[i])
            i += 1
        
        elif a[i] >= b[j]:
            # b[j] is smaller hence it neeeds to be inserted at index i
            temp.append(b[j])
            j += 1

    while i < m:
        temp.append(b[j])
        i += 1

    while j < n:
        temp.append(b[j])
        j += 1


    print(temp)
    return None

a = [4]
b = [1,2,3,5,6]

m= len(a)
n = len(b)

merge(a,b,m,n)