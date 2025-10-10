class Solution:
    def largestGoodInteger(self, num: str) -> str:
        listt = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]
        
        for pattern in listt:
            if pattern in num:
                return pattern
        return ""
                