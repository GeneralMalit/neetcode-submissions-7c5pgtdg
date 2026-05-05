class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]
        for k in range(1, n - 1):
          for left in range(n - k - 1):
            right = left + k + 1
            for i in range(left + 1, right):
              dp[left][right] = max(dp[left][right],
              dp[left][i] + dp[i][right] + (nums[left] * nums[i] * nums[right]))
        return dp[0][n - 1]