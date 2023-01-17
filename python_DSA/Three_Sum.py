def threeSum(nums):
        res = []
        for k in range(len(nums)):
            i = k + 1
            j = len(nums) - 1
            target = -nums[k]

            while i < j:
                if nums[i] + nums[j] == target:
                    res.append([nums[k],nums[i],nums[j]])
                    print(k,i,j)
                    break
                elif nums[i] + nums[j] < target:
                    i += 1
                elif nums[i] + nums[j] > target:
                    j -= 1

        print(res)  

n = [-4, -1, -1, 0, 1, 2]
n = [0,0,0,0]
print(n)
threeSum(n)
    