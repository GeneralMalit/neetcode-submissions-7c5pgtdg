class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp, l = 0, 0
        res = 0
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxp = max(maxp, prices[r] - prices[l])
        return maxp
