class Solution(object):
    def majorityElement(self, nums):
        check = len(nums) / 2
        hash_map = {}  

        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1

        for k, v in hash_map.items():
            if v > check:
                return k