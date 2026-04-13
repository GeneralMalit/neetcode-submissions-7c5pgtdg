class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_run = 0
        for i in num_set:
            if i - 1 not in num_set:
                run = 1
                while i + 1 in num_set:
                    run += 1
                    i += 1
                max_run = max(max_run, run)
        return max_run

