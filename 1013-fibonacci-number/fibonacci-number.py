class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        
        dp = [0, 1]
        for _ in range(2, n + 1):
            dp[0], dp[1] = dp[1], dp[0]+dp[1]

        return dp[1]