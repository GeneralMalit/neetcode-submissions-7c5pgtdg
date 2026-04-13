class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        total_water = 0
        l, r = 0, len(height) - 1

        max_l = height[l]
        max_r = height[r]


        while l < r:
            if max_l < max_r:
                l += 1
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    total_water += max_l - height[l]

            else:
                r -= 1
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    total_water += max_r - height[r]
        
        return total_water