class Solution(object):
    def singleNumber(self, nums):
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        
        for k, v in dic.items():
            if v == 1:
                return k