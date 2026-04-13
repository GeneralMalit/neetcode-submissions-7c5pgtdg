class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = -prices[0]
        sell = 0
        wait = 0

        for i in range(1, len(prices)):
            p_hold = hold
            p_sell = sell
            p_wait = wait

            hold = max(p_hold, p_wait - prices[i])
            sell = p_hold + prices[i]
            wait = max(p_wait, p_sell)

        return max(sell, wait)