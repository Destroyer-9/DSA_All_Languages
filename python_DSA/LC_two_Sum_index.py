class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d.keys() and i != d[nums[i]]:
                return [i,d[nums[i]]]
            d[target - nums[i]] = i
                            
s = Solution()

result = s.twoSum([2,7,9,11],9)

print(result)