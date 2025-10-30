from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    #   # violent solution
    #   profit = 0
    #   for i in range(len(prices)):
    #     for j in range(1, len(prices)-2):
    #       if prices[j] - prices[i] >= 0:
    #         profit = max(profit, prices[j] - prices[i])
    #     return profit


    ## Optimize (one loop, dynamic programming)
        minimum = float('inf')
        max_profit = 0

        for price in prices:
          minimum = min(minimum, price)
          max_profit = max(max_profit, price - minimum)

        return int(max_profit)