class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def hr1(nums):
            n1, n2 = 0, 0
            for i in range(len(nums)):
                curr = max(n2 + nums[i], n1)
                n2 = n1
                n1 = curr
            return n1
        return max(hr1(nums[1:]), hr1(nums[:-1]))

