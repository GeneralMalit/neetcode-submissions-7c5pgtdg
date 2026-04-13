class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        maximum = 0
        jumps = 0
        for i in range(len(nums) - 1):
            maximum = max(maximum, i + nums[i])
            if i == max_reach:
                print(f"max_reach = {max_reach}")
                jumps += 1
                max_reach = maximum
            

    
        return jumps