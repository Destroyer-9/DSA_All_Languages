class Solution:
    def rev(self, n):
        rev = 0
        while n!=0:
            rev = rev*10 + n%10
            n //=10
        return rev
    
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x > 0:
            return x == self.rev(x)
        return False
        
s = Solution()

result = s.isPalindrome(121)

print(result)