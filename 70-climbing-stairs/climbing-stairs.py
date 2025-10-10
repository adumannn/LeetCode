class Solution(object):
    def climbStairs(self, n):
        memo = [-1] * (n + 1)
        return self._climb(n, memo)
    
    def _climb(self, n, memo):
        if n <= 1:
            return 1
        if memo[n] != -1:
            return memo[n]
        
        memo[n] = self._climb(n - 1, memo) + self._climb(n - 2, memo)
        return memo[n]