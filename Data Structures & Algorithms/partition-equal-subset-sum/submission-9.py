class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        dp = {0}
        for i in nums:
            dp.update({i + j for j in dp})
        return total // 2 in dp