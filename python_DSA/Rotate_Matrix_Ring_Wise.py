def rotate_matrix_ringwise(m,r):
    for row in m:
        print(row)
    print()

    r = len(m)
    c = len(m[0])

    # range is no of shells possible
    for s in range(1,max(r,c)+1):
        array = shell2array(m,s)
        if array != []:
            print("Array From Shell: {} \n".format(array))
            rotated_array = rotate_One_D(array,1) # Positive values for clockwise and negative for ACW
            print("Rotated Array From Shell: {} \n".format(rotated_array))
            array2shell(rotated_array,m,s)

    for row in m:
        print(row)

def rotate_One_D(ar,r):
    r = -r
    r = r%len(ar)
    # We are assuming it to be clockwise
    ar = ar[len(ar) - r:] + ar[:len(ar)-r]
    return ar

def shell2array(m,s):
    # for rotation of outermost shell s
    ltr = s-1
    ltc = s-1

    rbr = len(m) - s
    rbc = len(m[0]) - s 

    temp = []

    #add left wall to temp
    for i in range(ltr,rbr + 1):
        temp.append(m[i][ltc])

    # add bottom wall
    for j in range(ltc+1,rbr):
        temp.append(m[rbr][j])
    
    # add right wall
    for i in range(rbr,ltr-1,-1):
        temp.append(m[i][rbc])
    
    # add top wall
    for j in range(rbr-1,ltr,-1):
        temp.append(m[ltr][j])
    
    return temp

def array2shell(ar,m,s):
    # for rotation of outermost shell s
    ltr = s-1
    ltc = s-1

    rbr = len(m) - s
    rbc = len(m[0]) - s 

    k = 0

    #add left wall to temp
    for i in range(ltr,rbr + 1):
        m[i][ltc] = ar[k]
        k+= 1
    # add bottom wall
    for j in range(ltc+1,rbr):
        m[rbr][j] = ar[k]
        k+= 1
    
    # add right wall
    for i in range(rbr,ltr-1,-1):
        m[i][rbc] = ar[k]
        k += 1
    
    # add top wall
    for j in range(rbr-1,ltr,-1):
        m[ltr][j] = ar[k]
        k += 1

if __name__ == '__main__':
    mat = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
        ]
    rotate_matrix_ringwise(mat,1)