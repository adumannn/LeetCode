class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokenMask = 0
        for ch in brokenLetters:
            brokenMask |= 1 << (ord(ch) - ord('a'))
        
        count = 0
        for word in text.split():
            wordMask = 0
            for ch in word:
                wordMask |= 1 << (ord(ch) - ord('a'))
            if wordMask & brokenMask == 0:
                count += 1
        return count