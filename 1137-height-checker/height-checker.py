class Solution:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        ans = []
        i = j = 0

        while len(left) > i and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1
            
        ans.extend(left[i:])
        ans.extend(right[j:])

        return ans

    def heightChecker(self, heights: List[int]) -> int:
        expected = heights
        res = self.merge_sort(heights)
        cnt = 0

        for i in range(0, len(expected)):
            if res[i] != expected[i]:
                cnt += 1

        return cnt