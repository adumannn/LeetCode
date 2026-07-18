import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxx = max(nums)
        minn = min(nums)

        return math.gcd(maxx, minn)