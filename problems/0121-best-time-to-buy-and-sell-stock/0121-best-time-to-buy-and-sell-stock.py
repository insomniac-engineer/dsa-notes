class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        buyPrice = prices[0]
        profit = 0

        for i in prices:
            buyPrice = min(buyPrice, i)
            profit = max(profit, i - buyPrice)
        return profit
