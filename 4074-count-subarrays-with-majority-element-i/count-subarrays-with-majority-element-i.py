class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        answer = 0
        for l in range(len(nums)):
            count = 0
            for r in range(l, len(nums)):
                if nums[r] == target:
                    count += 1
                if count * 2 > (r - l + 1):
                    answer += 1
        return answer