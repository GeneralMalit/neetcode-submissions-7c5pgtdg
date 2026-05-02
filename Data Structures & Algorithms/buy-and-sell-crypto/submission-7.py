class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(len(prices)):
            sell = prices[r] - prices[l]
            res = max(res, sell)
            if prices[r] < prices[l]:
                l = r

        return res
