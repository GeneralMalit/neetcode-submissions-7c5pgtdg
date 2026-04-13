class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = h

        while left <= right:
            k = (left + right) // 2
            time = 0
            for p in piles:
                time += (k + p - 1) // k
            
            if time <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        
        return res
