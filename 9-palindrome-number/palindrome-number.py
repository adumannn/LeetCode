class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        x2 = str(x)
        x2 = x[::-1]
        if x == x2:
            return True
        return False
        