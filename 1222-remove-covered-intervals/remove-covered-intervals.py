class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0], -x[1]))

        cnt = len(intervals)

        l = 0


        for r in range(len(intervals)-1):
            if intervals[l][0] <= intervals[r+1][0] and intervals[l][1] >= intervals[r+1][1]:
                cnt -= 1
                r += 1
            else:
                l = r + 1

        return cnt