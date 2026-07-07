class Solution:
    def sumAndMultiply(self, n: int) -> int:

        if n == 0:
            return 0

        n = str(n)

        ans = 0
        x = ''

        for nums in n:
            if nums != '0':
                x += nums
                ans += int(nums)
        
        return int(x) * ans
        
