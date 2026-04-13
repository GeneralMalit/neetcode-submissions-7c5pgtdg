class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxp = 0
        for r in range(len(prices)):
            maxp = max(maxp, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
        return maxp

            
