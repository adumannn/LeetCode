class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(x, y):
            while y != 0:
                (x, y) = (y, x % y)
            return x
        x = max(nums)
        y = min(nums)

        return gcd(x, y)