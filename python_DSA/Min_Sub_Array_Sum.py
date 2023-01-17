def maxSubArray(nums: list[int]) -> int:
        overall_min = 1e18
        current_sum = 0
           
        for n in nums:
            current_sum += n

            if current_sum < overall_min:
                overall_min = current_sum

            if current_sum > 0:
                current_sum = 0
                
        return overall_min

ar = [-2,1,-3,4,-1,2,1,-5,4]

print("Sequence-> ", ar)
print( "Max Sub Array Sum-> ",maxSubArray(ar) )

