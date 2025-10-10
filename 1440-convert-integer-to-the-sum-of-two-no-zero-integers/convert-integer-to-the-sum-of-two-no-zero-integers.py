class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n+1):
            a = i
            b = n - i
            a = str(a)
            b = str(b)
            if "0" in a or "0" in b:
                continue
            else:
                ans.append(a)  
                ans.append(b)   
                return ans   