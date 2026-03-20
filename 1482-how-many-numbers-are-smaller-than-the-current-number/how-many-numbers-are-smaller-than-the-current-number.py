class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        num = sorted(nums)

        cnt = 0
        res = []

        for i in range(len(nums)):
            dum = nums[i]
            for n in num:
                if dum > n:
                    cnt += 1
                
            res.append(cnt)
            cnt = 0

        return res