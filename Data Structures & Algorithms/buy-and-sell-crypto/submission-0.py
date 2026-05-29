class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - min_so_far

            max_profit = max(max_profit, profit)

            min_so_far = min(min_so_far, prices[i])
        
        return max_profit
        