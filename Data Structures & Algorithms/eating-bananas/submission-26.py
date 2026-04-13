import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        time = float("inf")
        rate = 0
        while l <= r:
            m = (l + r) // 2
            time = sum(math.ceil(float(i / m)) for i in piles)
            print(f"at speed of {m}, we eat it at {time}")
            if time <= h: #too fast
                rate = m
                r = m - 1
            else: #too slow
                l = m + 1
        return rate

