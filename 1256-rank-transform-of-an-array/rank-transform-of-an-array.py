class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if arr is None:
            return
        arr_unique = sorted(set(arr))
        rank = {}

        for i, x in enumerate(arr_unique):
            rank[x] = i + 1

        return [rank[x] for x in arr]