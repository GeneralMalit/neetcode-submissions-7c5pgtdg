from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        rs = deque()

        for i in range(len(nums)):
            while rs and nums[i] > nums[rs[-1]]:
                rs.pop()
            
            rs.append(i)

            if rs[0] == i - k:
                rs.popleft()

            if i >= k - 1:
                res.append(nums[rs[0]])

        return res