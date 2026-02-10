class Solution(object):
    def addDigits(self, num):
        if num % 10 == num:
            return num
        rem = num / 10
        rem2 = num % 10
        sol = rem + rem2
        
        return self.addDigits(sol)
            