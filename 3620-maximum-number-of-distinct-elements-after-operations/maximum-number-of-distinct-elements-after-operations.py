class Solution(object):
    def maxDistinctElements(self, nums, k):
        nums.sort()
        cnt, prev = 0, -10**9

        for x in nums:
            low = x - k
            high = x + k
            n = prev + 1
            if n < low:
                n = low
            
            if n <= high:
                cnt += 1
                prev = n

        return cnt