class Solution:
    def countCommas(self, n: int) -> int:
        cnt = 1
        if n >= 1000:
            for i in range (1000, n):
                cnt += 1
            return cnt
        return 0