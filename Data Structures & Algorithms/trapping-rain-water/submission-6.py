class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        res = 0
        while l < r:
            curr_l = height[l] 
            curr_r = height[r]
            if curr_l <= curr_r:
                l += 1
                if curr_l <= maxl:
                    res += maxl - curr_l
                else:
                    maxl = curr_l
            else:
                r -= 1
                if curr_r <= maxr:
                    res += maxr - curr_r
                else:
                    maxr = curr_r
                


        return res
