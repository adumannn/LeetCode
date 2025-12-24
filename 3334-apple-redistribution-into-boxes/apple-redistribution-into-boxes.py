class Solution(object):
    def minimumBoxes(self, apple, capacity):
        cnt = 0
        sum_apple = sum(apple)
        sum_cap = sum(capacity)
        if sum_apple == sum_cap:
            return len(capacity)

        capacity.sort()
        capacity.reverse()
        for i in capacity:
            sum_apple -= int(i)
            cnt+=1
            if sum_apple <= 0:
                return cnt