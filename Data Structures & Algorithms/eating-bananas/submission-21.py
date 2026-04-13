import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0 #minimum eating rate to finish within h hours
        l, r = 1, max(piles)

        while l <= r:
            #working eating rate
            m = (l + r) // 2 
            time = 0
            #calculate time taken to eat all piles
            for i in piles: 
                time += math.ceil(i / m)
            if time > h:
                l = m + 1
            else:
                res = m
                r = m - 1
                


        return res