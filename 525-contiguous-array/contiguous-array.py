class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(0, len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        mp = dict()
        mp[0] = -1

        prefix = 0
        ans = 0

        for i, n in enumerate(nums):
            prefix += n
            if prefix not in mp:
                mp[prefix] = i  
            else:
                ans = max(ans, i - mp[prefix])

        return ans