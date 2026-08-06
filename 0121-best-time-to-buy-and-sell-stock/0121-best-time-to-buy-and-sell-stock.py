class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        ans = 0

        for i in range(n):
            profit = prices[i] - min_price
            ans = max(ans, profit)
            min_price = min(min_price, prices[i])
        return ans
