class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxh = 0
        while l < r:
            if heights[l] > heights[r]:
                width = r - l
                print(f"l = {l}, r = {r}, width = {width}, heights = {heights[l]},{heights[r]}, maxh = {max(maxh, width * heights[r])}")
                maxh = max(maxh, width * heights[r])
                r -= 1
            else:
                width = r - l
                print(f"l = {l}, r = {r}, width = {width}, heights = {heights[l]},{heights[r]}, maxh = {max(maxh, width * heights[l])}")
                maxh = max(maxh, width * heights[l])
                l += 1
        return maxh