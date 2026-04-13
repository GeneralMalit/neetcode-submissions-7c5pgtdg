class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r  = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        while l < r:
            if maxl < maxr:
                l += 1
                if height[l] > maxl:
                    maxl = height[l]
                else:
                    water += (maxl - height[l])
            
            else:
                r -= 1
                if height[r] > maxr:
                    maxr = height[r]
                else:
                    water += (maxr - height[r])
        return water