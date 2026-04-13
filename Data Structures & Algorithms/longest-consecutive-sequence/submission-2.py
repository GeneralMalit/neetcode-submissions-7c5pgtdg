class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_streak = 0
        for num in nums:
            if num - 1 not in nums:
                curr_streak = 1
                while num + 1 in nums:
                    num = num + 1
                    curr_streak += 1
                max_streak = max(max_streak, curr_streak)
        return max_streak