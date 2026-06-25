class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = dict()
        mp[0] = 1

        prefix = 0
        ans = 0

        for n in nums:
            prefix += n
            ans += mp.get(prefix - k, 0)
            mp[prefix] = mp.get(prefix, 0) + 1

        return ans