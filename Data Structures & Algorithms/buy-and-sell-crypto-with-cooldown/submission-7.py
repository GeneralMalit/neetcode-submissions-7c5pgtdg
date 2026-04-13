class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        hold = -prices[0]
        sold = 0
        wait = 0
        for i in range(1, len(prices)):
            p_hold = hold
            p_sold = sold
            p_wait = wait

            hold = max(p_hold, p_wait - prices[i])
            sold = p_hold + prices[i]
            wait = max(p_wait, p_sold)
            print(f"{hold}. {sold}. {wait}")

        return max(sold, wait)