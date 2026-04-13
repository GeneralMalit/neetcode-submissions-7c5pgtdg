class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        dp = {0}
        target = total // 2
        for num in nums:
            dp.update({i + num for i in dp})

        return target in dp