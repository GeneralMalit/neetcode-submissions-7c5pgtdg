class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = -prices[0]
        sell = 0
        wait = 0

        for i in range(1, len(prices)):
            hold1 = hold
            sell1 = sell
            wait1 = wait
            
            hold = max(hold1, wait1 - prices[i])
            sell = hold1 + prices[i]
            wait = max(wait1, sell1)
            print(f"{hold}, {sell}, {wait}")

        return max(wait, sell)