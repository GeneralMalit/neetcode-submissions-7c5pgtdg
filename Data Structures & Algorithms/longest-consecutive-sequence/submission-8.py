class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxrun = 0
        for i in s:
            if i - 1 not in s:
                run = 1
                while i + 1 in s:
                    i = i + 1
                    run += 1
                maxrun = max(maxrun, run)
        return maxrun