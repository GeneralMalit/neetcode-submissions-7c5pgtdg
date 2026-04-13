class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0:
            return 0

        subset_target = (total + target) // 2
        dp = [0] * (subset_target + 1)
        dp[0] = 1

        for num in nums:
            for i in range(subset_target, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[subset_target]