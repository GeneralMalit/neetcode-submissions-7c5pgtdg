class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        maxArea = 0
        stack = []
        for idx, val in enumerate(heights):
            while stack and heights[stack[-1]] > val:
                h = heights[stack.pop()]
                w = idx if not stack else idx - stack[-1] - 1
                maxArea = max(maxArea, h * w)
            stack.append(idx)
        return maxArea