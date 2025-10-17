class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 1:
            return 0
        cheap = prices[0]
        max_profit = set()
        for i in range(1, len(prices)):
            stock = prices[i]
            if cheap > stock:
                cheap = stock
            max_profit.add(stock - cheap)
        profit = max(max_profit)
        return profit