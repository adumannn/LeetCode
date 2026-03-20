class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) <= 1 and nums[0] == 0:
            return 0
        elif len(nums) <= 1 and nums[0] == 1:
            return 1

        cnt_max = []
        cnt = 0
        n = 0

        for i in range(len(nums)):
            if 1 == nums[i]:
                cnt += 1
                # print("yes")
            else:
                cnt_max.append(cnt)
                cnt = 0

        cnt_max.append(cnt)
        # print(cnt_max)
        return max(cnt_max)