class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = -prices[0]
        sold = 0
        rest = 0

        for i in range(1, len(prices)):
            p_hold = hold
            p_sold = sold
            p_rest = rest

            hold = max(p_hold, p_rest - prices[i])
            sold = p_hold + prices[i]
            rest = max(p_rest, p_sold)
        return max(sold, rest)