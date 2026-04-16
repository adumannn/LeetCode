class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_map = {score[i]: i for i in range(len(score))}
        score.sort(reverse=True)

        res = ["" for _ in range(len(score))]

        for i in range(len(score)):

            if i == 0:
                res[score_map[score[i]]] = "Gold Medal"
            elif i == 1:
                res[score_map[score[i]]] = "Silver Medal"
            elif i == 2:
                res[score_map[score[i]]] = "Bronze Medal"
            else:
                res[score_map[score[i]]] = str(i + 1)

        return res