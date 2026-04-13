class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0
        while l <= r:
            m = (l + r) // 2
            time = 0
            #ceil division: x/y = (x+y-1) // y
            for i in piles:
                time += (i + m - 1) // m
            print(f"with {m}, we got time={time}")
            if time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res