class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        ans = 1

        for number in str(n):
            digits.append(int(number))

        digits.sort()

        ans = digits[-1] * digits[-2]
        
        return ans