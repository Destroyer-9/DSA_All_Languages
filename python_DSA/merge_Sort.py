def msort(ar):
    # length of array should always be greater than 1 as if len == 1 then they are considered sorted
    if len(ar)>1:
        # find the middle index
        m = len(ar)//2

        # Divide the array in Left and Right halves
        L = ar[:m]
        R = ar[m:]

        # Sort Left Half
        msort(L)
        # Sort Right Half
        msort(R)

        # Now merge Left and Right Halves
        merge(ar,L,R)
        # Don't Return anything as everything is done in place
 
def merge(ar,L,R):
    i = j = k = 0
    # Compare Elements of L and R and put the smallest one in the arr at position k
    while i < len(L) and j < len(R):
        # if left element is less than right
        if L[i] < R[j]:
            ar[k] = L[i] 
            i +=1 
        
        # if right element is less or equal to left
        elif L[i] >= R[j]:
            ar[k] = R[j]
            j +=1 
        k += 1
    
    # Fill the remaining elements of left into ar
    while i < len(L):
        ar[k] = L[i]
        i +=1
        k += 1
    
    # Fill the remaining elements of right into ar
    while j < len(R):
        ar[k] = R[j]
        j +=1
        k += 1
    # return nothing as values are already in place and pointed by call by reference


if __name__=='__main__':
    nums = [5,4,3,2,1]
    print("Before Sorting: ",nums)
    msort(nums)
    print("After Sorting: ",nums)