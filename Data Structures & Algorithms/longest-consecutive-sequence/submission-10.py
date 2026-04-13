class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxrun = 0
        numset = set(nums)
        for i in numset:
            if i - 1 not in numset:
                run = 1
                while i + 1 in numset:
                    i += 1
                    run += 1
                maxrun = max(maxrun, run)
        return maxrun