class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minp = float("inf")
        for i in range(len(prices)):
            curr = prices[i]
            if curr < minp:
                minp = curr
            res = max(res, curr - minp)
        return res