class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxp = 0 

        for r in range(len(prices)):
            price = prices[r]
            if price < prices[l]:
                l = r
            
            maxp = max(maxp, price - prices[l])
        return maxp
