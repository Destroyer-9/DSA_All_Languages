def min_SA(nums):
    min_sum = 1e18
    curr_sum = 0

    for n in nums:
        curr_sum += n

        min_sum = min(min_sum,curr_sum)

        if curr_sum > 0:
            curr_sum = 0

    print(min_sum) 


    pass

if __name__=='__main__':
    ar = [3, -4, 2, -3, -1, 7, -5] # result is -6
    ar = [2, 6, 8, 1, 4] # result is 1
    min_SA(ar)
