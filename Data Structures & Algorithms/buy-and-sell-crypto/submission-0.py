class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        start = 0
        end = 1
        profit = 0

        while end < len(prices):
            profit = max(profit, prices[end] - prices[start])
            if prices[end] < prices[start]:
                start = end
            end += 1


        return profit