class Solution:
    def sumAndMultiply(self, n: int) -> int:

        if n == 0:
            return 0
        
        s = res = 0
        m = 1

        while (n > 0):
            d = n % 10

            if d != 0:
                res = d * m + res
                m *= 10
                s += d
            
            n //= 10
        
        return res * s
        
