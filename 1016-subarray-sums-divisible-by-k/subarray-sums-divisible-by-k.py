class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1

        prefix = 0
        ans = 0

        for n in nums:
            prefix += n
            remain = prefix % k

            ans += mp[remain]
            mp[remain] += 1

        return ans
