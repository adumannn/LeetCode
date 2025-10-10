class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        k = n // 2
        for i in range(1, k+1):
            ans.append(i)
            ans.append(-i)

        if n % 2 == 0:
            return ans

        ans.append(0)
        return ans