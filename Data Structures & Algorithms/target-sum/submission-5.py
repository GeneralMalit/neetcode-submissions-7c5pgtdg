class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total < target) or (target + total) % 2 != 0:
            return 0
        
        subset_target = (target + total) // 2

        dp = [0] * (subset_target + 1)
        dp[0] = 1
        print(dp)
        for num in nums:
            for i in range(subset_target, num - 1, -1):
                dp[i] += dp[i - num]
        
        
        return dp[subset_target]