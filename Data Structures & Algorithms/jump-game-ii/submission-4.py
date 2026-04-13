class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_reach = 0
        max_reach = 0
        jumps = 0
        for i in range(len(nums) - 1):
            max_reach = max(nums[i] + i, max_reach)
            if i == curr_reach:
                curr_reach = max_reach
                jumps += 1
        return jumps