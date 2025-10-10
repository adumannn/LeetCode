class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        # return True if math.log(n, 3) else False
        # return True if n % 1162261467 == 0 else False
        return True if 1162261467 % n == 0 else False