class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")
        maxprice = 0

        for i in prices:
            if i < lowest:
                lowest = i
            else:
                maxprice = max(maxprice, i - lowest)
        return maxprice