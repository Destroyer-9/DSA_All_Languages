nums = [1,3,2]

def nextPermutation(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        temp = nums.copy()
        temp.sort(reverse = True)
        if nums == temp:
            nums.reverse()
            return
        
        n = len(nums)
        for i in range(n-2,-1,-1):
            # find first decreasing seq
            if nums[i]<nums[i+1]:
                idx = i 
                for j in range(n-1,idx,-1):
                    if nums[j] > nums[idx]:
                        idy = j
                        break
                nums[idx],nums[idy] = nums[idy], nums[idx]
                # Rotate From Idx + 1 
                print(nums)
                nums[idx+1::].reverse()
                print(nums)
                
                for k in range(n)
                # nums = nums[:idx+1:] + nums[idx+1::].reverse()
                
                # for k in range(1,(n-1-idx)//2):
                #     nums[idx+k],nums[n-k] = nums[n-k],nums[idx+k]    
                break
            
        return None
print(nums)
nextPermutation(nums)             
'''
def find_next_perm(seq):
    # find first decreasing sequence
    temp = seq.copy()
    temp.sort(reverse = True)

    if seq == temp:
        return seq[::-1]

    n = len(seq)

    for i in range(n-1,0,-1):
        
        if seq[i] > seq[i-1]:
            print("Old Sequence",seq)

            ptr = i-1

            for j in range(ptr + 1,n):
                if seq[j] > seq[ptr]:
                    ptr1 = j
                    
                
            seq[ptr1],seq[ptr] = seq[ptr],seq[ptr1]
            l_nxt = seq[ptr + 1::][::-1]
            nx = seq[:ptr+1:] + l_nxt
            print("New Sequence",nx)
            return nx
            
    

curr_perm = list(map(int, input("Enter: ").split()))
print(find_next_perm(curr_perm))
        
'''