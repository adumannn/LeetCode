class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n // 10 == 0:
            return False
        
        dig_sum = 0
        dig_product = 1
        
        for digit in str(n):
            d = int(digit)
            dig_sum += d
            dig_product *= d


        total = (dig_sum + dig_product)

        if (n % total) == 0:
            return True
        else:
            return False
        
        