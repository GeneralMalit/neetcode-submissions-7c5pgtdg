class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1

        l_max = height[l]
        r_max = height[r]

        res = 0

        while l < r:
            if l_max < r_max:
                l += 1
                if height[l] < l_max:
                    res += l_max - height[l]
                else:
                    l_max = height[l]
            
            else:
                r -= 1
                if height[r] < r_max:
                    res += r_max - height[r]
                else:
                    r_max = height[r]
        return res