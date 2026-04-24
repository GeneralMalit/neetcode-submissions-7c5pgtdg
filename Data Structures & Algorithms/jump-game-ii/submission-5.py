class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_reach = 0
        max_reach = 0
        jumps = 0
        for i in range(len(nums) - 1):
            curr_reach = max(curr_reach, i + nums[i])
            if i == max_reach:
                max_reach = curr_reach
                jumps += 1
        return jumps