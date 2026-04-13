class Solution:
    def rob(self, nums: List[int]) -> int:
        n1, n2 = 0, 0

        for i in range(len(nums)):
            curr = max(n1 + nums[i], n2)
            n1 = n2
            n2 = curr
        return max(n1, n2)