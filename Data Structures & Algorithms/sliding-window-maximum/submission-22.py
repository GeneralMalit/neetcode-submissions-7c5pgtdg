from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        l = 0

        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            
            dq.append(r)

            while dq[0] <= r - k:
                dq.popleft()
            
            if r >= k - 1:
                res.append(nums[dq[0]])

        return res