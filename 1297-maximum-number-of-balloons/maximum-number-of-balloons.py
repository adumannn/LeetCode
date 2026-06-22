class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        test = ['b', 'a', 'n']

        for test_ch in test:
            if test_ch not in text:
                return 0
            
        freq = {}

        for c in text:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        res = []

        for cnt in list(freq.items()):
            if cnt[0] == 'l':
                res.append(cnt[1] // 2)
            if cnt[0] == 'o':
                res.append(cnt[1] // 2)
            if cnt[0] in test:
                res.append(cnt[1])

        return min(res)