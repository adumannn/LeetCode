class Solution:
    def countCommas(self, n: int) -> int:
        temp = 1000
        ans = 0

        while temp <= n:
            ans = n - temp + 1
            temp *= 1000
        
        return ans