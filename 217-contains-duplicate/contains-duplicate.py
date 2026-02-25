class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = dict()

        for n in nums:
            ans[n] = ans.get(n, 0) + 1

        for k, v in ans.items():
            if v >= 2:
                return True
            
        return False