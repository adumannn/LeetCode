class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        if len(nums) == 1 and k == 0:
            return 0

        n = len(nums)

        pref_max = [0] * len(nums)
        pref_max[0] = nums[0]

        result = [0] * n
        result[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            result[i] = min(result[i+1], nums[i])

        for i in range(1, len(nums)):
            pref_max[i] = max(pref_max[i - 1], nums[i])

        for i in range(0, n):
            res = pref_max[i] - result[i]
            if res <= k:
                return i

        return -1