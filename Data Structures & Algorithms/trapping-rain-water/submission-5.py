class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        trapped = 0
        maxl, maxr = height[l], height[r]
        while l < r:
            if height[l] >= height[r]: #r moves
                
                
                if height[r] < maxr:
                    trapped += (maxr - height[r])
                else:
                    maxr = max(maxr, height[r])
                r -= 1

            else: #l moves
                if height[l] < maxl:
                    trapped += (maxl - height[l])
                else:
                    maxl = max(maxl, height[l])

                l += 1

        return trapped