import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for num in nums:
            if num > dp[-1]:
                dp.append(num)
            else:
                i = bisect.bisect_left(dp, num)
                dp[i] = num

        return len(dp)
