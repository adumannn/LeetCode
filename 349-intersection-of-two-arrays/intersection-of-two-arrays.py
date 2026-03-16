class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        ans = []
        for inter in n2:
            if inter in n1:
                ans.append(inter)

        return ans