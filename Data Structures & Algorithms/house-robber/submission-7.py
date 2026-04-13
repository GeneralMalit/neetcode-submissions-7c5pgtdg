class Solution:
    def rob(self, nums: List[int]) -> int:
        n1, n2 = 0, 0
        for i in range(len(nums)):
            curr = max(n2 + nums[i], n1)
            n2 = n1
            n1 = curr
        return n1