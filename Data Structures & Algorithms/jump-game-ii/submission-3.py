class Solution:
    def jump(self, nums: List[int]) -> int:
        maximum = 0
        reach = 0
        jumps = 0
        for i in range(len(nums) - 1):
            maximum = max(maximum, i + nums[i])
            if i == reach:
                jumps += 1
                reach = maximum
        return jumps