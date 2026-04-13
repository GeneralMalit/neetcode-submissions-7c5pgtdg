class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0 
        for i in nums:
            curr = max(two + i, one)
            two = one
            one = curr
        return curr