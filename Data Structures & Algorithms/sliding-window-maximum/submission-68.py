from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        q, res = deque(), []
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            while q and r - q[0] == k:
                q.popleft()
            if r >= k - 1:
                res.append(nums[q[0]])
        return res 