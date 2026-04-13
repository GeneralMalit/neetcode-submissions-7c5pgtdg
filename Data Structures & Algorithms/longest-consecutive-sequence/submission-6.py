class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set()
        for i in nums:
            hs.add(i)
        maxrun = 0
        for i in nums:
            current_run = 1
            if i-1 in hs:
                continue
            while i + 1 in hs:
                i += 1
                current_run += 1
            maxrun = max(current_run, maxrun)
        return maxrun